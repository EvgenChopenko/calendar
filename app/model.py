import os.path as Path
import sqlite3
#_____________________________________________________________________________________________________
SQL_SELECT_ALL = """ SELECT id, data_create, start_data, end_data,STATUS, text  FROM calendar"""

SQL_INSERT_NEW = """INSERT calendar (start_data, end_data, STATUS,  text) VALUES (?,?,?,?)
"""

SQL_UPDATE_TEXT="""
UPDATE calendar set text = ? WHERE id = ?
"""

SQL_UPDATE_START_DATA="""
UPDATE calendar set start_data = ? WHERE id = ?
"""
SQL_UPDATE_END_DATA="""
UPDATE calendar set end_data = ? WHERE id = ?
"""

SQL_UPDATE_STATUS="""
UPDATE calendar set STATUS = ? WHERE id = ?
"""

#_______________________________________________________________________________________________________________
def connect(db_name=None):
    if db_name is None:
        db_name=':memory:'
    conn = sqlite3.connect(db_name)
   # магия по пятницам
    return conn

def initialize(conn,creation_shema):
    with conn,open(creation_shema) as f:
        conn.executescript(f.read())
#_________________________________________________________________________________________________________________
def add_task(conn,start_data,end_data,text):
    pass
def find_all(conn):
    pass

def update(conn):
    def update_text(values):
        pass
    def update_start_date(values):
        pass
    def update_end_date(values):
        pass
    return update_text, update_start_date,update_end_date

"""
or попробывать так или как выше 
UPDATE calendar set ? = ? WHERE id = ? 
def update(parametr,values,id):

"""

def status(conn):
    def status_on():
        pass
    def status_off():
        pass
    return status_on, status_off






