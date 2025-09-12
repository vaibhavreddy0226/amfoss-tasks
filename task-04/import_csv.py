import csv
from db_utils import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()
with open("movies.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute("""
        INSERT INTO movies (Series_Title, Released_Year, Genre, IMDB_Rating, Director, Star1, Star2, Star3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row["Series_Title"],
            int(row["Released_Year"]) if row["Released_Year"].isdigit() else None,
            row["Genre"],
            float(row["IMDB_Rating"]) if row["IMDB_Rating"] else None,
            row["Director"],
            row["Star1"],
            row["Star2"],
            row["Star3"]
        ))
conn.commit()
conn.close()
