# -*- ccoding: utf-8 -*-
from wxpy import *
robot = Robot()
my_groups = robot.groups()
my_mps = robot.mps()
driver = my_groups.search("Driver Hub")[0]


@robot.register()
def print_others(msg):
    print(msg)


@robot.register(driver, TEXT)
def auto_reply(msg):
    return "收到来自{}的信息!".format(msg.chat.name)

robot.start()
