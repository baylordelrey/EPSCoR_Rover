
import keyboard
from roboclaw import Roboclaw
from time import sleep

if __name__ == "__main__":
    roboclaw = Roboclaw("/dev/ttyS0", 38400)
    roboclaw.Open()
    
    while True:
        def press_reaction(event):
            if event.name == 'w':
                roboclaw.ForwardM1(0x80,40)
                roboclaw.ForwardM2(0x80,40)
                roboclaw.ForwardM1(0x81,40)
                roboclaw.ForwardM2(0x81,40)
                roboclaw.ForwardM1(0x82,40)
                roboclaw.ForwardM2(0x82,40)
            if event.name == 's':
                roboclaw.BackwardM1(0x80,40)
                roboclaw.BackwardM2(0x80,40)
                roboclaw.BackwardM1(0x81,40)
                roboclaw.BackwardM2(0x81,40)
                roboclaw.BackwardM1(0x82,40)
                roboclaw.BackwardM2(0x82,40)
            if event.name == 'c':
                roboclaw.ForwardM1(0x80,0)
                roboclaw.ForwardM2(0x80,0)
                roboclaw.ForwardM1(0x81,0)
                roboclaw.ForwardM2(0x81,0)
                roboclaw.ForwardM1(0x82,0)
                roboclaw.ForwardM2(0x82,0)
                roboclaw.ForwardM2(0x83,0)
                roboclaw.ForwardM1(0x84,0)
                roboclaw.BackwardM1(0x83,0)
                roboclaw.BackwardM2(0x84,0)
            if event.name == 'd':
                roboclaw.ForwardM2(0x83,20)
                roboclaw.ForwardM1(0x84,20)
                roboclaw.BackwardM1(0x83,20)
                roboclaw.BackwardM2(0x84,20)
            if event.name == 'a':
                roboclaw.BackwardM2(0x83,20)
                roboclaw.BackwardM1(0x84,20)
                roboclaw.ForwardM1(0x83,20)
                roboclaw.ForwardM2(0x84,20)
        keyboard.on_press(press_reaction)   
        sleep(2) 