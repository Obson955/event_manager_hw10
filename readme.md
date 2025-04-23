# Event Manager: API Testing and Enhancement Project

This repository contains the implementation of various fixes and enhancements to the Event Manager API, focusing on schema validation, data integrity, and security improvements.

## Completed Issues

1. [Schema Field Mismatches in Test Fixtures](https://github.com/Obson955/event_manager_hw10/issues/1) - Fixed mismatches between test fixtures and schema definitions to ensure tests pass correctly.

2. [Enhance Username (Nickname) Validation](https://github.com/Obson955/event_manager_hw10/issues/4) - Improved nickname validation with maximum length constraint and reserved name validation.

3. [Implement Password Complexity Validation](https://github.com/Obson955/event_manager_hw10/issues/6) - Added comprehensive password validation to enforce security requirements.

4. [Fix Duplicate Role Field in UserResponse Schema](https://github.com/Obson955/event_manager_hw10/issues/8) - Removed duplicate role field from UserResponse schema to improve data integrity.

5. [Enhance URL Validation for Profile Fields](https://github.com/Obson955/event_manager_hw10/issues/10) - Improved URL validation with comprehensive checks and better error messages.

6. [Fix Duplicate Fields in UserListResponse Example](https://github.com/Obson955/event_manager_hw10/issues/12) - Fixed duplicate fields in example data to improve documentation clarity.

## Project Image

[Link to Docker Hub Image](https://hub.docker.com/repository/docker/obson/wis_club_api/general) - Link to docker image

## Reflection

Working on this Event Manager API project has been an invaluable learning experience that enhanced both my technical skills and understanding of collaborative development processes. The assignment challenged me to dive deep into FastAPI, Pydantic schemas, and test-driven development while following professional Git workflows.

From a technical perspective, I gained significant experience with schema validation and data integrity. Implementing password complexity validation taught me the importance of robust security measures in user authentication systems. The URL validation enhancements showed me how proper input validation can prevent potential security vulnerabilities and improve user experience by providing clear error messages. I also learned how seemingly small issues like duplicate field definitions can lead to unexpected behavior in an API.

The collaborative aspect of this project was equally enlightening. Following a structured Git workflow with issues, branches, and pull requests demonstrated how proper documentation and process can make development more organized and efficient. Creating detailed issue descriptions and linking them to pull requests helped me understand how good documentation facilitates collaboration and makes codebases more maintainable. This experience has given me a deeper appreciation for software quality assurance and the critical role it plays in developing robust, secure applications.



## Key Improvements

### Enhanced Validation
- Implemented comprehensive password validation with checks for length, uppercase, lowercase, numbers, and special characters
- Added maximum length constraint and reserved name validation for usernames
- Improved URL validation with detailed error messages and edge case handling

### Fixed Schema Issues
- Resolved field name mismatches between test fixtures and schema definitions
- Removed duplicate field definitions in schemas
- Improved example data in schema documentation

### Testing Improvements
- Added comprehensive tests for all validation rules
- Created mock SMTP client to prevent email-related test failures
- Ensured all tests pass with the updated schema definitions

## Technologies Used

- **FastAPI**: Modern, high-performance web framework for building APIs
- **Pydantic**: Data validation and settings management using Python type annotations
- **pytest**: Testing framework for Python
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library
- **JWT**: JSON Web Tokens for secure authentication
- **Git/GitHub**: Version control and collaboration platform

## Resources and Documentation

- **Code Documentation**: The project codebase includes docstrings and comments explaining various concepts and functionalities. Take the time to read through the code and understand how different components work together. Pay attention to the structure of the code, the naming conventions used, and the purpose of each function or class. Understanding the existing codebase will help you write code that is consistent and integrates well with the project.

- **Additional Resources**:
 - [SQLAlchemy Library](https://www.sqlalchemy.org/) - SQLAlchemy is a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a set of tools for interacting with databases, including query building, database schema management, and data serialization. Familiarize yourself with SQLAlchemy's documentation to understand how it is used in the project for database operations.
 - [Pydantic Documentation](https://docs.pydantic.dev/latest/) - Pydantic is a data validation and settings management library for Python. It allows you to define data models with type annotations and provides automatic validation, serialization, and deserialization. Consult the Pydantic documentation to understand how it is used in the project for request/response validation and serialization.
 - [FastAPI Framework](https://fastapi.tiangolo.com/) - FastAPI is a modern, fast (high-performance) Python web framework for building APIs. It leverages Python's type hints and provides automatic API documentation, request/response validation, and easy integration with other libraries. Explore the FastAPI documentation to gain a deeper understanding of its features and how it is used in the project.
 - [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/index.html) - Alembic is a lightweight database migration tool for usage with SQLAlchemy. It allows you to define and manage database schema changes over time, ensuring that the database structure remains consistent across different environments. Refer to the Alembic documentation to learn how to create and apply database migrations in the project.

- **API Documentation**: `http://localhost/docs` - The Swagger UI documentation for the API, providing information on endpoints, request/response formats, and authentication.
- **Database Management**: `http://localhost:5050` - The PGAdmin interface for managing the PostgreSQL database, allowing you to view and manipulate the database tables.
This assignment is designed to challenge you, help you grow as a developer, and prepare you for the real-world responsibilities of a Software QA Analyst/Developer. By working on realistic issues, collaborating with your team, and focusing on testing and quality assurance, you will gain valuable experience that will serve you throughout your career.

Remember, the goal is not just to complete the assignment but to embrace the learning journey. Take the time to understand the codebase, ask questions, and explore new concepts. Engage with your team members, seek feedback, and learn from their experiences. Your dedication, curiosity, and willingness to learn will be the key to your success in this role.

We are excited to have you on board and look forward to seeing your contributions to the project. Your fresh perspective and skills will undoubtedly make a positive impact on our team and the quality of our software.






