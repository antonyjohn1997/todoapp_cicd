import sqlite3  
from flask import g  

DATABASE = 'todo.db'  

def get_db():  
    db = getattr(g, '_database', None)  
    if db is None:  
        db = g._database = sqlite3.connect(DATABASE)  
    return db  

def init_db():  
    with sqlite3.connect(DATABASE) as conn:  
        conn.execute('''  
            CREATE TABLE IF NOT EXISTS tasks (  
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                content TEXT NOT NULL  
            );  
        ''')  

