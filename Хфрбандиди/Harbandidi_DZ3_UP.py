#калькулятор BMI_UP

list = {}

print("\tЗдравстуйте Вас привестствует, база данных BMI 'Индекс Массы Тела'")
print("Введите несколько значений для получения результата:")

name = ""
while not name:
     name = input("\n\nВведите Ваше имя: ")
     if name not in list:
          ves = ""
          while not ves:
               ves = int(input("\nВведите Ваш вес в килограммах: "))
          rost = ""
          while not rost:
               rost = int(input("\nВведите Ваш рост в сантиметрах: "))
          age = ""
          while not age:    
               age = int(input("\nВведите Ваш возраст: "))
          gender = ""
          while gender != 'man' and gender != 'woman':
               gender = input("\nВведите Ваш пол(ПРИМЕР:Мужчина - man, Женщина - woman): ")
               gender = gender.lower()
          #перевод в метры
          rost_m = rost / 100
          rost_m1 = rost_m * rost_m

          #формула 
          index = int(ves / rost_m1)

          list[name] = {"Пол": gender , "Возраст": age , "Рост": rost , "Вес": ves, "BMI": index}
          print("\n\nПользователь", name, "добавлен в базу данных BMI.")
          
          
          if age < 10:
               print("\n\nERROR:Не возможно корректно произвести расчеты.\nСожалеем, но Вы слишком юны для нашей базы данных.")
               break
          elif age <= 15 and rost <= 162 and rost > 173 and ves >= 48 and ves < 62 and gender == "man":
               print("\n\nПоздравляем. У Вас идеальный показатель BMI!!! ")
               print("Так держать!")
          elif age <= 15 and rost <= 157 and rost > 166 and ves >= 50 and ves < 60 and gender == "woman":
               print("\n\nПоздравляем. У Вас идеальный показатель BMI!!! ")
               print("Так держать!")
          elif age <= 15 and rost <= 154 and rost > 157 and ves >= 46 and ves < 50 and gender == "woman":
               print("\n\nВаш вес ниже среднего, поездка к бабушке вам аойдет на пользу")
          elif age <= 15 and rost <= 158 and rost > 162 and ves >= 43 and ves < 48 and gender == "man":
               print("\n\nВаш вес ниже среднего, поездка к бабушке вам пойдет на пользу")
          elif age <= 15 and rost <= 154 and rost > 158 and ves >= 38 and ves < 43 and gender == "man":
               print("\n\nУ Вас низкий вес, неделька у бубушки и все будет в норме")
          elif age <= 15 and rost <= 154 and ves >= 38 and gender == "man":
               print("\n\nу  Вас очень низкий вес, настоятельно рекамендуем остаток лета провести у бабушки!")
          elif age <= 15 and rost <= 150 and rost > 154 and ves >= 42 and ves < 46 and gender == "woman":
               print("\n\nУ Вас низкий вес, неделька у бубушки и все будет в норме")
          elif age <= 15 and rost <= 151 and ves >= 42 and gender == "woman":
               print("\n\nу  Вас очень низкий вес, настоятельно рекамендуем остаток лета провести у бабушки!")
          elif age <= 15 and rost <= 173 and rost > 181 and ves >= 62 and ves < 80 and gender == "man":
               print("\n\nВаш вес выше среднего, вечерние прогулки вам не повредят")
          elif age <= 15 and rost <= 166 and rost > 173 and ves >= 66 and ves < 74 and gender == "woman":
               print("\n\nВаш вес выше среднего, вечерние прогулки вам не повредят")
          elif age <= 15 and rost <= 173 and ves >= 75 and gender == "woman":
               print("\n\nУ вас очень высокий вес! Вам требуется болбше активности, басей илиактивные игры пойдут Вам на полбзу")
          elif age <= 15 and rost <= 181 and ves >= 80 and gender == "man":
               print("\n\nУ вас очень высокий вес! Вам требуется болбше активности, басей илиактивные игры пойдут Вам на полбзу")
          elif rost < 150 and ves >= 94:
               print("\n\nУ Вас критическая масса тела, обратитесь к специалисту!")
          elif gender == "man" and age >= 20 and age < 30:
               if index >= 16 and index < 18:
                    print("\n\nУ Вас критическая масса тела, состояние анорексии, обратитесь к специалисту!")
               elif index >= 19 and index < 21:
                    print("\n\nУ Вас низкий вес, неделька у бубушки и все будет в норме")
               elif index >= 22 and index < 25:
                    print("\n\nПоздравляем. У Вас идеальный показатель BMI!!! ")
                    print("Так держать!")
               elif index >= 26 and index < 29:
                    print("\n\nВаш вес выше среднего, вечерние прогулки вам не повредят")
               elif index >= 30 and index < 32:
                    print("\n\nУ вас очень высокий вес! Вам требуется болбше активности, басей илиактивные игры пойдут Вам на полбзу")
               elif index >= 32 and index < 36:
                    print("\n\nУ Вас критическая масса тела, обратитесь к специалисту!")
               elif index >= 36 and index < 42:
                    print("\n\nТретья степень ожирения")
               elif index > 42:
                    print("\n\nЧетвертая степень ожирения")
          elif gender == "man" and age >= 30:
               if index >= 18 and index < 19:
                    print("\n\nУ Вас критическая масса тела, состояние анорексии, обратитесь к специалисту!")
               elif index >= 19 and index < 22:
                    print("\n\nУ Вас низкий вес, неделька у бубушки и все будет в норме")
               elif index >= 22 and index < 26:
                    print("\n\nПоздравляем. У Вас идеальный показатель BMI!!! ")
                    print("Так держать!")
               elif index >= 26 and index < 30:
                    print("\n\nВаш вес выше среднего, вечерние прогулки вам не повредят")
               elif index >= 30 and index < 34:
                    print("\n\nУ вас очень высокий вес! Вам требуется болбше активности, басей илиактивные игры пойдут Вам на полбзу")
               elif index >= 34 and index < 38:
                    print("\n\nУ Вас критическая масса тела, обратитесь к специалисту!")
               elif index >= 38 and index < 43:
                    print("\n\nТретья степень ожирения")
               elif index > 43:
                    print("\n\nЧетвертая степень ожирения")
          elif gender == "woman":
               if index <= 16:
                    print("\n\nУ Вас критическая масса тела, состояние анорексии, обратитесь к специалисту!")
               elif index >= 16 and index < 18:
                    print("\n\nУ Вас низкий вес, неделька у бубушки и все будет в норме")
               elif index >= 18 and index < 25:
                    print("\n\nПоздравляем. У Вас идеальный показатель BMI!!! ")
                    print("Так держать!")
               elif index >= 25 and index < 30:
                    print("\n\nВаш вес выше среднего, вечерние прогулки вам не повредят")
               elif index >= 30 and index < 34:
                    print("\n\nУ вас очень высокий вес! Вам требуется болбше активности, басей илиактивные игры пойдут Вам на полбзу")
               elif index >= 34 and index < 40:
                    print("\n\nУ Вас критическая масса тела, обратитесь к специалисту!")
               elif index >= 40:
                    print("\n\nТретья степень ожирения")
               
          print("Ваш индекс массы тела составляет -", index)
          print("""\n
       |дефицит |недостаток|  норма  |избыток |ожирение |резкое ожирение| 
          """)
          print("\t5" + "=" * index + "|" + "=" * (55 - index) + "50")
 
     else:
          print("\n\t\nПользователь с таким именем уже существует!")
          print("Попробуйте изменить Имя пользователя.")     


choice = None
while choice != "0":
     print(
    """
     0 - Выйти
     1 - Добавить нового пользователя
     2 - Найти пользователя по имени
     3 - Посмотреть список пользователей
     4 - Изменить значения данные пользователя
     5 - Удалить пользавотеля

     """
     )
    
     choice = input("Ваш выбор: ")

     if choice == "0":
        print("До свидания.")

#калькулятор BMI
     if choice == "1":
          name = ""
          while not name:
               name = input("Введите Ваше имя: ")
               if name not in list:
                    ves = ""
                    while not ves:
                         ves = int(input("\nВведите Ваш вес в килограммах: "))
                    rost = ""
                    while not rost:
                         rost = int(input("\nВведите Ваш рост в сантиметрах: "))
                    age = ""
                    while not age:    
                         age = int(input("\nВведите Ваш возраст: "))
                    gender = ""
                    while gender != 'man' and gender != 'woman':
                         gender = input("\nВведите Ваш пол(ПРИМЕР:Мужчина - man, Женщина - woman): ")
                         gender = gender.lower()
          
                    #перевод в метры
                    rost_m = rost / 100
                    rost_m1 = rost_m * rost_m

                    #формула 
                    index = int(ves / rost_m1)

               list[name] = {"Пол": gender , "Возраст": age , "Рост": rost , "Вес": ves, "BMI": index}
               print("\n\n\nПользователь", name , "добавлен в словарь.")

               if age < 10:
                    print("\n\nERROR:Не возможно корректно произвести расчеты.\nСожалеем, но Вы слишком юны для нашей базы данных.")
                    break
               elif age <= 15 and rost <= 162 and rost > 173 and ves >= 48 and ves < 62 and gender == "man":
                    print("\n\nПоздравляем. У Вас идеальный показатель BMI!!! ")
                    print("Так держать!")
               elif age <= 15 and rost <= 157 and rost > 166 and ves >= 50 and ves < 60 and gender == "woman":
                    print("\n\nПоздравляем. У Вас идеальный показатель BMI!!! ")
                    print("Так держать!")
               elif age <= 15 and rost <= 154 and rost > 157 and ves >= 46 and ves < 50 and gender == "woman":
                    print("\n\nВаш вес ниже среднего, поездка к бабушке вам аойдет на пользу")
               elif age <= 15 and rost <= 158 and rost > 162 and ves >= 43 and ves < 48 and gender == "man":
                    print("\n\nВаш вес ниже среднего, поездка к бабушке вам пойдет на пользу")
               elif age <= 15 and rost <= 154 and rost > 158 and ves >= 38 and ves < 43 and gender == "man":
                    print("\n\nУ Вас низкий вес, неделька у бубушки и все будет в норме")
               elif age <= 15 and rost <= 154 and ves >= 38 and gender == "man":
                    print("\n\nу  Вас очень низкий вес, настоятельно рекамендуем остаток лета провести у бабушки!")
               elif age <= 15 and rost <= 150 and rost > 154 and ves >= 42 and ves < 46 and gender == "woman":
                    print("\n\nУ Вас низкий вес, неделька у бубушки и все будет в норме")
               elif age <= 15 and rost <= 151 and ves >= 42 and gender == "woman":
                    print("\n\nу  Вас очень низкий вес, настоятельно рекамендуем остаток лета провести у бабушки!")
               elif age <= 15 and rost <= 173 and rost > 181 and ves >= 62 and ves < 80 and gender == "man":
                    print("\n\nВаш вес выше среднего, вечерние прогулки вам не повредят")
               elif age <= 15 and rost <= 166 and rost > 173 and ves >= 66 and ves < 74 and gender == "woman":
                    print("\n\nВаш вес выше среднего, вечерние прогулки вам не повредят")
               elif age <= 15 and rost <= 173 and ves >= 75 and gender == "woman":
                    print("\n\nУ вас очень высокий вес! Вам требуется болбше активности, басей илиактивные игры пойдут Вам на полбзу")
               elif age <= 15 and rost <= 181 and ves >= 80 and gender == "man":
                    print("\n\nУ вас очень высокий вес! Вам требуется болбше активности, басей илиактивные игры пойдут Вам на полбзу")
               elif rost < 150 and ves >= 94:
                    print("\n\nУ Вас критическая масса тела, обратитесь к специалисту!")
               if gender == "man" and age >= 20 and age < 30:
                    if index >= 16 and index < 18:
                         print("\n\nУ Вас критическая масса тела, состояние анорексии, обратитесь к специалисту!")
                    elif index >= 19 and index < 21:
                         print("\n\nУ Вас низкий вес, неделька у бубушки и все будет в норме")
                    elif index >= 22 and index < 25:
                         print("\n\nПоздравляем. У Вас идеальный показатель BMI!!! ")
                         print("Так держать!")
                    elif index >= 26 and index < 29:
                         print("\n\nВаш вес выше среднего, вечерние прогулки вам не повредят")
                    elif index >= 30 and index < 32:
                         print("\n\nУ вас очень высокий вес! Вам требуется болбше активности, басей илиактивные игры пойдут Вам на полбзу")
                    elif index >= 32 and index < 36:
                         print("\n\nУ Вас критическая масса тела, обратитесь к специалисту!")
                    elif index >= 36 and index < 42:
                         print("\n\nТретья степень ожирения")
                    elif index > 42:
                              print("\n\nЧетвертая степень ожирения")
                    if gender == "man" and age >= 30:
                         if index >= 18 and index < 19:
                              print("\n\nУ Вас критическая масса тела, состояние анорексии, обратитесь к специалисту!")
                         elif index >= 19 and index < 22:
                              print("\n\nУ Вас низкий вес, неделька у бубушки и все будет в норме")
                         elif index >= 22 and index < 26:
                              print("\n\nПоздравляем. У Вас идеальный показатель BMI!!! ")
                              print("Так держать!")
                         elif index >= 26 and index < 30:
                              print("\n\nВаш вес выше среднего, вечерние прогулки вам не повредят")
                         elif index >= 30 and index < 34:
                              print("\n\nУ вас очень высокий вес! Вам требуется болбше активности, басей илиактивные игры пойдут Вам на полбзу")
                         elif index >= 34 and index < 38:
                              print("\n\nУ Вас критическая масса тела, обратитесь к специалисту!")
                         elif index >= 38 and index < 43:
                              print("\n\nТретья степень ожирения")
                         elif index > 43:
                              print("\n\nЧетвертая степень ожирения")
                    if gender == "woman":
                         if index <= 16:
                              print("\n\nУ Вас критическая масса тела, состояние анорексии, обратитесь к специалисту!")
                         elif index >= 16 and index < 18:
                              print("\n\nУ Вас низкий вес, неделька у бубушки и все будет в норме")
                         elif index >= 18 and index < 25:
                              print("\n\nПоздравляем. У Вас идеальный показатель BMI!!! ")
                              print("Так держать!")
                         elif index >= 25 and index < 30:
                              print("\n\nВаш вес выше среднего, вечерние прогулки вам не повредят")
                         elif index >= 30 and index < 34:
                              print("\n\nУ вас очень высокий вес! Вам требуется болбше активности, басей илиактивные игры пойдут Вам на полбзу")
                         elif index >= 34 and index < 40:
                              print("\n\nУ Вас критическая масса тела, обратитесь к специалисту!")
                         elif index >= 40:
                              print("\n\nТретья степень ожирения")
               
                         print("Ваш индекс массы тела составляет -", index)
                         print("""\n
                    |дефицит |недостаток|  норма  |избыток |ожирение |резкое ожирение| 
                         """)
                         print("\t5" + "=" * index + "|" + "=" * (55 - index) + "50")
     
                    else:
                         print("\n\t\nПользователь с таким именем уже существует!")
                         print("Попробуйте изменить Имя пользователя.")

     if choice == "2":
          name_1 = input("Чтобы найти пользователя, введите его имя: ")
          if name_1 in list:
               defin = list[name_1]
               print("\n", name_1 , " ", defin)
          else:
               print("\nУвы, пользователя", name, "нет в базе: ")
               print("\nПопробуйте добавить его в словарь.")


     if choice == "3":
          for key, value in list.items():
               print("Имя Пользователя:", key ,".  " "Данные:", value)
     
     #замена параметров пользователя
     if choice == "4":
          name = input("Для замены параметров пользователя введите его имя: ")
          if name in list:
               ves = ""
               while not ves:
                    ves = int(input("\nВведите Ваш вес в килограммах: "))
               rost = ""
               while not rost:
                    rost = int(input("\nВведите Ваш рост в сантиметрах: "))
               age = ""
               while not age:    
                    age = int(input("\nВведите Ваш возраст: "))
               gender = ""
               while gender != 'man' and gender != 'woman':
                    gender = input("\nВведите Ваш пол(ПРИМЕР:Мужчина - man, Женщина - woman): ")
                    gender = gender.lower()
          list[name] = {"Пол": gender , "Возраст": age , "Рост": rost , "Вес": ves, "BMI": index}
          print("\n\nПользователь", name , "изменен.")

     #удаления пользователя
     if choice == "5":
          name = input("Какого пользователя вы хотите удалить? ")
          if name in list:
               del list[name]
               print("\nПользователь", name , "удален.")
          else:
               print("\nНичем не могу помочь. Пользователя", name , "нет в словаре.")


input("\t\nPress Enter to exit")










