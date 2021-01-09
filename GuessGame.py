import random

import Live


def generate_number(difficulty):
    global secret_number
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    global user_number_guess
    user_number_guess = input("guess a number from 1 to {}\n".format(difficulty))
    # print(user_number_guess)
    while True:
        try:
            guess = int(user_number_guess)

            if 1 <= guess <= difficulty:
                print("good pick")
                break
            else:
                user_number_guess = input("value needs to be between 1 and {}}:".format(difficulty))
                continue
        except ValueError:
            user_number_guess = input("not a non decimal number or out of range, try again: ")
    # print(user_number_guess)
    return user_number_guess


def compare_results(diff):
    global win_or_lose
    if int(user_number_guess) == secret_number:
        win_or_lose = True
        Live.win_or_lose = diff
        print("i win")
    else:
        win_or_lose = False
        print("i lose")
    return win_or_lose


def play(diff):
    generate_number(diff)
    # print(secret_number)
    get_guess_from_user(diff)
    compare_results(diff)
    print(win_or_lose)
