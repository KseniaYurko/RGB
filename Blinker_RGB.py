import pyfirmata
import time

board = pyfirmata.Arduino("COM3")  

N =[2,3,4,5,6,7]

COLOR1 = str(input('Цвет 1: '))
COLOR2 = str(input('Цвет 2: '))
period = float(input('Скорость: '))
count = int(input('Сколько раз повторить? '))

if COLOR1 == 'red' and COLOR2 == 'blue':
    for i in range (count):
        board.digital[5].write(1)
        time.sleep(period)
        board.digital[5].write(0)
        board.digital[4].write(1)
        time.sleep(period)
        board.digital[4].write(0)
    
elif COLOR1 == 'red' and COLOR2 == 'green':
    for i in range (count):
        board.digital[5].write(1)
        time.sleep(period)
        board.digital[5].write(0)
        board.digital[3].write(1)
        time.sleep(period)
        board.digital[3].write(0)
    
elif COLOR1 == 'blue' and COLOR2 == 'red':
    for i in range (count):
        board.digital[7].write(1)
        time.sleep(period)
        board.digital[7].write(0)
        board.digital[2].write(1)
        time.sleep(period)
        board.digital[2].write(0)
    
elif COLOR1 == 'blue' and COLOR2 == 'green':
    for i in range (count):
        board.digital[7].write(1)
        time.sleep(period)
        board.digital[7].write(0)
        board.digital[3].write(1)
        time.sleep(period)
        board.digital[3].write(0)
    
elif COLOR1 == 'green' and COLOR2 == 'red':
    for i in range (count):
        board.digital[6].write(1)
        time.sleep(period)
        board.digital[6].write(0)
        board.digital[2].write(1)
        time.sleep(period)
        board.digital[2].write(0)

elif COLOR1 == 'green' and COLOR2 == 'blue':
    for i in range (count):
        board.digital[6].write(1)
        time.sleep(period)
        board.digital[6].write(0)
        board.digital[4].write(1)
        time.sleep(period)
        board.digital[4].write(0)      