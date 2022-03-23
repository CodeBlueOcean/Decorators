def hello():
    print('helloooooo');

greet = hello()
del hello
hello()

print(greet())

# example
def hello(func):
    func()

def greet():
    print('still here!')

a = hello(greet)

print(a)

