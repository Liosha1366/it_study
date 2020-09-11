text = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"

#Step 1
words = len(text)
print("\t\t\nШаг 1""\nКоличество символов:", words)

#Step 2
revers = text[::-1]
print("\t\t\nШаг 2""\nСтрока задом на перёд:", revers)

#Step 3
upper_letters = text.title()
print("\t\t\nШаг 3""\nКаждое слово начинается с заглавной буквы:", upper_letters)

#Step 4
upper_swords = text.upper()
print("\t\t\nШаг 4""\nТекст из одних загланых букв:", upper_swords)

#Step 5
a = text.count('нд')
print("\t\t\nШаг 5""\nКоличество символов 'нд' в предложении:", a)

a1 = text.count('ам')
print("\nКоличество символов 'ам' в предложении:", a1)

a2 = text.count('о')
print("\nКоличество символов 'о' в предложении:", a2)

print("\nСравнение количества найденных символов:""\n'нд' больше чем 'ам' -", a > a1)
print("'ам' болбше чем 'о' -", a1 > a2)

#Step 6
print("\t\nШаг 6")
#Конкатенация
print("Cложение строк:")
s = "Hello"
s2 = "World"
print(s, s2)
print(s + s2)

#Дублирование
print("\nДублирование строк:")
print(s)
print(s * 5)

#Доступ по индексу
print("\nДоступ по индексу:")
print(s2)
print(s2[0], "[0] ")
print(s2[1:-1], "[-1:-1] ")
print(s2[:4], "[:4] ")
print(s2[:], "[:] ")

input("\n\nPress Enter to exit.")