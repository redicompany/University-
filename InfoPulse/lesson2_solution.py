# -*- coding: utf-8 -*-
task1string = input("Введите слово(string, строку) = ")
if task1string.isdecimal():
    print("Вы ввели числовое значение")
else:
    print("Вы ввели строчное значение")

print("кол-во пробелов = "+ str(task1string.count(" ")))
print("кол-во символов '.' = "+ str(task1string.count(".")))

task4 = "Homework"
print(" "*46 + task4 + " "*46)
print(task4.upper())

