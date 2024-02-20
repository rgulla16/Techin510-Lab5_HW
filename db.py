import os

import psycopg2
from dotenv import load_dotenv


load_dotenv()
host = os.getenv('DB_HOST')
dbname = 'postgres'
user = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
sslmode = "require"

# Construct connection string
def get_db_conn():
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    print("Connection established")
    conn.autocommit = True
    return conn


