import random

user_numbers_picked = []
random_numbers_list = []


# i was nut sure if you wanted the numbers to be in order or just compare if
# they are the same numbers(no matter the order), went with no order required.

def generate_sequence(difficulty):
    # create a list of random numbers
    # remember! turn range length to "difficulty"
    for x in range(difficulty):
        random_numbers_list.append(random.randint(1, 101))
    # print("lvl:" + str(difficulty))
    # print(random_numbers_list)
    return random_numbers_list


def get_list_from_user():
    for x in range(0, len(random_numbers_list)):

        while True:
            try:
                print("enter number {}".format(x + 1))
                user_pick = input()
                num = int(user_pick)
                if 1 <= num <= 101:
                    user_numbers_picked.append(num)
                    # print result
                    break
                else:
                    print("try again")
            except ValueError:
                print("not a number, try again: ")


def is_list_equal():
    if set(str(random_numbers_list)) == set(str(user_numbers_picked)):
        print("i won")
        return True
    else:
        print("i lost")
        return False


def play(diff):
    #  print("difficulty lvl: " + difficulty)
    # generate a random list of numbers
    generate_sequence(diff)
    # show me the random list
    # begin user input for list
    get_list_from_user()
    # print(user_numbers_picked)
    # compare the two lists na return true or false
    is_list_equal()
    # print(is_list_equal())

# play()
