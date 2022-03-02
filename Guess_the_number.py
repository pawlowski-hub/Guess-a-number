import random
from logo import logo
str(logo)
print(logo)


def difficulty_attempts():
    dif_lvl = input("Chose difficulty level(Easy/Hard):\n").lower()
    dif_set = False
    attempts = 5

    if dif_lvl == "easy" or dif_lvl == "hard":
        print(f"{dif_lvl.capitalize()} Mode:")
        if dif_lvl == "easy":
            dif_set = True
    else:
        print("Incorrect answer.\n"
              "Hard Mode:")

    if dif_set:
        attempts = 10
    return attempts


def generated_number():
    number = random.randrange(1, 101, 1)
    return number


def game(num, attempts):
    while attempts > 0:
        user_num = int(input("Choose number(1-100): "))
        if num < user_num:
            print("Too high number!")
            attempts -= 1
            print(f"Remaining attempts: {attempts}")
        elif num > user_num:
            print("Too low number!")
            attempts -= 1
            print(f"Remaining attempts: {attempts}")
        elif num == user_num:
            print("You won!")
            break
        if attempts == 0:
            print("You lose!")


guessing_number = generated_number()
num_of_attempts = difficulty_attempts()
game(guessing_number, num_of_attempts)
print(f"Number is {guessing_number}")
exit()
