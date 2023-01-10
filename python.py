import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#try:
#    while True:
#        button_state = GPIO.input(26)
#        if button_state == False:
#             GPIO.output(, True)
#             print()
#             time.sleep(0.2)        
#         else:
#             GPIO.output(, False)
# except:
#     GPIO.cleanup()

songs = ["A", "B", "C", "D", "E"]

try:
    while True:
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
except:
    GPIO.cleanup()
