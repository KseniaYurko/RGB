import pyfirmata
import time

board = pyfirmata.Arduino("COM4")  

COLOR = str(input('Цвет: '))
period = float(input('Время: '))

if COLOR == 'red':
    board.digital[4].write(1)
    time.sleep(period)
    board.digital[4].write(0)
elif COLOR == 'green':
    board.digital[2].write(1)
    time.sleep(period)
    board.digital[2].write(0)
elif COLOR == 'blue':
    board.digital[3].write(1)
    time.sleep(period)
    board.digital[3].write(0)

