from wxpy import *
robot = Robot()
my_friends = robot.friends()
my_groups = robot.groups()
my_mps = robot.mps()
driver = my_groups.search("Driver Hub")[0]
ck = my_friends.search("蔡恺")[0]


@robot.register()
def print_others(msg):
    print(msg)


@robot.register(my_friends, TEXT)
def auto_reply(msg):
    return "{}真棒".format(msg.chat.name)


# robot.start()

for i in range(200):
    # driver.send("微信机器人刷个屏")
    ck.send("蔡老板真牛逼!")
