# -*- coding: utf-8 -*-
import schedule
import time


def job():
    print "I am working...."


schedule.every(10).minute.do(job)    # 每隔10分钟执行一次任务
schedule.every().hour.do(job)    # 每个一小时执行一次任务
schedule.every().dat.at("10:30").do(job)    # 每天10:30执行一次任务
schedule.every().monday.do(job)    # 每周一的这个时候执行任务
schedule.every().wednesday.at("13:15").do(job)    # 每周三13:15执行一次任务

while True:
    schedule.run_pending()
    time.sleep(1)
