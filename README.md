# Techin510-Lab5_HW
Streamlit App with PostgreSQL Database Integration
This Streamlit app visualizes event data using Altair charts. Instead of reading data from CSV files, it retrieves data directly from a PostgreSQL database.

Prerequisites
Install the required Python packages:
pip install streamlit pandas altair psycopg2

Set up your PostgreSQL database and create a table to store event data.
Usage
Clone this repository:
git clone https://github.com/yourusername/your-repo.git
cd your-repo

Update the database connection details in your Streamlit app (app.py):
Python

import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host='your-host',
    port='your-port',
    database='your-database',
    user='your-username',
    password='your-password'
)
AI-generated code. Review and use carefully. More info on FAQ.
Run the Streamlit app:
streamlit run app.py

Use the dropdown, date range selector, and location filter to explore event data.
Additional Notes
Make sure your PostgreSQL server is running and accessible.
Customize the SQL queries in your app to retrieve the relevant data from your database tables.