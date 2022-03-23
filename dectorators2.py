#Decorator with bye()

def my_decorator(func):
    def wrap_func():
        print("********")
        func()
        print("********")
    return wrap_func

@my_decorator
def hello():
    print('hellloooos')

@my_decorator
def bye():
    print('see ya later')

bye()

#Decorator with hello()

def my_decorator(func):
    def wrap_func():
        print("********")
        func()
        print("********")
    return wrap_func

@my_decorator
def hello():
    print('hellloooos')

@my_decorator
def bye():
    print('see ya later')

hello()


#Decorator 

def my_decorator(func):
    def wrap_func():
        print("********")
        func()
        print("********")
    return wrap_func

@my_decorator
def hello():
    print('hellloooos')

@my_decorator
def bye():
    print('see ya later')

hello2 = my_decorator(hello)
hello2()

#Decorator 

def my_decorator(func):
    def wrap_func():
        print("********")
        func()
        print("********")
    return wrap_func

@my_decorator
def hello():
    print('hellloooos')

@my_decorator
def bye():
    print('see ya later')

my_decorator(hello)()




