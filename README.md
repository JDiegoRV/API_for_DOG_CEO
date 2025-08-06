# API for DOG CEO

An internal FastAPI server that connects to the DOG CEO API (https://dog.ceo/dog-api/) and stores dog image requests in a MongoDB database and need JWT authentication for all endpoints.

# Install Dependecies

1. First, clone this repository to your local machine:

You need Python 3.11+ installed on your machine.

```bash
git clone https://github.com/JDiegoRV/API_for_DOG_CEO.git
cd API_for_DOG_CEO
```

2. Create a virtual environment

First you need to temporarily change the execution policy to allow the virtual environment activation script to run..
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
```
PowerShell:
python -m venv venv
```
3. Activate the virtual environment in your terminal with the proyect
```
venv\Scripts\Activate.ps1
```
4. For install dependencies from the `requirements.txt` open your terminal and execute:
```
pip install -r requirements.txt
```
# How to set up MongoDB locally

1. Download and Install MongoDB

Go to the official MongoDB Community Edition download page:
https://www.mongodb.com/try/download/community

2. MongoDB will run on the default connection string and when you send the first request of a dog breed MongoDB will automatically create the database and the collection.

# How to run the FastAPI server locally.

1. With MongoDB installed and the requirements.txt dependencies, we now run the FastAPI server locally in your terminal with:
```
uvicorn app.main:app --reload
```
2. The server will then be available at "http://127.0.0.1:8000"

3. Now you can use Postman or the SwaggerUI to make requests to the endpoints 

4. ENDPOINTS:

  a. POST /login 

You need to introduce in the body:
```
  {
  "username": "admin",
  "password": "admin"
  }
```
With this your are going to receive a "access_token" that you will need for the other GET type requests (this has the default duration)

For use this in POSTMAN, when you make a GET type request you need to go to the "Authorization" and select "Bearer Token" and put the token you receive before you send the request or you are gonna receive "an Invalid or missing JWT token" mesagge.

With SwaggerUI, you have a green button in the upper right corner that says "Authorization", click it and enter the token you received, with this all your GET requests will be authorized

  b. GET /dog/breed/{breed_name}

First you need authorization with a token obtained with the POST /login request.

When you make the request, you need to enter the name of a valid dog's breed. With this, you will receive, as a user, only the URL with a random image of a dog's breed you requested. All other data obtained will be saved in the database (timestap, status, and the name of the dog's breed).

  c. GET /dog/stats

First you need authorization with a token obtained with the POST /login request.

When you make the request, you will receive a list of up to 10 of the most requested dogs with the request GET /dog/breed/{breed_name}, which will show the name of the breed and the number of requests.

# How to run the pytest tests.

This project includes unit tests located in the test_main.py file.

1. Run the tests using:
```
pytest
```
If all tests pass, you will see no errors in the output.

# The test suite includes the following tests:

 1. test_dog_breed_success

Logs in to obtain a valid JWT access token.

Sends a request to the /dog/breed/{breed_name} endpoint with the token.

Verifies that the response status is 200 OK.

Checks that the returned JSON contains an image_url starting with https://.

 2. test_save_dog_request

Directly calls the save_dog_request function to insert a test entry into MongoDB.

Ensures the function executes without raising any exceptions.

# Swagger configuration file

This API includes an automatically generated Swagger interface provided by FastAPI.
Once the server is running locally, you can access the documentation at:

Swagger UI: http://localhost:8000/docs
