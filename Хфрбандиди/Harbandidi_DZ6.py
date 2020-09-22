
users = {'name1': 'pass1', 'name2': 'pass2'}

    #проверка имени и пароля
def auth_required(func):
    def wrapper(*args, **kwargs):
        login = input("Enter login name: ")
        passw = input("Enter password: ")
        if login in users and users[login] == passw: 
            func(*args, **kwargs)
        else:
            print("User doesn't exist or wrong password")
        
    return wrapper


@auth_required
def some_func(some):
    print("Login successful!", some)
    return
    
some_func("Welcome!")