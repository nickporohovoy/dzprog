# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# s = "a a a b c a a d c d d" .split()
# print(s)
# my_dict = {n: s.count(n) for n in s}
# print (my_dict)

# s = "a a a b c a a d c d d" .split()
# print(s)
# my_dict = {}
# print (my_dict)
# for v in s:
#     if v not in my_dict:
#         print(v, end = " ")
#         my_dict[v] = 1
#     else:
#         print(f"{v}_{my_dict[v]}", end = " ")
#         my_dict[v] += 1
#     my_dict[v] = my_dict.get(v, 0) +1

# stroka = 'a a b c'.split()
# result = {}
# for i in stroka:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#         result[i] += 1
#     else:
#         print(i, end=' ')
#         result[i] = 1




# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

from random import randint
set1 = set(randint(1, 51) for i in range(int(input("VVedite kol-vo 1: "))))
print(set1)
set2 = set(randint(1, 51) for i in range(int(input("VVedite kol-vo 2: "))))
print(set2)
set3 = sorted(set1.intersection(set2))
print(*set3)



# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9

n = int(input("vvedite chislo :"))
sp = list()
for i in range(n):
    a = int(input("vvedite kol-vo zgod :"))
    sp.append(a)

sp2 = list()
for i in range(len(sp)):
    sp.append(sp[i] + sp[i-1] + sp[i-2])
print(max(sp2))







