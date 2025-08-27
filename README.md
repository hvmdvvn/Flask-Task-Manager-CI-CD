# Flask Task Manager API

This repository contains a **Task Manager REST API** built with **Flask**, **SQLAlchemy**, and **Swagger (Flasgger)**.
The project demonstrates a production-ready setup with:

* User and task management APIs
* SQLAlchemy ORM with SQLite (development) and support for PostgreSQL/MySQL (production)
* API documentation with Swagger UI
* Unit testing using Pytest
* Continuous Integration and Deployment (CI/CD) with GitHub Actions
* Docker support for containerized deployment

---

## Features

* User Management: create, list, and delete users
* Task Management: create, list, update, and delete tasks
* Health Check endpoint (`/health`)
* Swagger documentation available at `/docs`
* Pytest integration with automated test execution in GitHub Actions
* Docker image build and push to DockerHub via GitHub Actions

---

## Project Structure

```
Flask-Task-Manager-CI-CD/
├── app/
│   ├── __init__.py          # Application factory
│   ├── database.py          # Database setup
│   ├── models/              # SQLAlchemy models
│   │   ├── user.py
│   │   ├── task.py
│   ├── routes/              # API routes
│   │   ├── user_routes.py
│   │   ├── task_routes.py
│   │   ├── health_routes.py
├── tests/
│   ├── test_api.py          # Unit and integration tests
├── Dockerfile
├── requirements.txt
├── .github/workflows/ci-cd.yml
├── README.md
```

---

## Prerequisites

* Python 3.12+
* pip (Python package manager)
* Docker (for containerized deployment)
* GitHub account with repository access (for CI/CD)

---

## Local Development Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/Flask-Task-Manager-CI-CD.git
   cd Flask-Task-Manager-CI-CD
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   flask run
   ```

5. Access Swagger documentation:

   * URL: [http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs)

---

## Running Tests

Tests are implemented with Pytest. To execute:

```bash
pytest -v
```

---

## Docker Usage

### Build the Docker image:

```bash
docker build -t flask-taskmanager .
```

### Run the container:

```bash
docker run -p 5000:5000 flask-taskmanager
```

### Pull from DockerHub (after CI/CD push):

```bash
docker pull <your-dockerhub-username>/flask-taskmanager:latest
docker run -p 5000:5000 <your-dockerhub-username>/flask-taskmanager:latest
```

---

## GitHub Actions (CI/CD)

A GitHub Actions workflow is included in `.github/workflows/ci-cd.yml`.

### Workflow Overview

* On push or pull request to `main`:

  1. Code is checked out
  2. Python dependencies are installed
  3. Tests are executed with Pytest
  4. DockerHub login is performed (using secrets)
  5. Docker image is built and pushed to DockerHub

### Required GitHub Secrets

* `DOCKERHUB_USERNAME` → Your DockerHub username
* `DOCKERHUB_TOKEN` → DockerHub Personal Access Token with read/write permissions

---

## Example API Usage

### Create a User

**Request:**

```http
POST /api/users/
Content-Type: application/json

{
  "email": "string",
  "password": "string",
  "username": "string"
}
```

**Response:**

```json
{
  "id": 1,
  "email": "string",
  "password": "string",
  "username": "string"
}
```

---

### Create a Task

**Request:**

```http
POST /api/tasks/
Content-Type: application/json

{
  "description": "string",
  "title": "string",
  "user_id": 0
}
```

**Response:**

```json
{
  "id": 1,
  "title": "Complete documentation",
  "description": "Write detailed README",
  "completed": false,
  "user_id": 1
}
```

---

## Next Steps

1. **Deployment Options**

   * Deploy using Docker to platforms like Render, Railway, Heroku, AWS ECS, or DigitalOcean.
   * Add GitHub Actions workflow for automatic deployment after successful builds.

2. **Database Enhancements**

   * Switch from SQLite to PostgreSQL or MySQL in production.
   * Implement migrations using Alembic.

3. **Authentication & Authorization**

   * Add JWT-based authentication using `flask-jwt-extended`.
   * Restrict task endpoints to authenticated users.

4. **Improved Testing**

   * Add integration and end-to-end test coverage.
   * Include coverage reports in CI/CD pipelines.

5. **Monitoring & Logging**

   * Add structured logging.
   * Enhance `/health` endpoint to include database connectivity checks.

6. **Optional Frontend Integration**

   * Build a frontend (React, Vue, or Next.js) to consume the API.
   * Use Docker Compose to run both frontend and backend services together.

