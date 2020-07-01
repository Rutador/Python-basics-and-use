import exceptions
import fib

while True:
    try:
        exceptions.greet(input('Inter your name: '))
    except exceptions.BadName as e:
        print(e, ', try again', sep='')
    else:
        break

print(fib.fib(10))
