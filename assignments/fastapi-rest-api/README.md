# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI. This assignment helps students practice defining endpoints, working with request and response data, and organizing backend code for a small web service.

## 📝 Tasks

### 🛠️	Create Basic API Endpoints

#### Description
Set up a FastAPI application that includes a few basic endpoints for a school-themed resource, such as books, courses, or assignments.

#### Requirements
Completed program should:

- Create a FastAPI app in the provided starter file.
- Include at least one `GET` endpoint that returns a welcome message or list of sample data.
- Include at least one `GET` endpoint with a path parameter, such as an item ID.
- Run successfully with `uvicorn` and return JSON responses.


### 🛠️	Add Data Creation and Validation

#### Description
Expand the API so users can send data to the server and receive a structured response using FastAPI models.

#### Requirements
Completed program should:

- Define a Pydantic model for the resource being managed by the API.
- Add a `POST` endpoint that accepts JSON request data.
- Return the created item in the response.
- Validate required fields through the FastAPI model.
