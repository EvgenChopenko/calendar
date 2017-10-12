# файл содержит промежуточные объект  необходимые для получения данных из модели

from app import modelview


def view():
    modelview.creat_shema()
    modelview.action_show_menu()

    list_funs =modelview.list_fun()
    while True:
        s=input(" Выберете значение ")
        fun=(list_funs.get(s))

        if fun:
            fun()
        else:
            print('неизвестная команда')




def output_update_parametr():
    return """
    0. Изменить текст
    1. Изменить дату начала
    2. Изменить дату окончания
    """
def output_status_parametr():
    return """
    0. решен
    1. не решен 
    """


def input_status_parametr():
    output_status_parametr()
    pram = input('Выберете действие')
    return pram


def input_start_data():
    pram = input('Введите дату начала события')
    return pram


def input_end_data():
    pram= input('Введите дату завершения события')
    return pram


def input_text():
    pram= input("Введите текс на Заметку*")
    return pram


def input_update_parametr():
    print(output_update_parametr())
    pram = input('Выберете параметр:')
    return pram


def input_update_values():
    pram=input("Введите значение:")
    return pram


# def input_status_values():
#     output_status_parametr()
#     return None

def output(param):
    print(param)