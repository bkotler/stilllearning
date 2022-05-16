from itertools import count
import pandas as pd
from random import randint
from argparse import ArgumentParser
import re

class Game:
    """This is the class that holds the functions that run our final project, a word game. This game 
    reads a text file with words on it and a text file with the clues for guessing each word on it.
    The program will then have the player pick if they want too play against the computer and the 
    computers difficulty. The player will then try too guess the word using the clue(s). The player
    and computer are awarded points based on the amount of guesses they used.
    """
    
    def __init__(self, player_name, easy_path, hard_path):
        """This will set up the game and initiate the game attributes
        Args:
            player_name (str): The name of the player
        Side effects:
            Sets all the attributes and initilizes the game
        """
        self.player_name = player_name
        self.user_words_guessed = list()
        self.user_points = 0
        self.easy_df, self.hard_df = self.open_files(easy_path, hard_path)
        self.easy = True
        self.df = self.pick_difficulty()
        self.opponent = self.pick_opponent()
        self.word, self.clue = self.generate_word()
        self.count = 0
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
    
    def check_turn(self):
        if self.count%2 == 0:
             return 1
        else:
             return 2
    def user_guesses(self):
        
        """This function will take the letters or word guessed by the player and it will return a match stored in the file.

        Args:
            player (str): The player will identify who they are
            guess_length (str):The length of the word guessed by the player
        Returns:
             str: Will return the guesses made by the player (letters or a word)
        """
        guess = input("Enter a word to solve: ")
    
        while re.search(r"\w", guess) == None:
            guess = input("Invalid guess. Please enter a word.: ")
        return guess
            
    def generate_word(self):
            random_int = randint(0, len(self.df.index)-1)
            word = self.df.iloc[random_int, 0]
            clue = self.df.iloc[random_int, 1]
            return word, clue
        
    def computer_guesses(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        random_int = randint(0, len(self.df.index)-1)
        word_guess = self.df.iloc[random_int, 0]
        
        print(f"The computer gussed: {word_guess} ")
        return word_guess 
            
        
        
    def play_game(self, player_1p, player_2p):
        guess_number_p1 = 1
        while guess_number_p1 < 3:
            print(f"{self.player_name}'s turn.")
            print(f"You have {self.calculate_points(player_1p)} points")
            print(f"Your clue is {self.clue}")
            print(f"The word has {len(self.word)} letters.")
            print(f"You have used {guess_number_p1} amount of guesses.")
            player_guess = self.user_guesses()
            if player_guess == self.word:
                print(f"{self.word} is correct!")
                guess_number_p1 = 3
            else:
                guess_number_p1 += 1
                if guess_number_p1 == 3:        
                    print("Out of guesses. Game over.")
        guess_number_p2 = 1
        while guess_number_p2 < 3:
            print(f"{self.player_name}'s turn.")
            print(f"You have {self.calculate_points(player_2p)} points")
            print(f"Your clue is {self.clue}")
            print(f"The word has {len(self.word)} letters.")
            print(f"You have used {guess_number_p2} amount of guesses.")
            computer_guess = self.computer_guesses()
            if computer_guess == self.word:
                print(f"{self.word} is correct!")
                guess_number_p2 = 3
            else:
                guess_number_p2 += 1
                if guess_number_p2 == 3:        
                    print("Out of guesses. Game over.")
                
    def calculate_points(self, guess_number, player_points):
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
        if guess_number == 1:
            player_points += length + 3
        elif guess_number == 2:
            player_points += length + 2
        elif guess_number == 3:
            player_points += length + 1
        return player_points
    
    
    def pick_opponent(self):
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
        
        if difficulty == "easy":
            self.easy = True
        else:
            self.easy = False
        return self.easy_df if difficulty == "easy" else self.hard_df
    
def argument_parser():
    parser = ArgumentParser()
    parser.add_argument("name", help = "Name of Player")
    parser.add_argument("easy_path", help = "Filepath for easy words (csv)")
    parser.add_argument("hard_path", help = "Filepath for hard words (csv)")
    args = parser.parse_args()
    return args
        
if __name__ == "__main__":
    args = argument_parser()
    new_game = Game(args.name, args.easy_path, args.hard_path)