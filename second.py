# В некоторой школе решили набрать три новых математических класса 
# и оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

students_count_1 = int(input("Введите количество учеников в классе 1 "))
students_count_2 = int(input("Введите количество учеников в классе 2 "))
students_count_3 = int(input("Введите количество учеников в классе 3 "))
print((students_count_1 + 1) // 2 + (students_count_2 + 1) // 2 + (students_count_3 + 1) // 2 )