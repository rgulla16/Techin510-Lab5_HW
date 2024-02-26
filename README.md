# Techin510-Lab5_HW
Streamlit App with PostgreSQL Database Integration
This Streamlit app visualizes event data using Altair charts. Instead of reading data from CSV files, it retrieves data directly from a PostgreSQL database.

Prerequisites
pip install streamlit pandas altair psycopg2

Set up PostgreSQL database and create a table to store event data.
Usage
Clone this repository:

### Update the database connection details in your Streamlit app (app.py):
Python

import psycopg2

# Connect to the PostgreSQL database using the connection string
The connection data is present in Azure and i am using the below to make the connection. 
conn = psycopg2.connect(
    host='my-host',
    port='my-port',
    database='my-database',
    user='my-username',
    password='my-password'
)

## Run the Streamlit app:
streamlit run app.py

There are 4 drop downs for selecting the event data. The 'Event category', 'Location', 'Start Date' and 'End Date'
The default shows all the events in the database table 'events' in 4 bar graphs. 
Graph 1 - Events by Type
Graph 2 - Events by Month of Year
Graph 3 - Day of Month Week
Graph 4 - Events by Location

Use the dropdown, date range selector, and location filter to explore event data.

Additional Notes
Make sure PostgreSQL server is running and accessible.
