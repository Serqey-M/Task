from random import randint


def creating_list(min_len_list, max_len_list, min_num, max_num):
    len_list = randint(min_len_list, max_len_list)
    list = []
    for i in range(len_list):
        list.append(randint(min_num, max_num))
    return list


min_len_list = 10
max_len_list = 30
min_num = -100
max_num = 100

# Задача 1
# Заведите список целых чисел. Напишите программу, которая будет выводить количество четных и количество нечетных чисел в списке.
# Используйте цикл for и конструкцию if else.

lst = creating_list(min_len_list, max_len_list, min_num, max_num)
even_num = 0
odd_num = 0
for i in lst:
    if i % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
print(f"список: {lst}")
print(
    f"всего чисел: {len(lst)}, количество четных чисел: {even_num}, количечтво нечетных чисел: {odd_num}"
)

# Задача 2
# Заведите список целых чисел. Напишите программу, которая выведет на экран среднее арифметическое значение чисел из списка.
# В данной задаче нельзя использовать встроенные функцию sum(). Используйте цикл for и суммирование элементов в цикле.

lst = creating_list(min_len_list, max_len_list, min_num, max_num)
summa = 0
for i in lst:
    summa += i
print(f"список: {lst}")
print(f"среднее арифметическое значение чисел из списка: {summa/len(lst)}")

# Задача 3
# Заведите список целых чисел. Напишите программу,  которая запрашивает у пользователя число.
# Напишите программу, которая выводит “Число есть в списке” – если заданное число есть в списке, “Числа нет в списке” – иначе.
# В данной задаче нельзя использовать оператор in. Используйте цикл for для перебора элементов списка и конструкцию if.

lst = creating_list(min_len_list, max_len_list, min_num, max_num)
num = int(input("Введите целое число: "))
flag = False
for i in lst:
    if num == i:
        flag = True
        break
print(f"список: {lst}")
if flag == True:
    print("Число есть в списке")
else:
    print("Числа нет в списке")
