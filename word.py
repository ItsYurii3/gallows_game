import random


class Word:   
                 
    def __init__(self):
        self.word = self.generate_word().lower()
        self.guessed_letters = set()
        self.incorrect_letters = set()   
        
    @staticmethod   
    def generate_word():
        with open("wordList.txt", 'r') as text:
              word_list = text.read().split()
              return random.choice(word_list)        
         
    def safe_enter_char(self, ch: str):
        if len(ch) > 1 or ch == " ":
            print("You should enter just one character")
            return
        if ch in self.guessed_letters or ch in self.incorrect_letters:
            print("You have already entered this character")
            return
        
        if ch in self.word:
            self.guessed_letters.add(ch)
        else:
            self.incorrect_letters.add(ch)
    
    
    def display_word_state(self):
        hidden_word = "".join(ch if ch in self.guessed_letters else "_" for ch in self.word)
        return hidden_word
            
            
    def is_guess(self, word: str):
       return all(i in self.guessed_letters for i in word)