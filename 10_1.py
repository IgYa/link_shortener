# Задание 1
# Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом,
# чтобы у него была основная часть, которая отвечала бы за логику работы и предоставляла обобщённый интерфейс,
# и модуль представления, который отвечал бы за взаимодействие с пользователем.
#
# При замене последнего на другой, взаимодействующий с пользователем иным способом,
# программа должна продолжать корректно работать.

from tkinter import *
from short_url import get_short, get_url

#  до конца не разобрался как передать параметры в функцию при нажатии кнопки и получить результат функции обратно,
#  поэтому пока сделал две доп функции, вызывающие функции модуля short_url

def get_short2():   # вызывает функцию-генератор короткой ссылки и сохранении ее в базе данных на диске
    li = link.get()
    ln = link_name.get()
    ls = get_short(li, ln)
    link_short.insert(0, ls)

def get_url2():    # вызывает функцию поиска ссылок в базе данных
    name = link_name2.get()
    l2, ls2 = get_url(name)
    link2.insert(0, l2)
    link_short2.insert(0, ls2)

root = Tk()  # Создаем главный объект (окно приложения)

# Настройки главного окна
root.title('Укорачиваем ссылки!')  # Указываем название окна
root.geometry('400x420')  # Указываем размеры окна

Label(root, text='Введите ссылку').pack()
link = Entry(root, width=60)
link.pack()

Label(root, text='Для пополнения Базы Данных ссылок, \nвведите наименование ссылки').pack()
link_name = Entry(root, width=60)
link_name.pack()

Label(root, text='------------------------').pack()
# Создаем кнопку и при нажатии будет срабатывать метод "get_short2"
Button(root, text='Укоротить ссылку', command=get_short2).pack()
Label(root, text='------------------------').pack()

Label(root, text='Короткая ссылка').pack()
link_short = Entry(root, width=40)
link_short.pack()

Label(root, text='===========================================').pack()
#  например, Python: exclusions
Label(root, text='Для получения ссылки из Базы Данных, \nвведите наименование ссылки').pack()
link_name2 = Entry(root, width=60)
link_name2.pack()

Label(root, text='------------------------').pack()
# Создаем кнопку и при нажатии будет срабатывать метод "get_url2"
Button(root, text='Получить ссылку', command=get_url2).pack()

Label(root, text='Прямая ссылка на сайт').pack()
link2 = Entry(root, width=60)
link2.pack()

Label(root, text='Короткая ссылка').pack()
link_short2 = Entry(root, width=40)
link_short2.pack()

root.mainloop()
