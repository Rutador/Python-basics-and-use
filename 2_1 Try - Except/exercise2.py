"""
Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
Также реализуйте новое исключение NonPositiveError.

В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить
неположительное целое число бросалось исключение NonPositiveError и число не добавлялось,
а при попытке добавить положительное целое число, число добавлялось бы как в стандартный list.

В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.
"""


class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError


class NonPositiveError(Exception):
    pass


xx = PositiveList([12, 4])
print(xx)
xx.append(32)
print(xx)

try:
    xx.append(-3)
except NonPositiveError as e:
    print(e)
    print('Non positive number')

print(xx)
