def create(added_namespace, parent):
    """ Добавляет пару 'родитель:неймспейс' в словарь parents
    """
    temp = []
    if parent in parents:                               # жуткие костыли чтобы строка записывалась в список как
        if type(parents.get(parent)) == type(temp):     # один элемент, а не в виде:
            temp.extend(parents.get(parent))            # temp.extend('variable')    # temp == ['v', 'a', 'r' ...]
        else:                                           #
            temp.append(parents.get(parent))            #
        temp.append(added_namespace)
        added_namespace = temp
    parents.update({parent: added_namespace})


def add_var(namespace, added_var):
    """ Добавляет пару 'неймспейс:переменная' в словарь variables
    """
    temp = []
    if namespace in variables:
        if type(variables.get(namespace)) == type(temp):
            temp.extend(variables.get(namespace))
        else:
            temp.append(variables.get(namespace))
        temp.append(added_var)
        added_var = temp
    variables.update({namespace: added_var})


def get_namespace(finding_namespace, finding_var):
    """ Возвращает неймспейс, соответствующий переменной
    """
    if (variables.get(finding_namespace) == finding_var) or (variables.get(finding_namespace) and (finding_var in variables.get(finding_namespace))):
        return finding_namespace
    if parents.get('None') == finding_namespace:
        return None
    for k in parents:
        if (parents.get(k) == finding_namespace) or (finding_namespace in parents.get(k)):
            return get_namespace(k, finding_var)


n = int(input())
parents = {'None': 'global'}
variables = {}

for i in range(n):
    input_string = [str(i) for i in input().split(' ')]
    if input_string[0] == 'create':
        create(input_string[1], input_string[2])
    if input_string[0] == 'add':
        add_var(input_string[1], input_string[2])
    if input_string[0] == 'get':
        print(get_namespace(input_string[1], input_string[2]))

#print(parents)
#print(variables)
