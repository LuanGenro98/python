from configuration import TransactionManager
from model import User

def createTable():
    TransactionManager.insert("CREATE TABLE IF NOT EXISTS uuser(\nid serial PRIMARY KEY,\nname VARCHAR ( 50 ) NOT NULL,\nemail VARCHAR ( 255 ) UNIQUE NOT NULL,\npassword VARCHAR ( 50 ) NOT NULL);")

def save(user: User):
    TransactionManager.insert(f"INSERT into uuser (name, email, password) values ('{user.name}', '{user.email}', '{user.password}');")

def findById(id: int):
    return TransactionManager.query(f"SELECT * FROM uuser WHERE id = {id};")

def update(user: User):
    TransactionManager.insert(f"UPDATE uuser SET name = '{user.name}', email = '{user.email}', password = '{user.password}' WHERE id = {user.id};")

def delete(id: int):
    TransactionManager.insert(f"DELETE FROM uuser WHERE id = {id};")

def findAll():
    return TransactionManager.query("SELECT * FROM uuser;")

def deleteAll():
    TransactionManager.insert("DELETE FROM uuser;")

def findByName(name):
    return TransactionManager.query(f"SELECT * FROM uuser WHERE name = '{name}';")

def findByEmail(email):
    return TransactionManager.query(f"SELECT * FROM uuser WHERE email = '{email}';")