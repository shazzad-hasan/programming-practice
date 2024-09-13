import sqlite3
from app import Employee

# Connect to database
conn = sqlite3.connect("employee.db")

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE employee (
          first_name text,
          last_name text,
          age integer,
          salary integer
    )""")

c.execute("INSERT INTO employee VALUES ('Jon', 'Snow', 26, 4000)")

print("Command executed successfully.")

# Commit
conn.commit()
# Close conection
conn.close()