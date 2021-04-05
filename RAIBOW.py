import pyfirmata
from pyfirmata import Arduino, INPUT, PWM
import time

board = pyfirmata.Arduino("COM4")

it = pyfirmata.util.Iterator(board)
it.start()

red = board.get_pin('d:3:p')
blue = board.get_pin('d:5:p')
green = board.get_pin('d:6:p')

r=0.31
b=0
g=0

while r>0.3 and r<=0.6: #просто красный
        red.write(r)
        blue.write(0)
        time.sleep(0.05)
        red.write(0)
        r = r + 0.01

while r>=0.6 and r<1:  #переход красный-зеленый
        red.write(r)
        green.write(g)
        time.sleep(0.05)
        red.write(0)
        green.write(0)
        r = r + 0.01
        g = g + 0.01

while g>0.3 and g<=0.6:  # зеленый
        red.write(0)
        green.write(g)
        time.sleep(0.05)
        g = g + 0.01

while g>0.6 and g<=1:  #переход зел-син
        green.write(g)
        blue.write(b)
        time.sleep(0.05)
        green.write(0)
        blue.write(0)
        b = b + 0.01
        g = g + 0.01

while b>0.3 and b<=0.6:  #сининй
        green.write(0)
        blue.write(b)
        time.sleep(0.05)
        blue.write(0)
        b = b + 0.01

while b>0.6 and b<=1:  # син-крас
        blue.write(b)
        red.write(r)
        time.sleep(0.05)
        blue.write(0)
        red.write(0)
        b = b + 0.01
        r = r + 0.01
        
