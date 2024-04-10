import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1) 
class Row:
    def __init__(self, row_id, collection):
        self.id = row_id
        self.collection = collection
        self.value = self.calculate_value()

    def calculate_value(self):
        # Вычисление значения функции f(x1, x2)
        # В данном случае это простое логическое И (AND) двух переменных
        return self.collection[0] * self.collection[1]


class Table:
    def __init__(self):
        self.rows = []
        self.rows_num = 0

    def add_row(self, row):
        # Добавление строки в таблицу
        for existing_row in self.rows:
            if existing_row.id == row.id:
                raise ValueError("Строка с таким идентификатором уже существует")
        self.rows.append(row)
        self.rows_num += 1

    def set_row(self, row):
        # Изменение строки в таблице
        for existing_row in self.rows:
            if existing_row.id == row.id:
                existing_row.collection = row.collection
                existing_row.value = row.calculate_value()
                return
        raise ValueError("Строки с таким идентификатором не существует")

    def get_row(self, row_id):
        # Получение строки по идентификатору
        for row in self.rows:
            if row.id == row_id:
                return row
        raise ValueError("Строки с таким идентификатором не существует")

    def display(self):
        # Вывод таблицы на экран
        print("id  x1  x2  f(x1,x2)")
        for row in self.rows:
            print(f"{row.id}   {row.collection[0]}   {row.collection[1]}   |   {row.value}")


class LogicFunction:
    def __init__(self, variables_num):
        self.variables_num = variables_num
        self.table = Table()

    def get_expression(self):
        # Вычисление и возвращение минимальной формулы логической функции
        # В данном случае это просто x1 AND x2
        return "f(x1, x2) = x1 * x2"

    def get_table(self):
        # Получение таблицы истинности логической функции
        return self.table

    def print_table(self):
        # Вывод таблицы на экран
        self.table.display()


# Пример использования классов
logic_function = LogicFunction(2)

# Добавление трех строк в таблицу
for i in range(1, 4):
    row_id = i
    x1 = int(input(f"Введите значение x1 для строки {i}: "))
    x2 = int(input(f"Введите значение x2 для строки {i}: "))
    collection = [x1, x2]
    row = Row(row_id, collection)
    logic_function.table.add_row(row)

# Вывод таблицы на экран
print("Таблица истинности:")
logic_function.print_table()

# Вывод минимальной формулы логической функции
print("Минимальная формула логической функции:", logic_function.get_expression())
