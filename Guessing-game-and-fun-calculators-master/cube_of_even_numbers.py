import pyautogui as gui
gui.alert('This program gives an output based on the range of numbers you provide.')
one = int(gui.prompt('Give first integer: '))
two = int(gui.prompt('Give second integer: '))
for i in range(one, two):
    if i%2==0:
        print (f'Cube of {i} is {i**3}') #for square print(f'Square of {i} is {i**3}
    else:
        print('There is no even number in the range you have given.')
