from Live import load_game, welcome
global difficulty
# difficulty = 0
print(welcome("Guy"))
load_game()
# tricking the system, had too much problem with circular import error
# so im sending the result of difficulty and win from here
