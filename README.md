Final Project / Still Learning
INST326-0102
Sorian Kamara, Benny Kotler, Kaleb Afework, Jaron Richman
05/18/2022

An explanation of the purpose of each file in your repository
final_project.py: This is the file that has actual program that allows the user to play the game against the computer
easy_words.csv: This file contains words and a clue for each word. This is considered “easy” because it is harder for the computer to randomly guess the word.
hard_words.csv: This file contains words and a clue for each word. It is just a few of the words and clues from the easy file. This is considered “hard” because it is easier for the computer to randomly guess the word.
play_game_with_graph.ipynb: This file is a Jupyter notebook that lets you run the game and it will show the bar graph at the end.
Instructions on how to run our program from the command line
Please follow the instructions below:
python3 final_project.py “Alex” “easy_words.csv” “hard_words.csv” 


Instructions on how to use our program and / or interpret the output of the program (as applicable)

You can use our program in two ways:
Without the bar graph: If you run it in the command line using the final_project.py file, the game will play well, but won’t display the bar graph at the end
With the bar graph: If you want the bar graph at the end, go to the file play_game_with_graph.ipynb and click the run all button. You can even change the 2nd cell to include your name instead of “Alex” which is listed as default.

Attribution: the primary author of each major function / method
Class Game:

Benny Kotler:
def __init__(self, player_name, easy_path, hard_path)
def open_files(self, easy_path, hard_path)
def __repr__ (self)
def argument_parser()

Sorian Kamara:
def user_guesses(self)
def generate_word(self)
def computer_gusses(self)

Kaleb Afework:
def play_game(self)
def calculate_points(self, guess_number, player_points)
def check_turn(self)

Jaron Richman:
def show_scores(self, player_1p, player_2p)
def pick_diffculty(self)


Annotated bibliography of all sources we used to develop our project. For each source, explain how we used the source. 
All codes are original, we didn't use anything from the web. For our csv files, we randomly came up with words we use in our day to day lives. 
