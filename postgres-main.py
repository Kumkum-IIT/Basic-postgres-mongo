import psycopg2

conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='kumkumsnakescript',
    host='localhost',
    port='5432'
)

cur = conn.cursor()

# CREATE A LIST FROM TOP TO BOTTOM, THE LIST SHOULD REPRESENT HOW GOOD OR WORST A DEVELOPER IS:

cur.execute("CREATE TABLE IF NOT EXISTS developers (id SERIAL PRIMARY KEY, name VARCHAR(50), level VARCHAR(50))")
conn.commit()

cur.execute("INSERT INTO developers (name, level) VALUES ('John', 'Good')")
conn.commit()

cur.execute("INSERT INTO developers (name, level) VALUES ('Jane', 'Better')")
conn.commit()

cur.execute("INSERT INTO developers (name, level) VALUES ('Jagz', 'Best')")
conn.commit()

cur.execute("INSERT INTO developers (name, level) VALUES ('Doe', 'Worst')")
conn.commit()

cur.execute("Delete from developers where name = 'Doe' and level = 'Best'")
conn.commit()

cur.execute("SELECT * FROM developers")
print(cur.fetchall())

cur.close()
conn.close()

