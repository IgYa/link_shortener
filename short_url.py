# Задание 1
# Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом,
# чтобы у него была основная часть, которая отвечала бы за логику работы и предоставляла обобщённый интерфейс,
# и модуль представления, который отвечал бы за взаимодействие с пользователем.
#
# При замене последнего на другой, взаимодействующий с пользователем иным способом,
# программа должна продолжать корректно работать.

import pyshorteners
import json

def get_short(li, ln):
    ls = pyshorteners.Shortener().tinyurl.short(li)

# чтение и сохранение в json c добавлением новых данных
    with open('url.json') as file:
        db = json.load(file)

    db.append({'link': li, 'link_name': ln, 'link_short': ls})

    with open('url.json', 'w') as file:
        json.dump(db, file, indent=3)

    return ls

def get_url(name):
    with open('url.json') as file:
        db = json.load(file)

    for d in db:
        if d['link_name'] == name:
            return d['link'], d['link_short']

