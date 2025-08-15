# Simple User Management API

This is a basic RESTful API built with Flask for managing a collection of users. It allows you to perform CRUD (Create, Read, Update, Delete) operations on user data. The user data is stored in memory and resets every time the application is restarted.

## Technologies Used

* **Language:** Python 3
* **Framework:** Flask

## Dataset

The application starts with a predefined in-memory dataset:
    ```
    {
    "1": {"name": "Akbar", "email": "akbar@example.com"},
    "2": {"name": "Birbal", "email": "birbal@example.com"}
    }
    ```

## Setup and Installation

1.  **Prerequisites:** Make sure you have Python 3 and `pip` installed on your system.
2.  **Install Dependencies:** Install the required Flask library.
    ```
    pip install Flask
    ```
3.  **Run the Application:** Save the code as `app.py` and run the following command in your terminal.
    ```
    python app.py
    ```
    The server will start running on `http://127.0.0.1:5000`.

## API Endpoints

The API provides the following endpoints:

### 1. Get All Users

* **Method:** `GET`
* **Endpoint:** `/users`
* **Description:** Retrieves a list of all users.
* **Example Request:**
    ```
    curl [http://127.0.0.1:5000/users](http://127.0.0.1:5000/users)
    ```
* **Example Response:**
    ```
    {
      "1": {
        "email": "akbar@example.com",
        "name": "Akbar"
      },
      "2": {
        "email": "birbal@example.com",
        "name": "Birbal"
      }
    }
    ```

### 2. Get a Single User

* **Method:** `GET`
* **Endpoint:** `/users/<user_id>`
* **Description:** Retrieves a single user by their ID.
* **Example Request:**
    ```
    curl [http://127.0.0.1:5000/users/1](http://127.0.0.1:5000/users/1)
    ```
* **Example Success Response:**
    ```
    {
      "email": "akbar@example.com",
      "name": "Akbar"
    }
    ```
* **Example Error Response (User Not Found):**
    ```
    {
      "error": "User not found"
    }
    ```

### 3. Create a New User

* **Method:** `POST`
* **Endpoint:** `/users`
* **Description:** Creates a new user. The request body must be a JSON object containing `name` and `email`.
* **Example Request:**
    ```
    curl -X POST -H "Content-Type: application/json" -d '{"name": "Tansen", "email": "tansen@example.com"}' [http://127.0.0.1:5000/users](http://127.0.0.1:5000/users)
    ```
* **Example Success Response:**
    ```
    {
      "data": {
        "email": "tansen@example.com",
        "name": "Tansen"
      },
      "id": 3
    }
    ```

### 4. Update a User

* **Method:** `PUT`
* **Endpoint:** `/users/<user_id>`
* **Description:** Updates an existing user's information. The request body can contain any fields to update.
* **Example Request:**
    ```
    curl -X PUT -H "Content-Type: application/json" -d '{"email": "new.birbal@example.com"}' [http://127.0.0.1:5000/users/2](http://127.0.0.1:5000/users/2)
    ```
* **Example Success Response:**
    ```
    {
      "email": "new.birbal@example.com",
      "name": "Birbal"
    }
    ```

### 5. Delete a User

* **Method:** `DELETE`
* **Endpoint:** `/users/<user_id>`
* **Description:** Deletes a user by their ID.
* **Example Request:**
    ```
    curl -X DELETE [http://127.0.0.1:5000/users/2](http://127.0.0.1:5000/users/2)
    ```
* **Example Success Response:**
    ```
    {
      "result": "User 2 deleted successfully"
    }
    ```
