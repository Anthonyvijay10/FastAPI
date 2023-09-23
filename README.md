# SVM_Titanic_FastAPi
It predicts the survival of a person in titanic dataset

PROCEDURE TO RUN THE FAST API:

1. Install FastAPI and a Web Server:

First, make sure you have Python installed on your system.

Install FastAPI using pip:

Copy code
pip install fastapi
Additionally, you'll need a web server. Uvicorn is a popular ASGI server recommended for FastAPI:

Copy code
pip install uvicorn

2. Create a FastAPI Application:

Create a Python file (e.g., main.py) where you'll define your FastAPI application.
3. Define Your API Endpoints:

Use FastAPI decorators like @app.get() or @app.post() to define your API endpoints.
Define functions for each endpoint that specify the route, request parameters, request body, and response model.
4. Run the Application with Uvicorn:

Use the uvicorn command to run your FastAPI application:

css
Copy code
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Replace main with your Python file name (without the .py extension) and app with the name of your FastAPI application instance.

The --host and --port options specify the host and port on which your application will run.

The --reload option enables automatic code reloading during development.

5. Access Your API:

Once the application is running, you can access your API in a web browser or use tools like curl or Postman to make HTTP requests to the defined endpoints.
6. Documentation and Interactive API Testing:

FastAPI automatically generates interactive API documentation at /docs or /redoc when you run the application in development mode. You can use these web interfaces to test and explore your API.
7. Production Deployment:

For production deployment, consider using a production-ready web server like Gunicorn in front of Uvicorn.
Set up appropriate security, logging, and monitoring for your production environment.
Here's a minimal example of a FastAPI application:

python
Copy code
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
To run this application, save it in a file (e.g., main.py) and run:

bash
Copy code
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Your FastAPI application will be available at http://localhost:8000 by default. You can define more complex routes, request handling, and data models as needed for your specific API.
