#     AUTOR:    BrincandoComIdeias
#     APRENDA:  https://cursodearduino.net/
#     SKETCH:   Como Movimentar o Robô usando Ponte H e Pico?
#     DATA:     20/12/22

from machine import Pin
from machine import PWM
from utime import sleep as delay

pinIn1 = Pin(12, Pin.OUT)
pinIn2 = Pin(13, Pin.OUT)
pinIn3 = Pin(14, Pin.OUT)
pinIn4 = Pin(15, Pin.OUT)

motorEsq1 = PWM(pinIn1)
motorEsq2 = PWM(pinIn2)
motorDir1 = PWM(pinIn3)
motorDir2 = PWM(pinIn4)

# Frequencia do PWM Arduino portas 3, 9, 10 e 11
motorEsq1.freq(490)
motorEsq2.freq(490)
motorDir1.freq(490)
motorDir2.freq(490)

# Equivalente a função map()
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# Função para converter a velocidade de 0 a 100 em pulso PWM 16 bits
def pulsoMotor(velocidade):
    return map(velocidade, 0, 100, 0, 65534)

def paraFrente():
    #for vel in range(100, 0, -5):
    #    pulso = pulsoMotor(vel)
        motorEsq1.duty_u16(25000)
        motorDir1.duty_u16(25000)
        delay(1)
        
def paraTras():
    #for vel in range(100, 0, -5):
    #    pulso = pulsoMotor(vel)
        motorEsq2.duty_u16(65000)
        motorDir2.duty_u16(65000)
        delay(0.5)

def parar():
    motorEsq1.duty_u16(0)
    motorDir1.duty_u16(0)
    motorEsq2.duty_u16(0)
    motorDir2.duty_u16(0)

# Delay de 2 segundos para começar a andar
delay(2)

while True:
   
    print("Frente")
    paraFrente()
    print("Para")
    parar()    
    delay(2)
    
    print("Tras")
    paraTras()
    print("Para")
    parar()
    delay(2)