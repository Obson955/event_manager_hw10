from builtins import str
import pytest
from pydantic import ValidationError
from datetime import datetime
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, UserListResponse, LoginRequest

# Tests for UserBase
def test_user_base_valid(user_base_data):
    user = UserBase(**user_base_data)
    assert user.nickname == user_base_data["nickname"]
    assert user.email == user_base_data["email"]

# Tests for UserCreate
def test_user_create_valid(user_create_data):
    user = UserCreate(**user_create_data)
    assert user.nickname == user_create_data["nickname"]
    assert user.password == user_create_data["password"]

# Tests for password validation
def test_password_too_short(user_create_data):
    user_create_data["password"] = "Abc1!"  # Only 5 characters
    with pytest.raises(ValidationError) as exc_info:
        UserCreate(**user_create_data)
    assert "Password must be at least 8 characters" in str(exc_info.value)

def test_password_no_uppercase(user_create_data):
    user_create_data["password"] = "abcdefg1!"  # No uppercase
    with pytest.raises(ValidationError) as exc_info:
        UserCreate(**user_create_data)
    assert "Password must contain an uppercase letter" in str(exc_info.value)

def test_password_no_lowercase(user_create_data):
    user_create_data["password"] = "ABCDEFG1!"  # No lowercase
    with pytest.raises(ValidationError) as exc_info:
        UserCreate(**user_create_data)
    assert "Password must contain a lowercase letter" in str(exc_info.value)

def test_password_no_number(user_create_data):
    user_create_data["password"] = "AbcdEfgh!"  # No number
    with pytest.raises(ValidationError) as exc_info:
        UserCreate(**user_create_data)
    assert "Password must contain a number" in str(exc_info.value)

def test_password_no_special_char(user_create_data):
    user_create_data["password"] = "AbcdEfgh1"  # No special character
    with pytest.raises(ValidationError) as exc_info:
        UserCreate(**user_create_data)
    assert "Password must contain a special character" in str(exc_info.value)

# Tests for UserUpdate
def test_user_update_valid(user_update_data):
    user_update = UserUpdate(**user_update_data)
    assert user_update.email == user_update_data["email"]
    assert user_update.first_name == user_update_data["first_name"]

# Tests for UserResponse
def test_user_response_valid(user_response_data):
    user = UserResponse(**user_response_data)
    assert user.id == user_response_data["id"]
    # assert user.last_login_at == user_response_data["last_login_at"]

# Tests for LoginRequest
def test_login_request_valid(login_request_data):
    login = LoginRequest(**login_request_data)
    assert login.email == login_request_data["email"]
    assert login.password == login_request_data["password"]

# Parametrized tests for nickname and email validation
@pytest.mark.parametrize("nickname", ["test_user", "test-user", "testuser123", "123test"])
def test_user_base_nickname_valid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    user = UserBase(**user_base_data)
    assert user.nickname == nickname

@pytest.mark.parametrize("nickname", ["test user", "test?user", "", "us"])
def test_user_base_nickname_invalid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Test for nickname maximum length validation
def test_user_base_nickname_too_long(user_base_data):
    user_base_data["nickname"] = "a" * 31  # 31 characters, exceeding the 30 char limit
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)
        
# Test for reserved nickname validation
@pytest.mark.parametrize("reserved_name", ["admin", "administrator", "system", "root", "superuser", "moderator"])
def test_user_base_reserved_nickname(reserved_name, user_base_data):
    user_base_data["nickname"] = reserved_name
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Parametrized tests for URL validation
@pytest.mark.parametrize("url", ["http://valid.com/profile.jpg", "https://valid.com/profile.png", None])
def test_user_base_url_valid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    user = UserBase(**user_base_data)
    assert user.profile_picture_url == url

@pytest.mark.parametrize("url", ["ftp://invalid.com/profile.jpg", "http//invalid", "https//invalid"])
def test_user_base_url_invalid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Test for URL length validation
def test_user_base_url_too_long(user_base_data):
    # Create a URL that exceeds 2048 characters
    long_url = "https://example.com/" + "a" * 2040
    user_base_data["profile_picture_url"] = long_url
    with pytest.raises(ValidationError) as exc_info:
        UserBase(**user_base_data)
    assert "URL is too long" in str(exc_info.value)

# Test for URL protocol validation
@pytest.mark.parametrize("url", ["invalid-url", "www.example.com", "example.com"])
def test_user_base_url_protocol(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    with pytest.raises(ValidationError) as exc_info:
        UserBase(**user_base_data)
    assert "URL must start with http:// or https://" in str(exc_info.value)

# Test for URL domain validation
@pytest.mark.parametrize("url", ["http://", "https://invalid", "http://invalid."])
def test_user_base_url_domain(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    with pytest.raises(ValidationError) as exc_info:
        UserBase(**user_base_data)
    assert "Invalid URL format" in str(exc_info.value)

# Tests for UserBase
def test_user_base_invalid_email(user_base_data_invalid):
    with pytest.raises(ValidationError) as exc_info:
        user = UserBase(**user_base_data_invalid)
    
    assert "value is not a valid email address" in str(exc_info.value)
    assert "john.doe.example.com" in str(exc_info.value)