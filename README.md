<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Management Web App</title>
</head>
<body>
    <h1>Car Management Web App</h1>
    <p>This is a simple web application for managing cars. Users can register, log in, and add cars to their profile.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>User Authentication:</strong> Users can register and log in to the application securely.</li>
        <li><strong>Car Management:</strong> Logged-in users can add, view, and manage their cars.</li>
        <li><strong>JWT Authentication:</strong> JSON Web Tokens (JWT) are used for secure authentication.</li>
        <li><strong>MySQL Database:</strong> Data is stored in a MySQL database using SQLAlchemy.</li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li>Clone the repository:</li>
        <code>git clone https://github.com/your_username/car-management-app.git</code>
        <li>Install dependencies:</li>
        <code>pip install -r requirements.txt</code>
        <li>Set up the MySQL database:</li>
        <ul>
            <li>Create a MySQL database named <code>mycar</code>.</li>
            <li>Update the database connection URI in <code>app.py</code> with your MySQL configuration.</li>
        </ul>
        <li>Run the application:</li>
        <code>python app.py</code>
    </ol>

    <h2>Usage</h2>
    <ul>
        <li>Open your web browser and navigate to <code>http://localhost:5000</code> to access the application.</li>
        <li>Click on "Sign Up" to create a new account, or "Log In" if you already have an account.</li>
        <li>Once logged in, you can add and manage your cars from the dashboard.</li>
    </ul>

    <h2>Controllers</h2>
    <p>These are the necessary imports for the file.</p>
    <ul>
        <li>Blueprint: Used to define a group of related routes.</li>
        <li>render_template: Renders HTML templates.</li>
        <li>request: Accesses incoming request data.</li>
        <li>jsonify: Converts Python objects into JSON format for HTTP responses.</li>
        <li>redirect, url_for: Handles URL redirection.</li>
        <li>create_access_token, jwt_required, get_jwt_identity: Functions for JWT-based authentication.</li>
        <li>db, User, Car: Objects from the models.py file representing the database and its tables.</li>
    </ul>

    <h2>Contributing</h2>
    <p>Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.</p>

    <h2>License</h2>
    <p><a href="https://choosealicense.com/licenses/mit/">MIT License</a></p>
</body>
</html>
