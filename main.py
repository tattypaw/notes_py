import json
import datetime

def help():
    print("Команды для управления заметками:","help - помощь", "begin - начало работы","end - конец работы","read - просмотр заметок","add - добавление записи","filtr - поиск дате","del - удаление записи","edit - редактирование записи","save - сохранение записи","exit - Выход",sep="\n")
    return

def load():
    with open("notes.json", 'r', encoding="utf-8") as fh:
        notes_data = json.load(fh)
        if len(notes_data)!=0 : print('Заметки были успешно загружены')
        else : print("Заметок нет, перейдите к добавлению заметки")
    return notes_data

def save():
    with open("notes.json", 'w', encoding="utf-8") as fh:
        fh.write(json.dumps(notes_data, ensure_ascii=False))
    print("Информация успешно сохранена в файле notes.json")

def view():
        i = 1
        for item in notes_data:
            note = item
            print(note['id'] +' ' + note['heading'], sep='\n')
            print(note['body'])
            print("последняя редакция: " + note['date'])
            print()
            i+=1
        return

def addEl():
        data={}
        if len(notes_data)!=0 : 
            data['id'] = str(len(notes_data) + 1)
        else :
            data['id'] = '1'
        print('id = ', data['id'])
        data['heading'] = input("Введите заголовок: ")
        data['body'] = input("Введите сообщение: ")
        data['date'] = str(datetime.date.today())
        notes_data.append(data)
        print("Заметка была успешно добавлена! ")
        return

def search(f):
        i = 0
        findArr = []
        choice = int(input("Уточните задание. Вам нужны записи: 1 - за указанную дату; 2 - до указанной даты; 3 - после указаннойдаты? Введите цифру 1, 2 или 3: "))
        if choice == 1:
            for item in notes_data:
                flag = False
                for    value in item.values() :
                    if f in value: flag = True
                if flag :
                    i += 1
                    findArr.append(item)
        elif choice == 2:
            f_date = datetime.datetime.strptime(f, '%Y-%m-%d').date()
            for item in notes_data:
                flag = False
                date = datetime.datetime.strptime(item['date'], '%Y-%m-%d').date()
                if date <= f_date: 
                    i += 1
                    findArr.append(item)
        elif choice == 3:
            f_date = datetime.datetime.strptime(f, '%Y-%m-%d').date()
            for item in notes_data:
                flag = False
                date = datetime.datetime.strptime(item['date'], '%Y-%m-%d').date()
                if date >= f_date: 
                    i += 1
                    findArr.append(item)
        else:
            print("Не могу выполнить запрос")
        print(f'Найдено вхождений: {i}')
        print()
        return findArr

def removeEl(f):
    i = 0
    for item in notes_data:
        flag = False
        for value in item.values() :
            if f in value: flag = True
        if flag :
            i += 1
            notes_data.remove(item)
    print()
    print(f'Найдено вхождений: {i}')
    return i 

def editEl(f):
    i = 0
    keys = ["id", "heading", "body", "date"]
    for item in notes_data:
        note = item
        if note['id'] == str(f):
            print(note)
            ask = input("Хотите изменить заголовок? (y/n): ")
            if ask.lower() == 'y':
                note['heading'] = input("Введите новое значение: ")
            print(note['heading'])
            ask = input("Хотите изменить сообщение? (y/n): ")
            if ask.lower() == 'y':
                note['body'] = input("Введите новое значение: ")
            note['date'] = str(datetime.date.today())
            notes_data.pop(i)
            notes_data.insert(i,note)
        i+=1
    print("Запись успешно отредактирована.")
    return

help()
notes_data = load()
while True:
    command = input("Введите команду: ")
    if command =="begin":
        print("Система готова к работе ")
    elif command=="end":
        save()
        print("Конец работы. Заходите ещё, будем рады! ")
        break
    elif command=="read":
        print('Текущий список заметок: ')
        view()
    elif command=="add":
        addEl()
    elif command=="help":
        help()
    elif command=="filtr":
        f = input("Введите дату в формате гггг-мм-дд: ")
        arrRes = []
        arrRes.append(search(f))
        for item in arrRes:
             print(item)
    elif command=="del":
        f = input("Какую запись надо удалить? Введите id записи: ")
        n = removeEl(f)
        print(f'количество удаленных записей: {n}')
    elif command=="edit":
        view()
        f = int(input("Введите id записи для редактирования: "))
        editEl(f)
    elif command=="save":
        save()
    elif command=="exit":
        print("Если не сохранить изменения, после выхода они будут отменены. Сохранить справочник? 1 - да; 2 - нет")
        i = input("Ваш выбор: ")
        if i == "1": 
            save()
        else:
            print("Изменения отменены.")
        print("До свидания! Сеанс окончен.")
        break
    else:
        print("Неопознанная команда. Просьба изучить мануал через help ")