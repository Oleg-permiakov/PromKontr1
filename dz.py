import csv

def interface():
    with open("noutis.csv", 'a', encoding="utf-8"): 
        pass            
    var = 0
    while var != "6":
        print(
            "Возможные варианты:\n"
            "1. Создать/Добавить заметку\n"
            "2. Вывести на экран \n"
            "3. Поиск заметки\n"
            "4. Редактировать заметку\n"
            "5. Удалить заметку\n"
            "6. Выход"
             )  
        print()
        var = input("Выберите вариант действия: ")
        while var not in ("1", "2", "3", "4", "5", "6"):
            print("Не корректный ввод")
            var = input("Выберите вариант действия: ")
        print()

        if var == "1":
            add_nout()
        if var == "2":
            print_nouts()
        if var == "3":
            search_nout()
        if var == "4":
            edit_nout()
        if var == "5":
            del_nout()
        if var == "6":
            print("До свидание")
    print()    


def input_id_nout():
    return input("Введите Id заметки: ").title() 

def input_name_nout():
    return input("Введите заголовок заметки: ").title()

def input_body_nout():
    return input("Введите содержание заметки: ").title()

def input_data_time():
    return input("Введите время создания заметки: ").title()

def read_file():
    with open('noutis.csv', 'r', encoding='utf-8') as file:
        return file.read()



def create_nout():
    id_nout = input_id_nout()
    name_nout = input_name_nout()
    body_nout = input_body_nout()
    data_time = input_data_time()
    list_1 = []
    list_1.append(id_nout + ';' + name_nout + ';' + body_nout + ';' + data_time)
    return list_1



def add_nout(): 
    nout = create_nout()
    with open("noutis.csv", 'a', newline='') as file: 
        writer = csv.writer(file)
        writer.writerow(nout)

def print_nouts(): 
    with open("noutis.csv", 'r', encoding="utf-8") as file:
        nout_sstr = file.read()
        nout_list = nout_sstr.rstrip().split("\n")
        for nout in enumerate(nout_list, 1): 
            print(*nout)

 
def search_nout():
    print(
            "Возможные варианты поиска заметки:\n"
            "1. Id заметки\n"
            "2. Заголовок\n"
            "3. Содержание\n"
            "4. Дата создания\n"
            ) 
    var = input("Выберите вариант поиска: ")
    while var not in ("1", "2", "3", "4"):
        print("Не корректный ввод")
        var = input("Выберите вариант поиска: ")
    i_var = int(var) - 1
    search_n = input("Введите данные для поиска: ").title()
    with open("noutis.csv", 'r', encoding="utf-8") as file:
        nout_sstr = file.read()
        nout_list = nout_sstr.rstrip().split("\n")
        for i in nout_list:
            lst_nout = i.split(";")
            for j in lst_nout: 
                if search_n in lst_nout[i_var]:
                    print(i)
                    break
              
def edit_nout():
    print('Введите полную запись заметки, которую хотите изменить.')
    nout = create_nout()
    note = nout[0]
    data = read_file()
    new_nout_list = data.rstrip().split("\n")
    with open('noutis.csv', 'w'):
        pass
    for i in new_nout_list:
        if note in i:
            print("Введите новую запись: ")
            new_nout1 = create_nout()
            new_nout = new_nout1[0]
            new_nout_list = [new_nout if x == note else x for x in new_nout_list]
    for j in new_nout_list:
        redj_list = [j]
        with open('noutis.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(redj_list)
       
        
def del_nout():
    print('Введите полную запись заметки, которую хотите удалить.')
    nout = create_nout()
    note = nout[0]
    data = read_file()
    new_nout_list = data.rstrip().split("\n")
    with open('noutis.csv', 'w'):
        pass
    for i in new_nout_list:
        if note in i:
            new_nout_list.remove(note)
    for j in new_nout_list:
        redj_list = [j]
        with open('noutis.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(redj_list)





 
    