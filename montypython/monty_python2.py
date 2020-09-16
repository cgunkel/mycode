#!/usr/bin/env python3

#Counter is round
round = 0

# While Loop
while True:
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of ------"')
    answer = input("Your guess--> ")
    if answer == 'Brian':
        print('Correct')
        break
    elif round==3:
        print('Sorry, the answer was Brian.')
        break
    print('Sorry! Try again!')

