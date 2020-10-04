import datetime
import time
import os

#добавляет и повторяет время
def get_current_time():
    now = datetime.datetime.now()
    clock = now.strftime("%H, %M, %S")
    return clock

#Формируем и вывводим цифры
def print_digist(current_time):
    lists = []
    for i in current_time:
        lists.append(i)

#графическая основа 
    a = [('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), (" \u2588\u2588\u2588\u2588  "), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ("\u2588\u2588   \u2588\u2588"), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588')]
    b = [("\u2588\u2588   \u2588\u2588"), ("   \u2588\u2588  "), ("     \u2588\u2588"), ("     \u2588\u2588"), ("\u2588\u2588   \u2588\u2588"), ("\u2588\u2588     "), ("\u2588\u2588     "), ("     \u2588\u2588"), ("\u2588\u2588   \u2588\u2588"), ("\u2588\u2588   \u2588\u2588")]
    c = [("\u2588\u2588   \u2588\u2588"), ("   \u2588\u2588  "), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ("     \u2588\u2588"), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588')]
    d = ["\u2588\u2588   \u2588\u2588", ("   \u2588\u2588  "), ("\u2588\u2588     "), ("     \u2588\u2588"), ("     \u2588\u2588"), ("     \u2588\u2588"), ("\u2588\u2588   \u2588\u2588"), ("     \u2588\u2588"), ("\u2588\u2588   \u2588\u2588"), ("     \u2588\u2588")]
    e = ["\u2588\u2588\u2588\u2588\u2588\u2588\u2588", ("\u2588\u2588\u2588\u2588\u2588\u2588\u2588"), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ("     \u2588\u2588"), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ("     \u2588\u2588"), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588'), ('\u2588\u2588\u2588\u2588\u2588\u2588\u2588')]

#присвоение перемынным цифрового значения    
    a1 = lists[0]
    a2 = lists[1]
    a3 = lists[4]
    a4 = lists[5]
    a5 = lists[8]
    a6 = lists[9]

    b1 = lists[0]
    b2 = lists[1]
    b3 = lists[4]
    b4 = lists[5]
    b5 = lists[8]
    b6 = lists[9]

    c1 = lists[0]
    c2 = lists[1]
    c3 = lists[4]
    c4 = lists[5]
    c5 = lists[8]
    c6 = lists[9]

    d1 = lists[0]
    d2 = lists[1]
    d3 = lists[4]
    d4 = lists[5]
    d5 = lists[8]
    d6 = lists[9]

    e1 = lists[0]
    e2 = lists[1]
    e3 = lists[4]
    e4 = lists[5]
    e5 = lists[8]
    e6 = lists[9]

#пременная генератора
    w = next(g)

#грыфический вывод циферблата      
    print(a[int(a1)], a[int(a2)], "    "           "", a[int(a3)], a[int(a4)], "    "           "", a[int(a5)], a[int(a6)])
    print(b[int(b1)], b[int(b2)], "    "           "", b[int(b3)], b[int(b4)], "    "           "", b[int(b5)], b[int(b6)])
    print(c[int(c1)], c[int(c2)], " "      ,w ,    "", c[int(c3)], c[int(c4)], " "     ,w ,    "", c[int(c5)], c[int(c6)])
    print(d[int(d1)], d[int(d2)], "    "           "", d[int(d3)], d[int(d4)], "    "           "", d[int(d5)], d[int(d6)])
    print(e[int(e1)], e[int(e2)], "    "           "", e[int(e3)], e[int(e4)], "    "           "", e[int(e5)], e[int(e6)])

    #генератор
def my_generator():
    while True:
        yield '\u2588' 
        yield ' '
g = my_generator()

def sleep_while(period):
    time.sleep(period)

def clear_screen():
    #os.system('cls' if os.name == 'nt' else 'clear')
    

if __name__ == "__main__":
    while True:
        current_time = get_current_time()
        print_digist(current_time)
        sleep_while(0.5)
        clear_screen()