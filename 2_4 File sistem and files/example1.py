f = open('test.txt')
print(next(f))
x = f.readline()
print(x.splitlines())
x = f.read()
print(x)
f.close()

k = open('test.txt', 'a')
k.write('Hello\n')
k.close()

