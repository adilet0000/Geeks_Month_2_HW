from random import randint
from decouple import config

def start():
    attempts = config('ATTEMPTS', cast=int)
    capital = config('INITIAL_CAPITAL', cast=int)
    min_range = config('RANGE_MIN', cast=int)
    max_range = config('RANGE_MAX', cast=int)
    random_num = randint(min_range, max_range)

    while attempts > 0:
        print(f"\nATTEMPS: {attempts}\nMONEY: {capital}$\n")
        try:
            guess = int(input(f"Guess a random number from {min_range} to {max_range}: \n"))
        except ValueError:
            print("ERROR")
            continue

        if guess == random_num:
            print(f'You got it. The number was: {random_num}!')
            capital *= 2
            print(f'You have {capital}$ at this moment')
            keep_going = int(input('Do you wanna play more?\n1 - YES\n2 - NO\n'))
            if keep_going == 1:
                attempts = config('ATTEMPTS', cast=int)
                random_num = randint(min_range, max_range)
            else:
                print(f'You\'ve won {capital}$')
                break
        else:
            attempts -= 1
            hint = "LESS" if guess > random_num else "BIGGER"
            print(f'\nRandom number is {hint} than yours. You have: {attempts} extra attempts')

        if attempts == 0:
            print(f'The number was: {random_num}|WASTED|You\'ve lost all your money.')
            break