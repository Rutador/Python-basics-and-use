# Создается класс-итератор для класса, который наследуется от int


class MyInt(int):
    def __iter__(self):
        return MyIntIterator(self)


class MyIntIterator:
    def __init__(self, value):
        self.int = value
        self.it = 0
        self.end_it = 5

    def __next__(self):
        if self.it < self.end_it:
            self.it += 1
            return self.int, self.it
        else:
            raise StopIteration


a = MyInt(13)
iterator = iter(a)
print(iterator)

for i in a:
    print(i)
