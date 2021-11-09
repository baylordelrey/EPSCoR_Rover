
import keyboard
from pynput.keyboard import Key, Listener
#from roboclaw import Roboclaw


roverSpeed = 0

def Keyboard_Control(key):
    
    if __name__ == "__main__":
        roboclaw = Roboclaw("/dev/ttyS0", 38400)
        roboclaw.Open()
    
    global roverSpeed
    print("Keyboard Control Activated.")
    pressed_key = str(key).replace("'", "")
    print(" key: ", pressed_key)
    
    if keyboard.is_pressed('w'):
        print("The Rover is moving Forwards")
        roboclaw.ForwardM1(0x80, roverSpeed)
        roboclaw.ForwardM2(0x80, roverSpeed)
        roboclaw.ForwardM1(0x81, roverSpeed)
        roboclaw.ForwardM2(0x81, roverSpeed)
        roboclaw.ForwardM1(0x82, roverSpeed)
        roboclaw.ForwardM2(0x82, roverSpeed)
        
    elif keyboard.is_pressed('s'):
        print("The Rover is moving Backwards")
        roboclaw.BackwardM1(0x80, roverSpeed)
        roboclaw.BackwardM2(0x80, roverSpeed)
        roboclaw.BackwardM1(0x81, roverSpeed)
        roboclaw.BackwardM2(0x81, roverSpeed)
        roboclaw.BackwardM1(0x82, roverSpeed)
        roboclaw.BackwardM2(0x82, roverSpeed)
        
    elif keyboard.is_pressed('a'):
        print("The Rover is turning left")
        roboclaw.BackwardM2(0x83, roverSpeed)
        roboclaw.BackwardM1(0x84, roverSpeed)
        roboclaw.ForwardM1(0x83, roverSpeed)
        roboclaw.ForwardM2(0x84, roverSpeed)
        
    elif keyboard.is_pressed('d'):
        print("The Rover is turning Right")
        roboclaw.ForwardM2(0x83, roverSpeed)
        roboclaw.ForwardM1(0x84, roverSpeed)
        roboclaw.BackwardM1(0x83, roverSpeed)
        roboclaw.BackwardM2(0x84, roverSpeed)
        
    elif keyboard.is_pressed('up'):
        print("Forward Speed Increasing")
        roverSpeed+=5
        
    elif keyboard.is_pressed('down'):
        print("Forward Speed Decreasing")
        roverSpeed-=5
        
    elif keyboard.is_pressed('c'):
        print("The Rover is not Moving")
        roverSpeed = 0
        roboclaw.ForwardM1(0x80, roverSpeed)
        roboclaw.ForwardM2(0x80, roverSpeed)
        roboclaw.ForwardM1(0x81, roverSpeed)
        roboclaw.ForwardM2(0x81, roverSpeed)
        roboclaw.ForwardM1(0x82, roverSpeed)
        roboclaw.ForwardM2(0x82, roverSpeed)
        roboclaw.ForwardM2(0x83, roverSpeed)
        roboclaw.ForwardM1(0x84, roverSpeed)

    if key == Key.esc:
        # Stop listener
        roverSpeed = 0
        print("Keyboard Control Deactivated")
        return False
    
    print("RoverSpeed is set to ", roverSpeed)
    
# Listener
with Listener(on_press=Keyboard_Control) as listener:
    listener.join()
