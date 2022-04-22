from machine import Pin
from time import sleep
Ledazul = Pin(1, Pin.OUT)
Ledamarillo = Pin(2, Pin.OUT)
Pulsador1 = Pin(28, Pin.IN)
Pulsador2 = Pin(27, Pin.IN)

while 2 != 3:
  if Pulsador1.value() == 1:
    Ledazul.on()
  else:
    Ledazul.off()
  
  if Pulsador2.value() == 1:
    Ledamarillo.value(not Ledamarillo.value())
    sleep(.5)
