def my_range():
    start = 0
    while start != 10:
        start += 1
        r = start % 3
        if r == 0:
            print("Василий")
        else:    
            yield start
        
for i in my_range():
    print(i)