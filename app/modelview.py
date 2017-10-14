"""
активности для содержат функции для обмена между интерфесом и субд
"""
import os.path as Path
import sys

from app import model

from app import view
def list_fun():
    return  {
    '!m':action_show_menu,
    '1':action_find_all,
    '2':action_find_statusfalse,
    '3':action_add,
    '4':action_update,
    '5':action_status,
    '!q':action_exit
    }
#_____________________________________________________________
get_connection= lambda: model.connect('calendar.sqlite')

#____________________________________________________________
def action_find_all():
    with get_connection() as conn:
        rows= model.find_all(conn)
    view.output_find_all(rows)

def action_find_statusfalse():
    with get_connection() as conn:
        rows= model.find_statusfalse(conn)
    view.output_find_all(rows)
def action_find_id():
    with get_connection() as conn:
        rows= model.find_lastid(conn)
    return (rows.get('MAX(id)'))
#-----------------------------------------------------------------------

def action_add():
    start_data= view.input_start_data()
    end_data = view.input_end_data()
    text= view.input_text()
    with get_connection() as conn:
        task= model.add_task(conn, start_data, end_data, text)
    if not text:
        return
    return task

#-------------------------------------------------------------------------

def action_update ():
    parametr_tela= view.input_update_parametr()
    values = view.input_update_values(parametr_tela)

    id = view.input_id()

    if id:
        with get_connection() as conn:
            mode = model.update(conn)
            try:
                s=mode[parametr_tela](values=values,id=int(id))# защита нужна продумай !!
                view.output_find_all(model.find_one(conn=conn,id=id))
            except:
                view.error_print()
            finally:
                return 0

    else:
        action_show_menu()
        return

def action_status ():
    parametr_tela= view.input_status_parametr()
    id= view.input_id()
    if id:
        with get_connection() as conn:
            mode = model.status(conn)# защиат нужна подумай!!!
            try:
                s=mode[parametr_tela](id)
                view.output_find_all(model.find_one(conn=conn, id=id))
            except:
                view.error_print()
            finally:
                return 0


    else:
        action_show_menu()
        return

def action_show_menu():
    view.output (""" 
    Ежедневник! выбирити задачу:
    1. Вывесте список задач
    2. Вывести список не завершенных задач
    3. Добавить Задачу
    4. Отредеактировать задачу
    5. Изменить статус задачи
    !q. Выход   
    !m. Меню
    """)

def action_exit():
    sys.exit(0)
#________________________________________________________________________________________________

def creat_shema():
    creation_schema = Path.join(
        Path.dirname(__file__), 'bd.sql')
    with get_connection() as conn:
        model.initialize(conn, creation_schema)

