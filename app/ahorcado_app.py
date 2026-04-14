

import random

def get_word():
    words = ["perro", "gato", "escorpion", "elefante", "cocodrilo"]
    length = len(words)
    index = random.randint(0, length - 1)
    return words[index]

def draw(errors):
    match errors:
        case 0:
            ahorcado = '''
            -----
            |   |
            |
            |
            |
            |
            =====
            '''
        case 1:
            ahorcado = '''
            -----
            |   |
            |   O
            |
            |
            |
            =====
            '''
        case 2:
            ahorcado = '''
            -----
            |   |
            |   O
            |   |
            |
            |
            =====
            '''
        case 3:
            ahorcado = '''
            -----
            |   |
            |   O
            |  /|
            |
            |
            =====
            '''
        case 4:
            ahorcado = '''
            -----
            |   |
            |   O
            |  /|\\
            |
            |
            =====
            '''
        case 5:
            ahorcado = '''
            -----
            |   |
            |   O
            |  /|\\
            |  /
            |
            =====
            '''
        case 6:
            ahorcado = '''
            -----
            |   |
            |   O
            |  /|\\
            |  / \\
            |
            =====
            '''
   
