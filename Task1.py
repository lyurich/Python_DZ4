# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

from random import randint
count1 = int(input('Введите количество чисел в первом наборе чисел: '))
count2 = int(input('Введите количество чисел во втором наборе чисел: '))

my_list1 = []
my_list2 = []

for _ in range(count1):
    my_list1.append(randint(0, 9))
print(my_list1)

for _ in range(count2):
    my_list2.append(randint(0, 9))
print(my_list2)

# print(set(my_list1))
# print(set(my_list2))


my_list3 = []
for i in (my_list1):
    for j in (my_list2):
        if i == j:
            my_list3.append(i)
# print(set(my_list3))

res = sorted(set(my_list3))
print(res)
