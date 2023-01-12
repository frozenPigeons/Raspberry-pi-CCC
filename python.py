import RPi.GPIO as GPIO
import time
Digits = [20, 24, 23, 10]
Switches = [19, 13, 6, 9, 16, 12, 25]
Buttons = [17, 27, 22, 26]

GPIO.setmode(GPIO.BCM)
def A(pin):
    GPIO.output(20, True)
    GPIO.output(24, False)
    GPIO.output(23, False)
    GPIO.output(10, False)

    GPIO.output(16, False)
    GPIO.output(25, False)
    GPIO.output(19, False)
    GPIO.output(9, False)
    GPIO.output(12, False)
    GPIO.output(13, False)
    GPIO.output(6, True)

def B():
    GPIO.output(20, False)
    GPIO.output(24, True)
    GPIO.output(23, False)
    GPIO.output(10, False)

    GPIO.output(16, False)
    GPIO.output(25,False)
    GPIO.output(19,False)
    GPIO.output(9, False)
    GPIO.output(12, False)
    GPIO.output(13, False)
    GPIO.output(6, False)

def C():
    GPIO.output(20, False)
    GPIO.output(24, False)
    GPIO.output(23, True)
    GPIO.output(10, False)

    GPIO.output(16, False)
    GPIO.output(25,False)
    GPIO.output(19,False)
    GPIO.output(9, True)
    GPIO.output(12, True)
    GPIO.output(13, True)
    GPIO.output(6, False)

def D():
    GPIO.output(20, False)
    GPIO.output(24, False)
    GPIO.output(23, False)
    GPIO.output(10, True)

    GPIO.output(16, False)
    GPIO.output(25,False)
    GPIO.output(19,False)
    GPIO.output(9, True)
    GPIO.output(12, False)
    GPIO.output(13, False)
    GPIO.output(6, False)

for i in Buttons:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for i in Digits:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, False)

for i in Switches:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, True)

songs = ["A", "B", "C", "D"]
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

    A()

    time.sleep(0.001)

    B()

    time.sleep(0.001)

    C()

    time.sleep(0.001)

    D()
