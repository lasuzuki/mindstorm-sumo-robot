#!/usr/bin/env pybricks-micropython
from pybricks.hubs import *
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.parameters import Port, Color, ImageFile, SoundFile
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
color_sensor_front = ColorSensor(Port.S2)
color_sensor_back = ColorSensor(Port.S1)
touch_sensor = TouchSensor(Port.S3)
#ir_sensor = InfraredSensor(Port.S4)

# Write your program here.
#ev3.screen.draw_text(10, 40,'HARUO YAGUCHI')
ev3.screen.load_image(ImageFile.NEUTRAL)
ev3.light.on(Color.GREEN)
ev3.speaker.say('PLAYER: ONO')
ev3.speaker.beep()
#ev3.screen.clear()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
ev3.screen.load_image(ImageFile.ANGRY)
ev3.light.on(Color.YELLOW)

flag = 0
while True:
    robot.drive(500,0)

    if(touch_sensor.pressed()):
        robot.stop()
        flag = 1
        ev3.light.on(Color.RED)
        break
    
    if(color_sensor_front.color() == Color.BLACK and color_sensor_back.color() != Color.BLACK):
        robot.stop()
        ev3.speaker.beep(1)
        robot.turn(180)

    elif(color_sensor_back.color() == Color.BLACK and color_sensor_front.color() == Color.BLACK):
        robot.stop()
        ev3.screen.load_image(ImageFile.KNOCKED_OUT)
        ev3.light.on(Color.RED)
        ev3.speaker.say('Ono lost')
        break

if(flag == 1):
    robot.straight(1000)
    robot.drive(2000,0)

robot.stop()