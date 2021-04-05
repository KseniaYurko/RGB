import pyfirmata
from pyfirmata import Arduino, INPUT, PWM
import time

board = pyfirmata.Arduino("COM4")

it = pyfirmata.util.Iterator(board)
it.start()

red = board.get_pin('d:3:p')
blue = board.get_pin('d:5:p')
green = board.get_pin('d:6:p')

r=0.50
b=0.50
g=0.50

for i in range(100):    
   
    while r>=0.5 and r<=1:
        red.write(r)
        time.sleep(0.01)
        red.write(0)
        r = r + 0.01
    
    while r>0:
        red.write(r)
        green.write(g)
        time.sleep(0.01)
        red.write(0)
        green.write(0)        
        r = r - 0.02
        g = g + 0.01

    r=0.51

    while g>=0.5 and g<=1:
        green.write(g)
        time.sleep(0.01)
        green.write(0)
        g = g + 0.01

    while g>0:
        green.write(g)
        blue.write(b)
        time.sleep(0.01)
        green.write(0)
        blue.write(0)        
        g = g - 0.02
        b = b + 0.01  

    g=0.51

    while b>=0.5 and b<=1:
        blue.write(b)
        time.sleep(0.01)
        blue.write(0)
        b = b + 0.01

    while b>0:
        blue.write(b)
        red.write(r)
        time.sleep(0.01)
        blue.write(0)
        red.write(0)
        b = b - 0.02
        r = r + 0.01

    b=0.51