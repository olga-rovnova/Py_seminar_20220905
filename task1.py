# Задание 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример: 6782 -> 23, 0,56 -> 11

str=input('введите число,\nдля отделения дробной части от целых используйте "точку":\n')

if str[0]=='-':
    str=str[1:]

new_str=str.replace('.','')
print(new_str)

elements=[int(d) for d in new_str]
print(elements)
print(len(elements))

sum=0
for i in range(len(elements)):
    sum+=elements[i]
print(sum)