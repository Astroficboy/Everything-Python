import pyautogui as gui
gui.alert('This program gives an output based on the range of numbers you provide.')
gui.alert('You can change the program for the output you want. This only gives square root.')
one = int(gui.prompt('Give first integer: '))
two = int(gui.prompt('Give second integer: '))
for i in range(one, two):
    print (f'Sqaure root of {i} is {i**1/2}')
