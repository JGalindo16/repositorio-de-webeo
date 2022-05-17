import logging

def ask_name():
    return input("cual es tu nombre?: ")

def greet(name):
    print(f'Hola {name}')

if __name__ == "__main__":
    name = ask_name()
    greet(name)