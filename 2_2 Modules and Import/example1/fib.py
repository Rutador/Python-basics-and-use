print(__name__)


def fib(x):
    if x == 0 or x == 1:
        return x
    return fib(x - 2) + fib(x - 1)


if __name__ == '__main__':
    print(fib(33))
