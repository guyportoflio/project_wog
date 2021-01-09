from os import system, name

SCORES_FILE_NAME = "Scores.txt"
#a number to represent a bad return code from a function
BAD_RETURN_CODE = 99


def screen_cleaner():
    # check system, 'nt' for windows
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


screen_cleaner()
