import sys
import time
command = ""
while 1:
    command = input("> ")
    if command.lower() == "start":
        condition = "Car is started!!!\n"
        for x in condition:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.1)
    elif command.lower() == "stop":
        condition = "Car is stopped!!!\n"
        for x in condition:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.1)
    elif command.lower() == "help":
        condition = "star - car start\nstop - car stop\nquit - exit from Game\n"
        for x in condition:
           sys.stdout.write(x)
           sys.stdout.flush()
           time.sleep(0.1)
    elif command.lower() == "quite":
        condition = "Finish Out!!!\n"
        for x in condition:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.1)
        break
  
