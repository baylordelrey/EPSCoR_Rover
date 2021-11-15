import keyboard
import threading
from pynput.keyboard import Key, Listener
from time import sleep 
# from roboclaw import Roboclaw

def on_press(key):
    try:
        print('{0} pressed'.format(
            key.char))
    except AttributeError:
        print('{0} pressed'.format(
            key))
        
    if keyboard.is_pressed('w'):
        Thread1 = threading.Thread(target=DriveForwardM1, args=(0x80,40))
        Thread2 = threading.Thread(target=DriveForwardM1, args=(0x81,40))
        Thread3 = threading.Thread(target=DriveForwardM1, args=(0x82,40))
        Thread4 = threading.Thread(target=DriveForwardM2, args=(0x80,40))
        Thread5 = threading.Thread(target=DriveForwardM2, args=(0x81,40))
        Thread6 = threading.Thread(target=DriveForwardM2, args=(0x82,40))
        Thread1.start()
        Thread2.start()
        Thread3.start()
        Thread4.start()
        Thread5.start()
        Thread6.start()
        Thread1.join()
        Thread2.join()
        Thread3.join()
        Thread4.join()
        Thread5.join()
        Thread6.join()
        
    elif keyboard.is_pressed('s'):
        Thread1 = threading.Thread(target=DriveBackwardM1, args=(0x80,40))
        Thread2 = threading.Thread(target=DriveBackwardM1, args=(0x81,40))
        Thread3 = threading.Thread(target=DriveBackwardM1, args=(0x82,40))
        Thread4 = threading.Thread(target=DriveBackwardM2, args=(0x80,40))
        Thread5 = threading.Thread(target=DriveBackwardM2, args=(0x81,40))
        Thread6 = threading.Thread(target=DriveBackwardM2, args=(0x82,40))
        Thread1.start()
        Thread2.start()
        Thread3.start()
        Thread4.start()
        Thread5.start()
        Thread6.start()
        Thread1.join()
        Thread2.join()
        Thread3.join()
        Thread4.join()
        Thread5.join()
        Thread6.join()
        
    elif keyboard.is_pressed('a'):
        print("Turning Left")
        Thread7 = threading.Thread(target=TurnLeftM1, args=(0x83,20))
        Thread8 = threading.Thread(target=TurnLeftM2, args=(0x84,20))
        Thread7.start()
        Thread8.start()
        Thread7.join()
        Thread8.join()
        
    elif keyboard.is_pressed('d'):
        print("Turning Right")
        Thread9 = threading.Thread(target=TurnRightM1, args=(0x83,20))
        Thread10 = threading.Thread(target=TurnRightM2, args=(0x84,20))
        Thread9.start()
        Thread10.start()
        Thread9.join()
        Thread10.join()
        
    if keyboard.is_pressed('c'):
        Thread1 = threading.Thread(target=DriveForwardM1, args=(0x80,0))
        Thread2 = threading.Thread(target=DriveForwardM1, args=(0x81,0))
        Thread3 = threading.Thread(target=DriveForwardM1, args=(0x82,0))
        Thread4 = threading.Thread(target=DriveForwardM2, args=(0x80,0))
        Thread5 = threading.Thread(target=DriveForwardM2, args=(0x81,0))
        Thread6 = threading.Thread(target=DriveForwardM2, args=(0x82,0))
        Thread1.start()
        Thread2.start()
        Thread3.start()
        Thread4.start()
        Thread5.start()
        Thread6.start()
        Thread1.join()
        Thread2.join()
        Thread3.join()
        Thread4.join()
        Thread5.join()
        Thread6.join()
        
def on_release(key):
    print('{0} released'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False
    
def DriveForwardM1(address, speed):
    print(hex(address), "Moving M1 Forwards")
    # roboclaw.ForwardM1(hex(address), speed)
    
def DriveForwardM2(address, speed):
    print(hex(address)) 
    print("Moving M2 Forwards")
    # roboclaw.ForwardM2(hex(address), speed)

def DriveBackwardM1(address, speed):
    print(hex(address), "Moving Backwards")
    # roboclaw.BackwardM1(address, speed)
    # roboclaw.BackwardM2(address, speed)

def DriveBackwardM2(address, speed):
    print(hex(address), "Moving Backwards")
    # roboclaw.BackwardM1(address, speed)
    # roboclaw.BackwardM2(address, speed)
    
def TurnLeftM1(address, speed):
    print(hex(address), "Turning Left")
    
def TurnLeftM2(address, speed):
    print(hex(address), "Turning Left")

def TurnRightM1(address, speed):
    print(hex(address), "Turning Right")
    
def TurnRightM2(address, speed):
    print(hex(address), "Turning Right")

def Stop(address, speed):
    print("Stopping Rover")
       
if __name__ == "__main__":

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
