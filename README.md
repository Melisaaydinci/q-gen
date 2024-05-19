# Flask PostgreSQL Demo

This is a simple demo that explains how to connect to PostgreSQL using the psycopg2 library and display the data using Flask.

## Prerequisites

Before running the demo, make sure you have the following installed:

- Python 3
- psycopg2 library (`pip install psycopg2`)
- Flask (`pip install flask`)
- PostgreSQL installed and running on your machine

## Connecting to PostgreSQL

To connect to PostgreSQL using psycopg2, you need to follow these steps:

1. Import the psycopg2 library in your Python script.
2. Establish a connection to your PostgreSQL database using the `connect()` function, providing the database connection parameters such as host, port, username, password, and database name.
3. Create a cursor object using the `cursor()` method on the connection object.
4. Execute SQL queries using the cursor object's `execute()` method.
5. Commit the transaction if necessary using the connection object's `commit()` method.
6. Close the cursor and connection objects using the `close()` method.

## Displaying Data with Flask

Once you have connected to PostgreSQL and retrieved the data, you can display it using Flask. Follow these steps:

1. Import the Flask library in your Python script.
2. Define routes for your Flask application to handle different URLs.
3. Within each route, render HTML templates and pass the data retrieved from PostgreSQL as context variables.
4. Run the Flask application using the `run()` method.

## Running the Demo

To run the demo:

1. Clone the repository:

```bash
git clone https://github.com/Melisaaydinci/q-gen.git
