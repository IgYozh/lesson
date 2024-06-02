#Через ручной ввод:

a = int(input("Введите значение для генерации пароля (от 3 до 20): "))
password = ''
print("Генерация пароля для числа: ", a)

for i in range(1, a):
    for j in range(i, a):
        if a>= 3 and a <=20 and a % (i + j) == 0:
            if str(j) == str(i):
                continue
            password = password + str(i) + str(j)

if a >= 3 and a <= 20:
    print("Ваш пароль: ", password)
else:
    print("Число не соответствует условию ввода!")



print("Далее через генерацию")

import random

a_2 = random.randint(3, 20)

n_password = ''
print("Генерация пароля для числа: ", a_2)
for i in range(1, a_2):
    for j in range(i, a_2):
        if a_2 % (i + j) == 0:
            if str(j) == str(i):
                continue
            n_password = n_password + str(i) + str(j)

print("Ваш пароль: ", n_password)