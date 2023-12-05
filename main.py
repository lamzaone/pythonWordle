import os
import random
import requests

def generate_random_word(letters):
    api_url = "https://random-word-api.herokuapp.com/word"
    params={}
    params['length'] = letters

    response = requests.get(api_url,params=params)
    if response.status_code == 200:
        word_data = response.json()
        if word_data:
            return word_data[0]

    return None

class Wordle:
    def __init__(self):
        os.system('cls')
        print(f"Game started!")
        x=input("Select number of letters: ")
        self.word = generate_random_word(x)
        print(f"The word has {len(self.word)} letters.")

wordle = Wordle();
dictionary = {}
wrong_chars = []
word = ""
words = []
for i in range (5):
    os.system('cls')
    for i in range (5):
        if len(words)>i:
            print(words[i])
        else:
            print('_'*len(wordle.word))
    word = ""
    print(f"Wrong letters: ", end="")
    for chr in wrong_chars: print(chr.upper(),end=" ")
    print()
    input_word = input("Enter word.\n")
    while len(input_word) != len(wordle.word):        
        input_word = input("Wrong length. Enter word again\n")
    for j in range(len(input_word)):
        if input_word[j] == wordle.word[j]:
            dictionary[j] = input_word[j]
        elif input_word[j] in wordle.word:
            dictionary[j] = input_word[j].upper()
        else:
            if input_word[j] not in wrong_chars: wrong_chars.append(input_word[j])
    word = ""
    for j in range (len(wordle.word)):
        if dictionary.get(j) is not None:
            word += dictionary.get(j)
        else:
            word += '_'
    words.append(word)
    dictionary = {}
    if word == wordle.word:
        print(f"Congratulations! You have found the word \"{word}\"")
        exit(0)
print(f"You lost. the word was {wordle.word}")