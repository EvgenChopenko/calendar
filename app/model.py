"""
связь с БД функции по обмену данными с СУБД
основный команды SQL
"""

import os.path as Path
import sqlite3
#_____________________________________________________________________________________________________
SQL_SELECT_ALL = """ SELECT id, data_create, start_data, end_data,STATUS, text  FROM calendar"""

SQL_SELECT_ONETASK="""SELECT id, data_create, start_data, end_data,STATUS, text  FROM calendar WHERE id =? """

SQL_SELECT_SATAUSFALSE="""SELECT id, data_create, start_data, end_data,STATUS, text  FROM calendar WHERE STATUS =1 """

SQL_SELECT_ID="""SELECT MAX(id) FROM calendar """
#----------------------------------------------------------------------------------------------------------------
SQL_INSERT_NEW = """INSERT INTO calendar (start_data, end_data,text) VALUES (?,?,?)"""
#----------------------------------------------------------------------------------------------------------------------
SQL_UPDATE_TEXT="""UPDATE calendar set text = ? WHERE id = ?"""

SQL_UPDATE_START_DATA="""UPDATE calendar set start_data = ? WHERE id = ?"""

SQL_UPDATE_END_DATA="""UPDATE calendar set end_data = ? WHERE id = ?"""

SQL_UPDATE_STATUS="""UPDATE calendar set STATUS = ? WHERE id = ?"""
#---------------------------------------------------------------------
#________________________________________________________
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#_______________________________________________________________________________________________________________
def connect(db_name=None):
    if db_name is None:
        db_name=':memory:'
    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    return conn

def initialize(conn,creation_shema):
    with conn,open(creation_shema) as f:
        conn.executescript(f.read())
#_________________________________________________________________________________________________________________
def add_task(conn,start_data,end_data,text):
    with conn:
        cursor = conn.execute(SQL_INSERT_NEW,(start_data,end_data,text,))
#__________________________________________________________________________________________________________________
def find_all(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
    return cursor.fetchall()

def find_one(conn,id):
    with conn:
        cursor = conn.execute(SQL_SELECT_ONETASK,(id,))
    return cursor.fetchall()

def find_statusfalse(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_SATAUSFALSE)
    return cursor.fetchall()
def find_lastid(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ID)
    return cursor.fetchone()
#____________________________________________________________________________________________________________________
def update(conn):
    def update_text(values,id):
        with conn:
            cursor = conn.execute(SQL_UPDATE_TEXT,(values,id))
    def update_start_date(values,id):
        with conn:
            cursor = conn.execute(SQL_UPDATE_START_DATA,(values, id))
    def update_end_date(values,id):
        with conn:
            cursor = conn.execute(SQL_UPDATE_END_DATA,(values, id))
    return update_text, update_start_date,update_end_date



def status(conn):
    def status_on(id):
        with conn:
            cursor = conn.execute(SQL_UPDATE_STATUS,(0, id,))
    def status_off(id):
        with conn:
            cursor = conn.execute(SQL_UPDATE_STATUS,(1, id,))
    return status_on, status_off






