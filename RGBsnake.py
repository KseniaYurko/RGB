import pyfirmata
import time

board = pyfirmata.Arduino("COM3")  

N =[2,3,4,  5,6,7]

COLOR = str(input('Цвет: '))
period = float(input('Скорость: '))
count = int(input('Сколько раз повторить? '))


if COLOR == 'red':
    color1 = 5
    color2 = 2

if COLOR == 'blue':
    color1 = 7
    color2 = 4

if COLOR == 'green':
    color1 = 6
    color2 = 3

for i in range (count):
    board.digital[color1].write(1)
    time.sleep(period)
    board.digital[color1].write(0)
    board.digital[color2].write(1)
    time.sleep(period)
    board.digital[color2].write(0)
    
    if color1 < 7:
        color1 = color1 + 1    
    elif color1 == 7:
        color1 = 5
    
    if color2 < 4:
        color2 = color2 + 1    
    elif color2 == 4:
        color2 = 2