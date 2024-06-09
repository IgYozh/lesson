#Задача "Распаковка"
# 1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'str', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

# 2.Распаковка параметров:

values_list = ['Hello', 4.5, False]
values_dict = {"a": 9, "b": "Key", "c": True}

print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:

values_list_2 = (True, "Look")
print_params(*values_list_2, 42)
