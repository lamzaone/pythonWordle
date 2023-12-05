import os
import random
import requests
import enchant

d = enchant.Dict("en_US")

os.system('cls' if os.name == 'nt' else 'clear')

def generate_random_word(nr_letters):
    api_url = "https://random-word-api.herokuapp.com/word"
    params={}
    params['length'] = nr_letters

    response = requests.get(api_url,params=params)
    if response.status_code == 200:
        word_data = response.json()
        if word_data:
            return word_data[0]

class Wordle:
    def __init__(self):
        self.word = None
        self.x = input("Enter number of letters: ")
        while self.word is None or not d.check(self.word):
            self.word = generate_random_word(self.x)
        self.wrong_chars = []
        self.words = []
        self.found = 0
        self.score = 0
    
    def check_word(self):
        dictionary = {}
        word=""
        input_word = input("Enter word.\n")
        while len(input_word) != len(self.word) or not d.check(input_word):        
            input_word = input("Wrong length or inexistent word. Enter word again\n")
        for j in range(len(input_word)):
            if input_word[j] == self.word[j]:
                dictionary[j] = input_word[j]
            elif input_word[j] in self.word:
                dictionary[j] = input_word[j].upper()
            else:
                if input_word[j] not in self.wrong_chars: self.wrong_chars.append(input_word[j])
        for j in range (len(self.word)):
            if dictionary.get(j) is not None:
                word += dictionary.get(j)
            else:
                word += '_'
        self.words.append(word)
        if word == self.word:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.words_()
            print(f"Congratulations! You have found the word \"{word}\"")
            self.score += 1
            self.found = 1
            print(f"Your score: {self.score}\n")
            input("")
        
    def reset(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.word = None
        while self.word is None or not d.check(self.word):
            self.word = generate_random_word(self.x)
        self.wrong_chars = []
        self.words = []
        self.found = 0
    
    def words_(self):
        for i in range (5):
                if len(self.words)>i:
                    print(self.words[i])
                else:
                    print('_'*len(self.word))

    def run(self):
        running = True
        while running is True:
            for i in range(5):
                os.system('cls' if os.name == 'nt' else 'clear')
                self.words_()
                word = ""
                print(f"Wrong letters: ", end="")
                for chr in wordle.wrong_chars: print(chr.upper(),end=" ")
                print()
                self.check_word()
            if self.found:
                self.reset()    
            else:
                print(f"You lost. the word was {wordle.word} \nFinal score: {self.score}")
                input("")
                self.score = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                self.x = input("Enter number of letters: ")
                self.reset()

wordle = Wordle()
wordle.run()