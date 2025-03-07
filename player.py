class Player:
    
    def __init__(self, name):
        self.name = name
        self.attempt_limit = 6
        self.attempt_user = 0
    
    
    def enter_char(self, word: str):
        while(self.attempt_limit > self.attempt_user):
            ch = input('Enter a char...  ').strip().lower()
            if len(ch) == 1 and ch.isalpha():
                if ch in word:
                    print("You have guessed the character\n")
                    return ch, True
                else:
                    print("You don`t guessed the character\n")
                    self.attempt_user += 1
                    return ch, False
            else:
                print("You have entered not correct symbol\n")    
            
            
    def check_attempt_limit(self):
        return self.attempt_limit == self.attempt_user