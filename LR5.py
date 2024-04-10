import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1) 
'''
13. Создайте файл lab_04 05.py. Создайте класс Person, определив для него в конструкторе атрибуты firstname, lastname и age,
а также метод display(),выводящий информацию об объекте класса на экран. Создайте класс Student, унаследованный от Person,
определив для него дополнительные атрибуты student ID, являющийся уникальным номером для каждого объекта класса, и record Book,
содержащий информацию о количестве пятерок, четверок, троек и двоек студента в виде списка. В классе Student дополните метод display()
вводом значений атрибутов student ID и record Book на экран. Создайте три объекта класса Student для проверки работы методов
и выведите информацию о них на экран.
'''



class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def display(self):
        print(f"Имя: {self.firstname}")
        print(f"Фамилия: {self.lastname}")
        print(f"Возраст: {self.age}")


class Student(Person):
    def __init__(self, firstname, lastname, age, student_id, record_book):
        super().__init__(firstname, lastname, age)
        self.student_id = student_id
        self.record_book = record_book

    def display(self):
        super().display()
        print(f"ID студента: {self.student_id}")
        print("Оценки:")
        print(f"Пятерки: {self.record_book[0]}")
        print(f"Четверки: {self.record_book[1]}")
        print(f"Тройки: {self.record_book[2]}")
        print(f"Двойки: {self.record_book[3]}")


# Создание объектов класса Student
student1 = Student("Карина", "Шарафутдинова", 20, "1", [5, 4, 3, 2])
student2 = Student("Мария", "Бянкина", 22, "2", [4, 4, 4, 3])
student3 = Student("Андрей", "Петров", 21, "3", [5, 5, 5, 5])

# Вывод информации о студентах на экран
print("Информация о студенте 1:")
student1.display()
print("\nИнформация о студенте 2:")
student2.display()
print("\nИнформация о студенте 3:")
student3.display()
print(" ")
class Professor(Person):
    def __init__(self, firstname, lastname, age, professor_id, degree):
        super().__init__(firstname, lastname, age)
        self.professor_id = professor_id
        self.degree = degree
    
    def display(self):
        super().display()
        print("ID профессора:", self.professor_id)
        print("Научная степень:", self.degree)


# Создаем объекты класса Professor для проверки работы методов
professor1 = Professor("Оксана", "Панченко", 45, "1", "Доктор наук")
professor2 = Professor("Ольга", "Владимировна", 50, "2", "Кандидат наук")
professor3 = Professor("Марья", "Ивановна", 55, "3", "Профессор")

# Выводим информацию о профессорах на экран
print("Информация о профессоре 1:")
professor1.display()
print("\nИнформация о профессоре 2:")
professor2.display()
print("\nИнформация о профессоре 3:")
professor3.display()
