# Одним из самых часто используемых классов в Python является класс filter. Он принимает в конструкторе
# два аргумента a и f – последовательность и функцию, и позволяет проитерироваться только по таким
# элементам x из последовательности a, что f(x) равно True. Будем говорить, что в этом случае функция f
# допускает элемент x, а элемент x является допущенным.
#
# В данной задаче мы просим вас реализовать класс multifilter, который будет выполнять ту же функцию,
# что и стандартный класс filter, но будет использовать не одну функцию, а несколько.
#
# Решение о допуске элемента будет приниматься на основании того, сколько функций допускают этот элемент,
# и сколько не допускают. Обозначим эти количества за pos и neg.
#
# Введем понятие решающей функции – это функция, которая принимает два аргумента – количества pos и neg,
# и возвращает True, если элемент допущен, и False иначе.


class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos > 0

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterator = iter(iterable)
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        return self

    def __next__(self):
        while (True):
            elem = next(self.iterator)
            pos, neg = 0, 0
            for func in self.funcs:
                if func(elem):
                    pos += 1
                else:
                    neg += 1

            if self.judge(pos, neg):
                return elem
