# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 13:32:06 2021

@author: baylo
"""
import KeyboardControl
import PiArduinoComm

def main():
    global roverSpeed
    KeyboardControl()
    ArduinoData()