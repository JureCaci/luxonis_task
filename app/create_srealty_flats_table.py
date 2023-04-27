import psycopg2

connection = psycopg2.connect(database="devdb",user="devuser",password="devpass",host="db",port="5432")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS sreality_flats")
cursor.execute("""
    CREATE TABLE sreality_flats(
        id SERIAL PRIMARY KEY,
        title TEXT,
        image_url TEXT
    )
""")
connection.commit()
cursor.close()
connection.close()
