#Decorator
def my_decorator(func):
    def wrap_func(x, y):
        print('********')
        func(x, y)
        print('********')
    return wrap_func

# @my_decorator
# def hello(greeting='hi', emoji):
#     print(greeting, emoji)

# a = my_decorator(hello)
# a('hiiii', ':)')

#Decorator ex *kwargs meaning keywords arguements    
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('********')
        func(*args, **kwargs)
        print('********')
    return wrap_func

@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)

hello('hiiii')