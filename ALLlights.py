import pyfirmata
import time

board = pyfirmata.Arduino("COM4")  

board.digital[5]
].write(1)
board.digital[3].write(1)
