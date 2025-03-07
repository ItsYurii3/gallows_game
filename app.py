from word import Word
from player import Player


class Game:
    
    @staticmethod
    def display_menu():
        print("Menu: \n")
        print('1. Play game')
        print('2. Exit \n')
    
    
    def check_user_choice(self):
        choice = input('Enter your choise.....')
        while True:
            try: 
                choice = int(choice)
                if choice == 1:
                    self.game_cycle()
                    break
                elif choice == 2:
                    print("You exited from menu")
                    break
                else:
                     print("Please enter either 1 or 2.")
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
    
    
    def game_cycle(self):
        riddle_word = Word()            
        player = Player(input("Enter your name.... "))
        while (not player.check_attempt_limit()):
            user_ch = player.enter_char(riddle_word.word) 
            ch, flag = user_ch
            riddle_word.save_enter_char(ch)
            guess_word = riddle_word.display_word_state()

            print(f"Word:  {guess_word}\n")
            print(f"Mistake {len(riddle_word.incorrect_letters)}: {str(riddle_word.incorrect_letters)}" )
            
            if riddle_word.is_guess(riddle_word.word):
                print(f"{player.name}, you guessed the word {guess_word}. Congratulations, you won! ")
                break
            elif player.check_attempt_limit() and not riddle_word.is_guess():
                 print(f"{player.name}, you lost. Try again!")
         
             
game = Game()
game.display_menu()
game.check_user_choice()

               
      
      