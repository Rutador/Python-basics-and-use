class BadName(Exception):
    def __str__(self):
        return 'incorrect name'


def greet(name):
    if name[0].isupper():
        print('Hello,', name)
    else:
        raise BadName


while True:
    try:
        input_name = input("Inter your name")
        greeting = greet(input_name)
    except BadName as e:
        print(e)
        print('Try again')
    else:
        break
