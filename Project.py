
import random                                                       #Package to pick random words from a list
import time                                                         #Package to create a delay of time in the code.
import re                                                           #Package to have a regular expression

Movies = open('Movies.txt', 'r')                                    #Text file containing names of movies
Brands = open('Brands.txt', 'r')                                    #Text file containgin names of brands
Countries = open('Countries.txt', 'r')                              #Text file containing names of Countries

options = ["Movies", "Brands", "Countries"]                         #creating a variable with the options for the user

name = input("What's your name? \n")
time.sleep(1)                                                       #Adding a delay of 1 second
print("Hello, ", name, ". Are you ready to play Hangman?")

time.sleep(2)                                                       #Adding a delay of 2 seconds
print("The Categories are:", )
for i in range(len(options)):
    print(options[i])

time.sleep(2)

print(name, ", you now choose the desired category for the game.")
time.sleep(2)

print("Have you decided yet?")

time.sleep(1)

while True:
    option = input("Enter your option: \n")
    option = option.lower()
    option = option.capitalize()
    if option in options:
        print("It seems you have chosen", option, "as your category.")
        break
    else:
        print("Wrong input. Try again!")

time.sleep(1)

print("Your word for the game will be chosen from the ", option, " category now.")

if option == "Movies":                                              #if-else statements to comapre the option added by user
    lists = Movies.readlines()
elif option == "Brands":
    lists = Brands.readlines()
elif option == "Countries":
    lists = Countries.readlines()

words = random.choice(lists)                                        #Randomly choosing the word
word = words.lower()
word = re.sub(r'[^a-zA-Z]', "", word)                            #Removing special characters from the word from the list

time.sleep(1)

print("Your game starts in :")
for i in range(3, 0, -1):           #For givving the countdown
    print(i)
    time.sleep(1)

guess_character = ''

turns = len(word)-1 #To know the number of turns


while turns > 0:
    fail = 0
    for char in word:
        if char in guess_character:
            print(char.upper()+" ", end="")

        else:
            print(" _ ", end=" ")
            fail += 1

    if fail == 0:
        print("\n You won")

        break

    guess = input(". \t Guess characters: ")
    guess = guess.lower()       #Changing the case of the letter inputted by the user to lower
    guess_character += guess

    if guess not in word:
        turns = turns - 1


        print("Wrong guess")

    # Number of turns left
        print("You have", + turns, "more guesses. Keep trying!")

    #When the turns are equal to zero
        if turns == 0:
            print("You have lost the game \n")
            print("The word is :", word.capitalize())
            print("Bye ")
            print("  ____")
            print(" |    |")
            print(" |    0")
            print(" |  \/|\/ ")
            print(" |    |")
            print(" |   / \ ")
            print("_|_")
