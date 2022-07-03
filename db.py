import sqlite3

DATABASE_NAME = "database.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_table_readkey():
    tables = [
            """CREATE TABLE IF NOT EXISTS
                readkey_table(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    key TEXT NOT NULL)"""
        ]
    
    db = get_db()
    cursor = db.cursor()
    
    for table in tables:
        cursor.execute(table)

def create_table_writekey():
    tables = [
           """CREATE TABLE IF NOT EXISTS
                writekey_table(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    key TEXT NOT NULL)"""
        ]
    
    db = get_db()
    cursor = db.cursor()
    
    for table in tables:
        cursor.execute(table)
    
def create_table_adc():
    tables = [
           """CREATE TABLE IF NOT EXISTS
                adc_table(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    adc INTEGER NOT NULL)"""
        ]
    
    db = get_db()
    cursor = db.cursor()
    
    for table in tables:
        cursor.execute(table)