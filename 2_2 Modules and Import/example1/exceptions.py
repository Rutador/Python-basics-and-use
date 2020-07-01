class BadName(Exception):
    def __str__(self):
        return 'Incorrect name'


def greet(name):
    if name[0].isupper():
        print('Hello, ', name)
    else:
        raise BadName

print('exceptions successfully imported')
