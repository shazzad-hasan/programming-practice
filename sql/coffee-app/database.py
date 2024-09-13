import sqlite3 

CREATE_BEANS_TABLE = "CREATE TABLE beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);"
INSERT_BEAN = "INSERT INTO beans (name, method, rating) VALUES (?,?,?);"
GET_ALL_BEANS = "SELECT * FROM beans;"
GET_BEANS_BY_NAME = "SELECT * FROM beans WHERE name = ?;"
GET_BEST_PREPARATION_FOR_BEAN = """
SELECT * FROM beans
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""

UPDATE_BEAN = "UPDATE beans SET name = ?, method = ?, rating = ? WHERE id = ?;"
DELETE_BEAN = "DELETE FROM beans WHERE id = ?;"


# Create the database
def connect():
    return sqlite3.connect("data.db")

# Create table
def create_tables(connection):
    with connection:
        connection.execute(CREATE_BEANS_TABLE)

def add_bean(connection, name, method, rating):
    with connection:
        connection.execute(INSERT_BEAN, (name, method, rating))

def get_all_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS).fetchall()

def get_beans_by_name(connection, name):
    with connection:
        return connection.execute(GET_BEANS_BY_NAME, (name,)).fetchall()

def get_best_preparation_for_bean(connection, name):
    with connection:
        return connection.execute(GET_BEST_PREPARATION_FOR_BEAN, (name,)).fetchone()
    
def update_bean(connection, bean_id, new_name, new_method, new_rating):
    with connection:
        return connection.execute(UPDATE_BEAN, (new_name, new_method, new_rating, bean_id))

def delete_bean(connection, bean_id):
    with connection:
        return connection.execute(DELETE_BEAN, (bean_id,))