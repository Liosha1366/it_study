#практика
print("Введите три числа для дальнейшей работы программы: ")
a = int(input("\nВведите первое число: "))
b = int(input("\nВведите второе число: "))
c = int(input("\nВведите третье число: "))

#1
print("Шаг 1")
print(a and b and c and "Нет нулевых значений!!!")

#2
print("Шаг 2")
print(a or b or c or "Нет нулевых значений!!!")

#3 и #4
print("Шаг 3 и 4")
if a <= (b + c):  
    print("Ваше первое число <= сумме второго и третьего числа.")
    print("Применяем формулу b + c - a")
    print("\nВаш результат: ", b + c - a)
else:
    print("Ваше первое число > сумме второго и третьего числа.")
    print("Применяем формулу a - b - c")
    print("\nВаш результат: ", a - b - c )

#5
print("Шаг 5")
if a > 50 and (b > a or c > a):
    print("Вася")


#6
print("Шаг 6")
if a > 5 or b == 7 or c == 7:
    print("Петя")
