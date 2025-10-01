# Pastebin API

This project is a simple Pastebin-like API built with Django and Django Rest Framework. It allows users to create, share, and manage code snippets through a browsable web API with user authentication.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.x
*   pip

### Installation

1.  **Clone the repository:**
    ```sh
    git clone <your-repo-url>
    cd drf-official
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    python -m venv env
    source env/bin/activate
    ```

3.  **Install the dependencies:**

    Create a `requirements.txt` file with the following content:

    ```
    Django
    djangorestframework
    drf-yasg
    pygments
    ```

    Then, install the packages:
    ```sh
    pip install -r requirements.txt
    ```

4.  **Run the database migrations:**
    ```sh
    python manage.py migrate
    ```

5.  **Start the development server:**
    ```sh
    python manage.py runserver
    ```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

The API provides the following endpoints:

*   `GET /`: The root of the API, providing access to the other endpoints.

### Snippets

*   `GET, POST /snippets/`: List all snippets or create a new snippet.
*   `GET, PUT, DELETE /snippets/<int:pk>/`: Retrieve, update or delete a specific snippet.
*   `GET /snippet/<int:pk>/highlight/`: Retrieve a highlighted HTML representation of a snippet.

### Users

*   `GET /users/`: List all users.
*   `GET /users/<int:pk>/`: Retrieve a specific user.

## API Documentation

This project uses `drf-yasg` to generate API documentation. You can access the documentation at the following URLs:

*   **Swagger UI**: `http://127.0.0.1:8000/swagger/`
*   **ReDoc UI**: `http://127.0.0.1:8000/redoc/`

## Important Information

*   **Authentication**: The API uses Django's built-in authentication system. You can log in and out of the browsable API via the `/api-auth/` endpoint.
*   **Pagination**: The list views are paginated, with a default page size of 10.
