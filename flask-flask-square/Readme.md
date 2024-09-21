
# Flask Flask-Square API

## Overview

This project is a simple **Square Calculator** application built using Python's Flask framework for both the frontend and backend. The frontend collects input from the user (a number), and the backend calculates and returns the square of that number.

The project has been containerized using **Docker** and can be easily set up and run with **Docker Compose**. The frontend communicates with the backend via a Python-based proxy, eliminating the need for CORS handling.

### Key Features:
- A **backend API** that calculates the square of a number.
- A **frontend** that interacts with the backend through a proxy, avoiding CORS issues.
- **Dockerized** services for easy deployment and development.

## Project Structure

```
.
├── backend/               # Backend service code
│   ├── Dockerfile         # Dockerfile for the backend
│   ├── backend.py         # Flask app for backend logic
│   └── requirements.txt   # Backend dependencies
├── frontend/              # Frontend service code
│   ├── Dockerfile         # Dockerfile for the frontend
│   ├── frontend.py        # Flask app for frontend logic
│   ├── templates/
│   │   └── index.html     # HTML file for user input
│   └── requirements.txt   # Frontend dependencies
├── settings.env           # Environment variables for configuration
├── docker-compose.yml     # Docker Compose configuration
└── README.md              # Project documentation (this file)
```

## Getting Started

### Prerequisites

- **Docker**: Ensure Docker is installed and running on your system. You can download Docker from [here](https://docs.docker.com/get-docker/).
- **Docker Compose**: This project uses Docker Compose to orchestrate the frontend and backend services. Docker Compose is typically included with Docker Desktop.

### Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-repo/flask-flask-square.git
   cd flask-flask-square
   ```

2. Create a `.env` file (or use the provided `settings.env`) and specify the following environment variables:

   ```bash
   BACKEND_PORT=3001
   BACKEND_URL=http://backend:${BACKEND_PORT}
   FRONTEND_PORT=3000
   ```

3. Ensure that `docker-compose.yml` is configured to use the ports and environment variables correctly.

### Running the Application

1. Start the application with Docker Compose:

   ```bash
   docker-compose --env-file settings.env up --build
   ```

2. This will spin up two containers:
   - **Backend**: Accessible on port `3001`.
   - **Frontend**: Accessible on port `3000`.

3. Open your browser and go to `http://localhost:3000`. You will see a simple form where you can input a number. The frontend will send the number to the backend, which will return the square of the number.

### Stopping the Application

To stop the containers, run:

```bash
docker-compose down
```

This will stop and remove the containers but leave the images intact.

### API Endpoints

The backend provides the following API endpoint:

- **GET /square**: Accepts a `number` query parameter and returns the square of the number.

   Example:

   ```bash
   curl "http://localhost:3001/square?number=4"
   ```

   Response:

   ```json
   {
     "number": 4,
     "square": 16
   }
   ```

### Testing the Frontend Proxy

The frontend Flask app acts as a proxy for the backend. The browser communicates only with the frontend, which then handles the request to the backend API.

Test the proxy by visiting `http://localhost:3000` and entering a number into the form. The frontend will handle the request and display the result.

### Environment Configuration

The application uses environment variables to configure ports and backend URLs. You can adjust these settings in the `settings.env` file.

#### Environment Variables:

- `BACKEND_PORT`: Port on which the backend runs (default: `3001`).
- `FRONTEND_PORT`: Port on which the frontend runs (default: `3000`).
- `BACKEND_URL`: URL that the frontend uses to communicate with the backend (set to `http://backend:${BACKEND_PORT}` for Docker networking).

### Example Usage

1. Start the application with Docker Compose.
2. Open a browser and navigate to `http://localhost:3000`.
3. Enter a number in the input field and click "Calculate Square".
4. The result will be displayed below the form.

