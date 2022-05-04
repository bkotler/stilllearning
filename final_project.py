import pandas as pd
class Game:
    """This is the class that holds the functions that run our final project, a word game. This game 
    reads a text file with words on it and a text file with the clues for guessing each word on it.
    The program will then have the player pick if they want too play against the computer and the 
    computers difficulty. The player will then try too guess the word using the clue(s). The player
    and computer are awarded points based on the amount of guesses they used.
    """
    
    def __init__(self, player_name):
        """This will set up the game and initiate the game attributes
        Args:
            player_name (str): The name of the player
        Side effects:
            Sets all the attributes and initilizes the game
        """
        self.player_name = player_name
        self.user_words_guessed = list()
        self.user_points = 0
    def open_files(self, easy_path, medium_path, hard_path):
        """This will open three files and set them to dataframes. Each file
            is a csv file with of each word and clue
            easy_path (str): Filename of the easy clues file
            medium_path (str): Filename of the medium clues file
            hard_path (str): Filename of the hard clues file
        Side effects:
            Sets the words_list and clues_list attributes to the data from the
                files.
        """
        easy_df = pd.read_csv(easy_path)
        medium_df = pd.read_csv(medium_path)
        hard_df = pd.read_csv(hard_path)
    
    def user_guesses(self, player, guess_length):
        
        """This function will take the letters or word guessed by the player and it will return a match stored in the file.

        Args:
            player (str): The player will identify who they are
            guess_length (str):The length of the word guessed by the player
        Returns:
             str: Will return the guesses made by the player (letters or a word)
        """
        name = input("Type your name: ")
        print(f" Hey {name}, Goodluck!")
            
            
        words = input("Guess a word to solve this word game: ")
        turns = 0
        while turns < 3:
            for words in .csv:
                if words in .csv:
                    print(f"Right word {words}")
                else:
                    turns += 1
                    print
        
        
    def computer_guesses(self, player, guess_length):
        """This function will take the letters or word guessed by the player and it will return a match stored in the file.

        Args:
            player (str): The computer will let the humna player know they are playing against the computer
            guess_length (str): The length of the word guessed by the computer player
        Returns:
             str: Will return the guesses made by the computer (letters or a word)
        """
        
    def show_screen(self, player, points, length, guess_number, player_guess, word, clue):
        """ This function displays the screen of the game to the player. This includes the players score,
        the computers score, the length of the word being guessed as well as its clue, and the amount of
        guesses the player and computer have used respectivly. 
        Args:
            player (str): The players name stored as a string.
            points (int): The points that the player or computer have stored as an integer.
            length (int): The length of the word stored as an integer.
            guess_number(int): The amount of guesses the user or computer have used stored as an integer.
            player_guess(str): The guess the player inputs stored as a string.
            word(str): The word the player is trying to guess stored as a string.
            clue(str): the clue the user has stored as a string
        Side Affects: Prints the current board for te user to see.
        """
        guess_number = 0
        if guess_number < 3:
            print(f"{self.player}'s game.")
            print(f"You have {points} points")
            print(f"Your clue is {clue}")
            print(f"The word has {length} letters.")
            print(f"You have used {self.guess_number} amount of guesses.")
            if player_guess == word:
                print(f"{word} is correct!")
            else:
                print(f"{word} is incorrect.")
                guess_number += 1
                print(f"{self.player}'s game.")
                print(f"You have {self.points} points")
                print(f"Your clue is {clue}")
                print(f"The word has {self.length} letters.")
                print(f"You have used {self.guess_number} amount of guesses.")
        else:        
            print("Out of guesses. Game over.")
                
    def calculate_points(self, guess_number, points, length, word):
        """ This function calculates the players and computers points respectivly. It uses the amount of guesses
        used, and the length of the word to calculate the points and adds them to either the player and computers
        score's respectivly.
        Args:
            points(int): The points that the player or computer have stored as an integer.
            length (int): The length of the word stored as an integer.
            guess_number(int): The amount of guesses the user or computer have used stored as an integer.
            word(str): the word the player is trying to guess stored as a string.
        """
        length = len(word)
        points += 0
        if guess_number == 1:
            points += length + 3
        if guess_number == 2:
            points += length + 2
        if guess_number == 3:
            points += length + 1
        else:
            points = 0
            
    def pick_opponent(self, user, name):
        '''This function picks whether the user is playing against the computer or another person
        
            Args:
                user (str): the type of opponent
                name (str): the name of the opponent
        '''
        
        
    def pick_difficulty(self, difficulty):
        '''This function will determine the difficulty of the game, ranging from easiest to hardest
        
            Args:
                difficulty (str): the level of difficulty
        '''
        
if __name__ == "__main__":
    new_game = Game("Joe")