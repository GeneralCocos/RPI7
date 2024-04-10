import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1) # Это на всякий случай, чтобы питон не ругался на русские буквы

import time
# Создаем класс
class Ticket:
    # метод класса инициализация. Принимает три аргумента
    def __init__(self, date, name,deadline):
        self.createDate = date # дата
        self.owner = name # имя
        self.deadline = deadline # дедлайн

    # Метод __del__() - это деструктор класса Ticket. Он вызывается, когда объект класса уничтожается.
    def __del__(self):
        print("Delete ticket:",time.asctime(self.createDate)) # сообщение об удалении с датой ссоздания

    # display - метод для вывода инфы
    def display(self):
        print("Ticket:")
        print(" createDate:",time.asctime(self.createDate))
        print(" owner: ",self.owner)
        print(" deadline:",time.asctime(self.deadline))

# создание объекта класа
ticket1 = Ticket(time.localtime(),"Ivan Ivanov", time.strptime("17.12.2017", "%d.%m.%Y"))

# вызов метода
ticket1.display()

# получение значения атрибута
print("Owner: ", ticket1.owner)
print("Owner(getattr): ", getattr(ticket1,"owner"))

# проверка наличия атрибута
print("hasattr: ", hasattr(ticket1,"owner"))
setattr(ticket1,"owner","Alexei Petrov") # установка значение атрибута
print("Owner(setattr): ", ticket1.owner)

# Задание 2
delattr(ticket1,"owner") # удаление значения атрибута
# Старый вариант:
# print("delattr: ", ticket1.owner)
# Возника ошибка AttributeError потому что мы пытались обратиться к атрибуту который больше не существует
# Исправленный вариант:
print("delattr:  ticket1.owner")
# Или же можно с поомощью if сначала сделать проверку на существование атрибута, прежде обращаться к неиу

# Задание 3
del ticket1 # удаление объекта
# Старый вариант:
# print(ticket1)
# Возника ошибка NameError потому что мы пытались обратиться к объекту который больше не существует

# Задание 4
# Выводим время компа в определенном формате
print(time.strftime("%d %b %Y %H:%M:%S", time.localtime()))

# Задание 5
# Создаем объект по строке
time_string = "17.07.2017 10:53:00"
time_object = time.strptime(time_string, "%d.%m.%Y %H:%M:%S")

print(time_object)