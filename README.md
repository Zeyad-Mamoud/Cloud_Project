# Cloud Project

## Overview

This is a cloud-based application designed using Clean Architecture principles. The project is divided into two main parts:

- **Backend:** Implements the business logic, domain rules, and infrastructure services.
- **Frontend:** Provides a user-friendly interface for the application.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Zeyad-Mamoud/Cloud_Project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Cloud_Project
   ```

### Using Docker

1. Build and run the containers:
   ```bash
   docker-compose up --build
   ```
2. Access the frontend at `http://localhost:3000` and the backend at `http://localhost:8000`.

## Project Structure

- **Backend:**
  - `application/`: Contains use cases and business logic.
  - `domain/`: Holds entities and core business rules.
  - `infrastructure/`: Manages external services like Celery or databases.
- **Frontend:**
  - `src/`: Contains React components and logic.

## Future Enhancements

- Add more detailed documentation.
- Implement CI/CD pipeline for automated testing and deployment.
