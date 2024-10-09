import os

def clear_screen():
    os.system('clear')

def header(h1, h2, h3):
    clear_screen()
    print('.: Kalkylator :.')
    print('--------------')
    print('-', h1)
    print('-', h2)
    print('-', h3)
    print('--------------')