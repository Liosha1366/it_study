#находим ID
import re
from collections import Counter
def reader(file):
    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    with open(file) as f:
        log = f.read()
        ip = re.findall(regexp, log)
        inter_all = len(ip)
        print('Количество всех запросов: ', inter_all)
#исключаем повторные ID
        
    return ip
#количество браузеров
def web1():
    web = []
    web_all = []
    fp = open('573303.log', 'r')
    for line in fp:
        line.split()

        a = line.split('" "')
        b = a[-2]
        
        if b not in web:
            web.append(b)
        else:
            web_all.append(b)
    print("Количество браузеров:", Counter(web))
    print("\n\n\nKоличество запросов от каждого браузера: ", Counter(web_all))
    


if __name__ == '__main__':
    reader('573303.log')
    web1()