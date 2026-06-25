def decorator(func):
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper
def say_hello():
    print("Hello!")
f=decorator(say_hello)
f()  # Output: Before the function call. Hello! After the function call.


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()