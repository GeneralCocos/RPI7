import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1) 
import heapq
from collections import Counter
import math

class Encoder:
    def encode(self, text):
        pass
    
    def decode(self, encoded_text):
        pass

class HuffmanEncoder(Encoder):
    def __init__(self):
        super().__init__()
        self.compression_coef = None
        self.huffman_dict = {}  # Словарь кодирования Хаффмана
    
    def encode(self, text):
        # Подсчет частот символов в тексте
        freq = Counter(text)
        # Построение кучи из списка символов и их частот
        heap = [[weight, [char, ""]] for char, weight in freq.items()]
        heapq.heapify(heap)
        # Построение дерева Хаффмана
        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        # Формирование словаря кодирования Хаффмана
        codes = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
        self.huffman_dict = {char: code for char, code in codes}
        # Кодирование текста с использованием Хаффмана
        encoded_text = ''.join(self.huffman_dict[char] for char in text)
        # Рассчет коэффициента сжатия
        self.setCompressionCoef(text)
        return encoded_text
    
    def decode(self, encoded_text):
        decoded_text = ''
        current_code = ''
        # Декодирование текста с использованием словаря кодирования Хаффмана
        for bit in encoded_text:
            current_code += bit
            for char, code in self.huffman_dict.items():
                if code == current_code:
                    decoded_text += char
                    current_code = ''
                    break
        return decoded_text
    
    def setCompressionCoef(self, text):
        # Вычисление общего количества символов в тексте
        total_chars = len(text)
        # Вычисление длины закодированного текста с использованием Хаффмана
        huffman_encoded_length = sum(len(self.huffman_dict[char]) for char in text)
        #  кодирование ASCII
        original_length = total_chars * 8
        #  коэффициент сжатия
        self.compression_coef = original_length / huffman_encoded_length
    
    def getCompressionCoef(self):
        return self.compression_coef
    
    def lz77_encode(self, text, window_size=1024):
        encoded_text = []
        window = ""
        i = 0
        # Проход по тексту и кодирование Лемпеля-Зива
        while i < len(text):
            length = 0
            offset = 0
            # Поиск наилучшей подстроки в окне
            while i - offset >= 0 and length < window_size:
                substring = text[i:i + length + 1]
                if substring in window:
                    offset = window.rindex(substring)
                    length += 1
                else:
                    break
            # Доб закодированной инфы в список
            if length > 0:
                encoded_text.append((length, i - offset))
                window += text[i:i + length]
                i += length
            else:
                encoded_text.append((0, 0))
                window += text[i]
                i += 1
            if len(window) > window_size:
                window = window[-window_size:]
        return encoded_text


test_string = "Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991."

huffman_encoder = HuffmanEncoder()
encoded_text = huffman_encoder.encode(test_string)
decoded_text = huffman_encoder.decode(encoded_text)
compression_coef = huffman_encoder.getCompressionCoef()

print("Исходный текст:", test_string)
print("Закодированный текст с использованием Хаффмана:", encoded_text)
print("Раскодированный текст с использованием Хаффмана:", decoded_text)
print("Коэффициент сжатия методом Хаффмана:", compression_coef)

lz77_encoded_text = huffman_encoder.lz77_encode(test_string)
print("Закодированный текст методом Лемпеля-Зива:", lz77_encoded_text)





'''
12. Создайте файл lab_04_04.py. Создайте класс Encoder, определив для него методы encode () и decode () , аргументом которых является строка,
a выходными данными закодированная и декодированная строка соответственно. Создайте классы HuffmanEncoder и LZEncoder, унаследованные от класса Encoder,
определив для них атрибут compression Calf в конструкторах классов. Для созданных классов HuffmanEncoder и LZEncoder переопределите методы encode () и decode (),
реализующие кодирование и декодирование поданных в качестве аргументов строк, используя методы Хаффмана и Лемпеля-Зива соответственно. Определите приватный метод setCompressionCoef()
(с использованием двойного подчеркивания), осуществляющий расчет коэффициентов сжатия для методов Хаффмана и Лемпеля-Зива B соответствующих классах. Метод setCompressionCoef()
должен вызываться при работе внутри классa B метода encode (). Определите общедоступный метод get Compression Coef(), позволяющий получить значение коэффициента сжатия. Осуществите
проверку методов классов на следующей строке:

Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991.
'''