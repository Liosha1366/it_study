from views import render_template

from models import User, Phone



def default_controller(data=None, cls=True):
    """Default controller"""
    render_template(context={}, template="default.jinja2", cls=cls)
    return (input(), None)


def exit_controller(data=None, cls=True):
    render_template(context={}, template="exit.jinja2", cls=cls)
    exit()


def all_users_controller(data=None, cls=True):
    users = User.all()
    render_template(context={'users':users}, template="all_users.jinja2", cls=cls)
    input("Продолжить?")
    return 'main', None # (next state, data)


def add_user_controller(data=None, cls=True):
    render_template(context={}, template="add_user.jinja2", cls=cls)
    username = input()
    user = User.add(username)
    return 21, user # (next state, data)





def add_phone_controller(user, cls=True):
    render_template(context={}, template="add_phone.jinja2", cls=cls)
    phone_number = input()
    phone = Phone.add(phone_number, user)
    return 212, user # (next state, data)


def add_more_controller(user, cls=True):
    render_template(context={}, template="add_more.jinja2", cls=cls)
    answer = input()
    if answer == 'Y':
        return 21, user
    return 51, user # (next state, data)

def get_controller(state):
    return controllers_dict.get(state, default_controller)

def update_users_controller(data=None, cls=True):
    render_template(context={}, template="update_users_controller.jinja2", cls=cls)
    up_user = input()
    if User.name == up_user:
        user = User.update(name=User.name = up_user).where(User.id)
    return 21

def delete_users_controller(data=None, cls=True):
    render_template(context={}, template="delete_users_controller.jinja2", cls=cls)
    input_del = input()
    user = User.delete(User.name == input_del)
    print(user)
    input("Продолжить?")
    return 'main', None

def print_users_controller(data=None, cls=True):
    render_template(context={}, template="print_users_controller.jinja2", cls=cls)
    user_input = input()
    user = User.get(User.name == user_input)
    user.save(S)
    print(user)
    input("Продолжить?")
    return 'main', None



controllers_dict = { # use dict type instead of if else chain
    '0': exit_controller,
    '1': all_users_controller,
    '2': add_users_controller,
    '3': update_users_controller,
    '4': delete_users_controller,
    '5': print_users_controller,
    21: add_phone_controller, # user can't enter 21 of int type
    212: add_more_controller
}