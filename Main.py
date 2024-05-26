import random

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = []
game = False
computer_number = random.choice(list1)


def number_guess():
    while game == False:
        computer_number = random.choice(list1)
        number = int(input("Guess a number. "))
        if number == computer_number:
            print("Congratulations you guessed correctly.")
            game == True
            break
        else:
            print("Sorry you guessed wrong.")


number_guess()
