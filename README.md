# Car Management Web App

This is a simple web application for managing cars. Users can register, log in, and add cars to their profile.

## Features

- **User Authentication:** Users can register and log in to the application securely.
- **Car Management:** Logged-in users can add, view, and manage their cars.
- **JWT Authentication:** JSON Web Tokens (JWT) are used for secure authentication.
- **MySQL Database:** Data is stored in a MySQL database using SQLAlchemy.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your_username/car-management-app.git
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Set up the MySQL database:
   
   - Create a MySQL database named `mycar`.
   - Update the database connection URI in `app.py` with your MySQL configuration.

4. Run the application:

    ```
    python app.py
    ```

## Usage

- Open your web browser and navigate to `http://localhost:5000` to access the application.
- Click on "Sign Up" to create a new account, or "Log In" if you already have an account.
- Once logged in, you can add and manage your cars from the dashboard.

## Controllers

These are the necessary imports for the file.
Blueprint: Used to define a group of related routes.
render_template: Renders HTML templates.
request: Accesses incoming request data.
jsonify: Converts Python objects into JSON format for HTTP responses.
redirect, url_for: Handles URL redirection.
create_access_token, jwt_required, get_jwt_identity: Functions for JWT-based authentication.
db, User, Car: Objects from the models.py file representing the database and its tables.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
