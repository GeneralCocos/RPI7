import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1) 

class Worker:
    'doc class Worker'
    count = 0

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        Worker.count += 1

    def display(self):
        print("Worker:")
        print("{} {}".format(self.name,self.surname))

w1 = Worker("Ivan", "Ivanov")
print("w1.count: ", w1.count)
w2 = Worker("Alexei", "Petrov")
print("w2.count: ", w2.count)
print("w1.count: ", w1.count)
print("Worker.count: {0} \n".format(Worker.count))
print("Worker.__name__: ", Worker.__name__)
print("Worker.__dict__: ", Worker.__dict__)
print("Worker.__doc__: ", Worker.__doc__)
print("Worker.__bases__: ", Worker.__bases__)

# Задание 7 и 9
'''Измените название атрибута id на count. Модифицируйте программу так, чтобы определив атрибут id, он являлся уникальным для каждого объекта,
изменяясь на единицу с увеличением количества объектов класса'''

class Animal:
    'doc class Animal'
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.count += 1
        self.id = Animal.count

    def display(self):
        print("Animal count: {}".format(self.id))
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))


animal1 = Animal("Кот белый", 1)
animal2 = Animal("Кот серый", 2)
animal3 = Animal("Кот черный", 3)

animal1.display()
animal2.display()
animal3.display()

# Задание 8
'''
атрибут Animal.count увеличивается при создании каждого нового объекта класса, так же self.id = Animal.count
Поэтому id автоматически становится равен тому, какое это животное по счету
'''
