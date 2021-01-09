import random
from urllib.request import urlopen
import json
import Live
random_generated_number = random.randint(1, 100)
# currency api key: 14451ac9f9e3c2e1a8f3905246acb717
url2 = urlopen("http://apilayer.net/api/live?access_key=14451ac9f9e3c2e1a8f3905246acb717&currencies=ILS")


def play(diff):
    get_money_interval(diff)
    # print(range_of_error)
    low_range = int(range_of_error[0])
    high_range = int(range_of_error[1])
    # print(low_range)
    # print(high_range)
    get_guess_from_user()
    if low_range <= user_guess <= high_range:
        print("win")
        Live.win_or_lose = diff
        return True
    else:
        print("lose")
        Live.win_or_lose = 0
        return False


def get_money_interval(difficulty):
    global range_of_error
    # open url
    url_read = (url2.read())
    # get result of conversion
    result = url_read
    # close url
    # save the result
    result = json.loads(result)
    # print(str(result))
    # getting the value of the exchange rate
    rate = result["quotes"]["USDILS"]
    total_value = rate * random_generated_number
    # print(rate)
    # print(str(random_generated_number))
    # print(total_value)
    interval = (total_value - (5 - difficulty), total_value + (5 - difficulty))
    range_of_error = interval


# print(interval)
# print(range_of_error)


def get_guess_from_user():
    global user_guess
    while True:
        try:
            print("enter the value in SHEKELS to the \namount of {} "
                  "US DOLLARS: \n".format(random_generated_number))
            user_input = input()

            if user_input.isnumeric():
                user_guess = int(user_input)
                break
            else:
                print("try again")

        except ValueError:
            print("not a number, try again: ")


# print(user_input)

# play()
