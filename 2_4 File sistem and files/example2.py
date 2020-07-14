import os
import os.path

print((os.getcwd()))  # путь до текущей директории
print(os.listdir('../temp'))  # список файлов и папок директории
os.chdir('task1')  # смена текущей директории
print((os.getcwd()))
os.chdir('../')

print(os.path.exists('test.txt'))  # проверка существования
print(os.path.exists('task1'))  #

print(os.path.isfile('test.txt'))  # проверка на файл
print(os.path.isdir('test.txt'))

print(os.path.abspath('test.txt'))  # абсолютный путь до файла

print(list(os.walk('.')))

os.system('dir')
