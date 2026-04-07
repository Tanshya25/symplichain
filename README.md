# SympliChain — Hackathon Project

## Overview

**SympliChain** is a backend-driven supply-chain API platform developed during a hackathon to demonstrate scalable service architecture, API orchestration, and automated CI/CD deployment workflows.

The project provides a modular backend service exposing health monitoring and core API endpoints, designed for rapid integration with frontend applications and future microservice expansion.

---

## Architecture

```
symplichain/
│
├── backend/                # FastAPI backend service
│   ├── config/             # Application configuration
│   ├── gateway/            # API routes & task handlers
│   ├── app.py              # FastAPI entry point
│   └── requirements.txt
│
├── frontend/               # Frontend client (integration ready)
│
└── .github/workflows/      # CI/CD automation
    └── deploy.yml
```

---

## Tech Stack

### Backend

* FastAPI
* Python 3.12
* Uvicorn ASGI Server
* Celery (task-ready architecture)
* REST API (OpenAPI 3.1)

### DevOps

* GitHub Actions CI/CD
* Automated workflow execution
* Environment-based deployment pipeline

### Frontend

* React (integration ready)

---

## Features

* REST API using FastAPI
* Swagger/OpenAPI documentation
* Health monitoring endpoint
* Modular gateway routing
* Async-ready architecture
* CI/CD pipeline via GitHub Actions
* Scalable project structure

---

## API Documentation

After running locally:

```
http://127.0.0.1:8000/docs
```

Available endpoints:

| Method | Endpoint  | Description          |
| ------ | --------- | -------------------- |
| GET    | `/`       | Home endpoint        |
| GET    | `/health` | Service health check |

Example response:

```json
{
  "status": "SympliChain backend running"
}
```

---

## Local Setup

### 1. Clone Repository

```bash
git clone https://github.com/Tanshya25/symplichain.git
cd symplichain/backend
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run Server

```bash
uvicorn app:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

## CI/CD Workflow

GitHub Actions automatically runs workflows on push.

Pipeline responsibilities:

* Dependency installation
* Backend validation
* Deployment preparation

Workflow file:

```
.github/workflows/deploy.yml
```

---

## Project Goals

* Demonstrate production-style backend architecture
* Enable rapid frontend integration
* Showcase DevOps automation during hackathon development
* Provide extensible API foundation for supply-chain workflows

---

## Future Enhancements

* Authentication & authorization
* Database integration (PostgreSQL)
* Blockchain transaction tracking
* Async job processing via Celery workers
* Containerization using Docker
* Cloud deployment

---

## Contributor

**Tanshya Mishra**
GitHub: https://github.com/Tanshya25

---

## License

This project is created for educational and hackathon purposes.
