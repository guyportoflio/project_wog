import os
# from MainGame import difficulty

# POINTS_OF_WINNING = (difficulty * 3) + 5


def add_score(diff):
    # check if Score file even exists
    if os.path.exists("Scores.txt"):
        # check to see if there is anything in Scores file,
        # moved to avoid crash if no file exists
        print("file exists")
    else:
        print("no Scores.txt file")
        # create a file and enter the score into it
        score_file = open("Scores.txt", "w+")
        score_file.write(str((diff * 3) + 5))
        score_file.close()

    empty_or_not = os.path.getsize("Scores.txt")
    if empty_or_not == 0:
        print("score file is empty!")
        score_file = open("Scores.txt", "a+")
        score_file.write(str((diff * 3) + 5))
        score_file.close()

    else:
        print("score file is not empty")
        score_file = open("Scores.txt", "r")
        existing_value = score_file.read()
        print(existing_value)
        new_value = int(existing_value) + ((diff * 3) + 5)
        score_file = open("Scores.txt", "w+")
        score_file.write(str(new_value))
        # print("new value: " + str(new_value))
        print("new value in file:" + str(new_value))
        score_file.close()

