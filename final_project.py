from importlib.machinery import WindowsRegistryFinder
import pandas as pd
from random import randint

class Game:
    """This is the class that holds the functions that run our final project, a word game. This game 
    reads a text file with words on it and a text file with the clues for guessing each word on it.
    The program will then have the player pick if they want too play against the computer and the 
    computers difficulty. The player will then try too guess the word using the clue(s). The player
    and computer are awarded points based on the amount of guesses they used.
    """
    
    def __init__(self, player_name, easy_path):
        """This will set up the game and initiate the game attributes
        Args:
            player_name (str): The name of the player
        Side effects:
            Sets all the attributes and initilizes the game
        """
        self.player_name = player_name
        self.user_words_guessed = list()
        self.user_points = 0
        self.easy_df, self.hard_df = self.open_files(easy_path)
        self.df = self.pick_difficulty()
        self.word, self.clue = self.generate_word()
        self.play_game()
        
    def open_files(self, easy_path, hard_path):
        """This will open three files and set them to dataframes. Each file
            is a csv file with of each word and clue
            easy_path (str): Filename of the easy clues file
            medium_path (str): Filename of the medium clues file
            hard_path (str): Filename of the hard clues file
        Side effects:
            Sets the words_list and clues_list attributes to the data from the
                files.
        """
        
        return pd.read_csv(easy_path), pd.read_csv(hard_path)
    
    def user_guesses(self, guess_length, clue):
        
        """This function will take the letters or word guessed by the player and it will return a match stored in the file.

        Args:
            player (str): The player will identify who they are
            guess_length (str):The length of the word guessed by the player
        Returns:
             str: Will return the guesses made by the player (letters or a word)
        """
<<<<<<< HEAD
       
=======
>>>>>>> 1b1b141e04e5b303d6dc668a9f0b28f81b7b6337
        
        return input(f"Your clue is {clue}. Enter a word to solve:")
            
    def generate_word(self):
            df = self.df
            word = "Bicycle"
            clue = "A vehicle with training wheels"
            return word, clue
        
    def computer_guesses(clue):
        """This function will take the letters or word guessed by the player and it will return a match stored in the file.

        Args:
            player (str): The computer will let the humna player know they are playing against the computer
            guess_length (str): The length of the word guessed by the computer player
        Returns:
             str: Will return the guesses made by the computer (letters or a word)
        """
        guesses = clue 
        while guesses == words:
            print ("The computer gussed:" guesses)
            
        
        
    def play_game(self):
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
        guess_number = 1
        while guess_number < 3:
            player_guess = self.user_guesses(0, self.clue)
            print(f"{self.player_name}'s game.")
            print(f"You have {self.calculate_points(guess_number)} points")
            print(f"Your clue is {self.clue}")
            print(f"The word has {len(self.word)} letters.")
            print(f"You have used {guess_number} amount of guesses.")
            guess_number += 1
            if player_guess == self.word:
                print(f"{self.word} is correct!")
                guess_number = 3
            elif guess_number == 3:        
                print("Out of guesses. Game over.")
                
    def calculate_points(self, guess_number):
        """ This function calculates the players and computers points respectivly. It uses the amount of guesses
        used, and the length of the word to calculate the points and adds them to either the player and computers
        score's respectivly.
        Args:
            points(int): The points that the player or computer have stored as an integer.
            length (int): The length of the word stored as an integer.
            guess_number(int): The amount of guesses the user or computer have used stored as an integer.
            word(str): the word the player is trying to guess stored as a string.
        """
        length = len(self.word)
        points = 0
        if guess_number == 1:
            points += length + 3
        if guess_number == 2:
            points += length + 2
        if guess_number == 3:
            points += length + 1
        else:
            points = 0
            
    def pick_opponent(self, opponent, user_name, opponent_name):
        '''This function picks whether the user is playing against the computer or another person
        
            Args:
                opponent (str): the type of opponent
                user_name (str): the name of the user
                opponent_name (str, optional): the name of the opponent (only if it is another user, not a computer)
        '''
        
        opponent = input("Who do you want to play? (computer or human)")
        
        if opponent == "human":
            return input("What is the name of the other human?")
        else:
            return opponent
        
    def pick_difficulty(self):
        '''This function will determine the difficulty of the game, ranging from easiest to hardest
        
            Args:
                difficulty (str): the level of difficulty
        '''
        difficulty = input("What difficulty do you want? (easy or hard)")
        
        return self.easy_df if difficulty == "easy" else self.hard_df
        
if __name__ == "__main__":
    new_game = Game("Joe", "words.csv")