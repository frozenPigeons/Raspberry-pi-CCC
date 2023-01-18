import RPi.GPIO as GPIO
import time
Digits = [20, 24, 23, 10]
Switches = [16, 25, 19, 9, 12, 13, 6]
Buttons = [17, 27, 22, 26]

GPIO.setmode(GPIO.BCM)
def A():
    Aarr = [False, False, False, False, False, False, True]

    for i in range(len(Switches)):
        GPIO.output(Switches[i], Aarr[i])



def B():
    Barr = [False, False, False, False, False, False, False]

    for i in range(len(Switches)):
        GPIO.output(Switches[i], Barr[i])


def C():

    Carr = [False, False, False, True, True, True, False]

    for i in range(len(Switches)):
        GPIO.output(Switches[i], Carr[i])

def D():

    Darr = [False, False, False, True, False, False, False]

    for i in range(len(Switches)):
        GPIO.output(Switches[i], Darr[i])

def E():
    Earr = [False, False, False, False, True, True, False]

    for i in range(len(Switches)):
        GPIO.output(Switches[i], Earr[i])

for i in Buttons:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for i in Digits:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, False)

for i in Switches:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, True)

songs = ["A", "B", "C", "D", "E"]
print('Starting...')

while GPIO.input(17) != False:
    if(GPIO.input(26) == False):
        songs = [songs[1], songs[2], songs[3], songs[4], songs[0]]
        time.sleep(0.3)
    if(GPIO.input(22) == False):
        songs = [songs[4], songs[0], songs[1], songs[2], songs[3]]
        time.sleep(0.3)
    if(GPIO.input(27) == False):
        songs = [songs[1], songs[0], songs[2], songs[3], songs[4]]
        time.sleep(0.3)


if(GPIO.input(17) == False):
    print(songs)

while True:
    time.sleep(0.001)
    GPIO.output(20, True)
    GPIO.output(24, False)
    GPIO.output(23, False)
    GPIO.output(10, False)
    if songs[0] == 'A':
        A()
    if songs[0] == 'B':
        B()
    if songs[0] == 'C':
        C()
    if songs[0] == 'D':
        D()
    if songs[0] == 'E':
        E()
    time.sleep(0.001)
    GPIO.output(20, False)
    GPIO.output(24, True)
    GPIO.output(23, False)
    GPIO.output(10, False)
    if songs[1] == 'A':
        A()
    if songs[1] == 'B':
        B()
    if songs[1] == 'C':
        C()
    if songs[1] == 'D':
        D()
    if songs[1] == 'E':
        E()  
    time.sleep(0.001)
    GPIO.output(20, False)
    GPIO.output(24, False)
    GPIO.output(23, True)
    GPIO.output(10, False)
    if songs[2] == 'A':
        A()
    if songs[2] == 'B':
        B()
    if songs[2] == 'C':
        C()
    if songs[2] == 'D':
        D()
    if songs[2] == 'E':
        E()  
    time.sleep(0.001)
    GPIO.output(20, False)
    GPIO.output(24, False)
    GPIO.output(23, False)
    GPIO.output(10, True)
    if songs[3] == 'A':
        A()
    if songs[3] == 'B':
        B()
    if songs[3] == 'C':
        C()
    if songs[3] == 'D':
        D()
    if songs[3] == 'E':
        E()  