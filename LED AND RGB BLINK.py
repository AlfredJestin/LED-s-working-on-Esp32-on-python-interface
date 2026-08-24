from machine import ADC,Pin
from utime import sleep


b = Pin(25,Pin.OUT)
b1 = Pin(14,Pin.OUT)
g = Pin(26,Pin.OUT)
y1 = Pin(12,Pin.OUT)
r = Pin(27,Pin.OUT)
r1 = Pin(13,Pin.OUT)

while True:
    
     b1.value(0)
     y1.value(0)
     r1.value(1)
     b.value(0)
     g.value(0)
     r.value(1)
     sleep(1)
     b1.value(0)
     y1.value(1)
     r1.value(0)
     b.value(0)
     g.value(1)
     r.value(1)
     sleep(1)
     b1.value(1)
     y1.value(0)
     r1.value(0)
     b.value(0)
     g.value(1)
     r.value(0)
     sleep(1)
    
    
     
