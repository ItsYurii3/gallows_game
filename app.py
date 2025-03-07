from word import Word
from player import Player


class Game:
    
    @staticmethod
    def display_menu():
        print("Memu\n".center(15))
        print('1. Play game')
        print('2. Exit \n')
    
    def check_user_choise(self):
        choise = input('Enter your choise.....')
        while True:
            try: 
                choise = int(choise)
                if choise == 1:
                    self.game_cicle()
                    break
                elif choise == 2:
                    break
                else:
                    print('Enter the correct numer')
            except:
                print("Error")
            finally:
                break
    
             
    
    def game_cicle(self):
        riddle_word = Word()            
        player = Player(input("Enter your name.... "))
        while (not riddle_word.is_guess(riddle_word.word)):
            if player.check_attempt_limit():
                break
            user_ch = player.enter_char(riddle_word.word) 
            ch, flag = user_ch
            if flag:
                riddle_word.safe_enter_char(ch)
            
            guess_word = riddle_word.display_word_state()
            print(f"Word:  {guess_word}\n")
             
game = Game()
game.display_menu()
game.check_user_choise()

               
      
      