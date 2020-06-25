"""
Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел
из этой последовательности, затем сумму второй пятерки, и т. д.

Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части.
Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.

Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок
последовательных элементов по мере их накопления.

Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему
действительно необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку,
для которой была выведена сумма.
"""


class Buffer:

    def __init__(self):
        self.list = []

    def add(self, *a):
        for i in a:
            self.list.append(i)
        n = len(self.list) // 5
        m = len(self.list) % 5
        for i in range(n):
            temp_sum = 0
            for j in range(5):
                k = j + i * 5
                temp_sum += self.list[k]
            print(temp_sum)
        temp = []
        for i in range(len(self.list) - m, len(self.list)):
            temp.append(self.list[i])
        self.list = temp

    def get_current_part(self):
        return self.list


buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part())  # вернуть [1, 2, 3]
buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part())  # вернуть [6]
buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part())  # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part())  # вернуть [1]
