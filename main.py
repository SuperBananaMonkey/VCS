import time
import random
import os
import platform

class VCS:
    def pause():
        pause = input("[Press ENTER to continue]")

    def parity(num):
        if (num % 2 == 0):
            return True
        else:
            return False

    def charout(data):
        print(data, "\n")

    def wait(seconds):
        time.sleep(seconds)

    def randomInt():
        return random.randint(1, 10000000)

    def increment(numfunct):
        return numfunct + 1

    def clear():
        os.system("cls")

    def fontColor(colour):
        if (colour == "red"):
            os.system("color 04")
        elif (colour == "green"):
            os.system("color 02")
        elif (colour == "blue"):
            os.system("color 01")
        elif (colour == "yellow"):
            os.system("color 06")

    def countdown(secs):
        while secs > 0:
            time.sleep(1)
            secs = secs - 1
            print(secs)

    def getline(put):
        input(put)

    def resetStyle():
        os.system("color 07")

    def detectPlatform():
        os_name = platform.system()
        if (os_name == "Windows"):
            return "Windows"
        elif (os_name == "Linux"):
            return "Linux"
        elif (os_name == "Darwin"):
            return "MacOS"
        else:
            return "Unknown System"

# Documentation for VCS

# VCS works best on Windows
# Darwin is used for MacOS
# Put variable in getline just means input
# VCS.charout("Hello world") - output hello world, and start a new line
# VCS.charout(detectPlatform()) - outputs user's platform name
# VCS.resetStyle() - returns the font color back to normal
# VCS.countdown() - Just makes a countdown and may require to use the CPU more than usual
# VCS.clear() - Clears the screen on consoles
# VCS.pause() - Pauses the screen so users can see the output
# VCS.parity(9) - returns True or False depending on if the number is even (True) or odd (False), in this case it is 9 which would be False since it's an odd number