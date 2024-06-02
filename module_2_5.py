

def get_matrix(n, m, value):
    matrix = []
    for i in range(n): #
        new_matrix = []
        matrix.append(new_matrix)
        for j in range(m):
            matrix[i].append(value)

    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

print("Так может эта функция, Вы также можете ввести свои значения и убедиться!")
a = int(input("Введите количество строк: "))
b = int(input("Введите количество столбцов: "))
c = int(input("Введите значение ячейки: "))

result4 = get_matrix(a, b, c)
print(result4)