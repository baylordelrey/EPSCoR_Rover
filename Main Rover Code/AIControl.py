"""
1. Write a program to control roboclaw motors with a keyboard
"""

import sys, tty, termios, os, time
import roboclaw
import serial

# Linux software serial port on Raspberry Pi
#ttyAMA0 = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

# Linux USB serial port on Raspberry Pi
ttyUSB0 = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=3.0)

# Windows USB serial port on PC
#ttyUSB0 = serial.Serial("COM4", baudrate=115200, timeout=3.0)

# Set up roboclaw
rc = roboclaw.Roboclaw("/dev/ttyS0", 115200)
rc.Open()

# Get keyboard input
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Motor control
def motor_control(char):
    if char == 'w':
        rc.ForwardM1(0x80, 64)
        rc.ForwardM2(0x80, 64)
        rc.ForwardM1(0x81, 64)
        rc.ForwardM2(0x81, 64)
        rc.ForwardM1(0x82, 64)
        rc.ForwardM2(0x82, 64)
    elif char == 's':
        rc.BackwardM1(0x80, 64)
        rc.BackardM2(0x80, 64)
        rc.BackwardM1(0x81, 64)
        rc.BackwardM2(0x81, 64)
        rc.BackwardM1(0x82, 64)
        rc.BackwardM2(0x82, 64)
    # elif char == 'a':
    #     rc.BackwardM1(address, 64)
    #     rc.ForwardM2(address, 64)
    # elif char == 'd':
    #     rc.ForwardM1(address, 64)
    #     rc.BackwardM2(address, 64)
    elif char == ' ':
        rc.ForwardM1(0x80, 0)
        rc.ForwardM2(0x80, 0)
        rc.ForwardM1(0x81, 0)
        rc.ForwardM2(0x81, 0)
        rc.ForwardM1(0x82, 0)
        rc.ForwardM2(0x82, 0)
# Main loop
if __name__ == "__main__":
    while True:
        char = getch()
        motor_control(char)
        if char == 'q':
            break