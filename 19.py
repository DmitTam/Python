# Задача №19. Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 3

# Output:  [3, 4, 5, 1, 2]

# Примечание: Пользователь может вводить значения списка или список задан изначально.

from random import randint

list = [i for i in range(1, randint(5, 10))]
print(list)

k = int(input("введите число: "))
# print(list.pop())

for _ in range(k):
    last_num = list.pop()
    list.insert(0,last_num)
print(list)