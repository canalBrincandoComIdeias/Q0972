#     AUTOR:    BrincandoComIdeias
#     APRENDA:  https://cursodearduino.net/
#     SKETCH:   Como Movimentar o Robô usando Ponte H e Pico?
#     DATA:     20/12/22

from machine import Pin
from utime import sleep as delay

pinIn1 = Pin(12, Pin.OUT)
pinIn2 = Pin(13, Pin.OUT)
pinIn3 = Pin(14, Pin.OUT)
pinIn4 = Pin(15, Pin.OUT)

def paraFrente():
    pinIn1.value(1)
    pinIn2.value(0)
    
    pinIn3.value(1)
    pinIn4.value(0)
        
def paraTras():
    pinIn1.value(0)
    pinIn2.value(1)
    
    pinIn3.value(0)
    pinIn4.value(1)

def parar():
    pinIn1.value(0)
    pinIn2.value(0)
    pinIn3.value(0)
    pinIn4.value(0)
    
while True:
    print("Frente")
    paraFrente()
    delay(0.25)
    print("Para")
    parar()    
    delay(2)
    
    print("Tras")
    paraTras()
    delay(0.25)
    print("Para")
    parar()
    delay(2)