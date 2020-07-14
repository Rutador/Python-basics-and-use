# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
#
# Выведите одно число – количество вхождений строки t в строку s.
#
# Пример:
# s = "abababa"
# t = "aba"
#
# Вхождения строки t в строку s:
# abababa
# abababa
# abababa


s = input()
x = input()
n = 0
for i in range(len(s)):
    n += s.count(x, i, i + len(x))
print(n)
