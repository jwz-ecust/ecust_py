# -*- ccoding: utf-8 -*-
from wxpy import *
robot = Robot()
my_groups = robot.groups()
my_mps = robot.mps()
# driver = my_groups.search("Driver Hub")[0]
my_friend = robot.friends().search("5byg5L2z5Lyf")

zjw = utils.Tuling(api_key="5a494f1a82024daba9449cab43e45db6")

@robot.register()
def print_others(msg):
    return zjw.do_reply(msg)

@robot.register()
def auto_reply(msg):
    return zjw.reply_text(msg)

robot.start()
