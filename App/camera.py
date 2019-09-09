import cv2
from opentrons import instruments, containers, robot
import time

def goto1():
    robot.move_head(x=83, y=108, z=100)

def goto2():
    robot.move_head(x=175, y=108, z=100)

def goto3():
    robot.move_head(x=269, y=108, z=100)

def capturepetri():
    cam = cv2.VideoCapture(1)
    cv2.namedWindow("test")
    img_counter = 0
    for i in range(3):
        print(i)
        if i == 0:
            goto1()
        elif i == 1:
            goto2()
        elif i == 2:
            goto3()
        time.sleep(1)
        ret, frame = cam.read()
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
    cam.release()
    cv2.destroyAllWindows()
