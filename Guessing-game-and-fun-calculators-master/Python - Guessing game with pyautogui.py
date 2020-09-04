import random
import pyautogui                        #You'll need to install pyautogui, use pip method 'pip install pyautogui'.
n = random.randint(1, 101)              #Edit the number as you wish or keep guessing
guess = int(pyautogui.prompt('Guess the number: '))

while n != guess:
    print
    if guess < n:
        print ("guess is low")          #you don't need this print command
        guess = int(pyautogui.prompt('Guess is too low, guess the number again: '))
    elif guess > n:
        print ("guess is high")         #nor this
        guess = int(pyautogui.prompt('Guess is too high, guess the number again: '))
    else:
        pyautogui.alert('You nailed it!!!')
        break
    print
