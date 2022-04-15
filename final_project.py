class Game:
    """This is the class that holds the functions that run our final project, a word game. This game 
    reads a text file with words on it and a text file with the clues for guessing each word on it.
    The program will then have the player pick if they want too play against the computer and the 
    computers difficulty. The player will then try too guess the word using the clue(s). The player
    and computer are awarded points based on the amount of guesses they used.
    """
    
    def __init__(self, player_name = "Joe"):
        """This will set up the game and initiate the game attributes
        Args:
            player_name (str): The name of the player
        Side effects:
            Sets all the attributes and initilizes the game
        """
        
    def open_files(self, words_path, clues_path):
        """This will open two files and set them to lists. One file will be
            for the words and another for the clues.
        Args:
            words_path (str): Filename of the words file
            clues_path (str): Filename of the clues file
        Side effects:
            Sets the words_list and clues_list attributes to the data from the
                files.
        """
    
    def user_guesses():
        """"""
        
    def computer_guesses():
        """"""
        
    def show_screen(self, player, computer, points, length, guess_number):
        """ This function displays the screen of the game to the player. This includes the players score,
        the computers score, the length of the word being guessed as well as its clue, and the amount of
        guess the player and computer have used respectivly. 

        Args:
            player (str): The players name stored as a string.
            computer (str): The computer and its difficulty stored as a string.
            points (int): The points that the player or computer have stored as an integer.
            length (int): The length of the word stored as an integer.
            guess_number(int): The amount of guesses the user or computer have used stored as an integer.
        """

        
    def calculate_points(self, player, computer, points, length, guess_number):
        """ This function calculates the players and computers points respectivly. It uses the amount of guesses
        used, and the length of the word to calculate the points and adds them to either the player and computers
        score's respectivly.
        Args:
           player (str): The players name stored as a string.
            computer (str): The computer and its difficulty stored as a string.
            points (int): The points that the player or computer have stored as an integer.
            length (int): The length of the word stored as an integer.
            guess_number(int): The amount of guesses the user or computer have used stored as an integer.
        """
        
        
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
    new_game = Game()