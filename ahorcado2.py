''' Juego del Ahorcado '''
import random

#Una variable en mayúsculas es una variable constante.
IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = ["lavadora", "secadora", "sofa", "covid19", "coronavirus", "ordenador", "python", "teclado"]


def random_word():
    idx = random.randint(0, len(WORDS)-1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print("")
    print(hidden_word)
    print("--- * --- * --- * --- * --- * --- * --- * ---")



def run():
    word = random_word()
    hidden_word = ['_'] * len(word)
    tries = 0
    
    while True:
        display_board(hidden_word, tries)
        current_letter = input("Escoge una letra: ")
        
        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)
                
        
        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                display_board(hidden_word, tries)
                print("")
                print("¡Perdiste! La palabra correcta era ", word)
                break            
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter
                
            letter_indexes = []
        
        try:
            hidden_word.index('_')
        except ValueError:
            print("¡Felicidades! ¡Gánaste!, la palabra era", word)
            break

if __name__ == '__main__':
    print("B I E N V E N I D O S    A H O R C A D O S")
    run()
