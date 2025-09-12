import mysql.connector

def get_db_connection(db_name="movies_db"):
    return mysql.connector.connect(
        host="localhost", user="vaibhav", password="vaibhav", database=db_name
    )
