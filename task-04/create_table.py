from db_utils import get_db_connection

conn = get_db_connection(db_name=None)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS movies_db")
conn.commit()
conn.close()

conn = get_db_connection()
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Series_Title VARCHAR(255),
    Released_Year INT,
    Genre VARCHAR(100),
    IMDB_Rating FLOAT,
    Director VARCHAR(255),
    Star1 VARCHAR(255),
    Star2 VARCHAR(255),
    Star3 VARCHAR(255)
)
""")
conn.commit()
conn.close()
