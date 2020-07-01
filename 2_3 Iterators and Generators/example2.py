# создается функция-генератор для итерации класса, который наследуется от int


class MyInt(int):
    def __iter__(self):
        return my_gen()


def my_gen():
    print('case 1')
    yield a
    print('case 2')
    yield a
    print('case 3')
    yield a
    print('case 4')
    yield a
    print('case 5')
    yield a
    print('case 6')


a = MyInt(13)
iterator = iter(a)
print(iterator)

for i in a:
    print(i)
