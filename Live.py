import CurrencyRouletteGame
import MemoryGame
import GuessGame


def welcome(name):
    print("Hello {} and welcome to the World Of Games(WOG).".format(name))
    # used return to avoid "None" output due to 2 prints
    return "Here you can find many cool games to play\n"


def load_game():
    res = input("Please choose a game to play:\n1.Memory Game - a sequence" +
                " of numbers will appear for 1 second and you have to guess" +
                " it back\n2.Guess Game - guess a number and see if you" +
                " chose like the computer\n3.Currency Roulette - " +
                "try and guess the value of a random amount of USD in ILS\n")

    while True:
        # forcing user to submit a valid int response
        try:
            turn_to_number = int(res)

            if 1 <= turn_to_number <= 3:
                print("good pick")
                break
            else:
                res = input("value needs to be between 1 and 3:")
                continue
        except ValueError:
            res = input("not a non decimal number or out of range, try again: ")

    difficulty = input("please select a difficulty level from 1 to 5: ")
    while True:
        try:
            int(difficulty)
            turn_to_number = int(difficulty)

            if 1 <= turn_to_number <= 5:
                print("good pick")
                break
            else:
                difficulty = input("value needs to be between 1 and 5:")
                continue
        except ValueError:
            difficulty = input("not a number, try again:")
    # from this point i am adding the last part changes from WOG2
    # print("result " + res)
    # print(difficulty)
    if int(res) == 1:
        print("memory")
        MemoryGame.play(int(difficulty))
    elif int(res) == 2:
        GuessGame.play(int(difficulty))
    elif int(res) == 3:
        print("currency")
        CurrencyRouletteGame.play(int(difficulty))
    else:
        pass
