import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1) 
import math

class HammingEncoder:
    def __init__(self, dataBits):
        self.dataBits = dataBits
        self.controlBits = self._calculate_control_bits(dataBits)
    
    def encode(self, input_str):
        totalBits = self.dataBits + self.controlBits

        codedBits = ['' for _ in range(totalBits)]
        
        dataIndex = 0
        for i in range(1, totalBits + 1):
            if not math.log2(i).is_integer():
                codedBits[i-1] = input_str[dataIndex]
                dataIndex += 1
        
        for i in range(self.controlBits):
            index = (2 ** i) - 1
            codedBits[index] = self._calculate_parity_bit(codedBits, i)
        
        return ''.join(codedBits)
    
    def decode(self, encoded_str):
        erorrBit = 0
        for i in range(self.controlBits):
            expected_parity = self._calculate_parity_bit(encoded_str, i)
            if expected_parity == '1':
                erorrBit += 2 ** i      
        return erorrBit if erorrBit <= len(encoded_str) else 0
    
    def _calculate_control_bits(self, dataBits):
        m = dataBits
        r = 1
        while 2**r < m + r + 1:
            r += 1
        return r

    def _calculate_parity_bit(self, bits, controlBitPos):
        parity = 0
        for bitPos in range(1, len(bits) + 1):
            if bitPos & (2**controlBitPos) and bits[bitPos-1] == '1':
                parity ^= 1
        return str(parity)

encoder = HammingEncoder(4)

original_str = "1011"
print(f"Исходная строка: {original_str}")

encoded_str = encoder.encode(original_str)
print(f"Закодированная строка: {encoded_str}")

error_str = list(encoded_str)
error_bit_position = 2 
error_str[error_bit_position] = '1' if error_str[error_bit_position] == '0' else '0'
error_str = "".join(error_str)
print(f"Закодированная строка с ошибкой: {error_str}")

error_position = encoder.decode(error_str)
if error_position:
    print(f"Обнаружена ошибка в бите: {error_position}")
else:
    print("Ошибок не обнаружено")
