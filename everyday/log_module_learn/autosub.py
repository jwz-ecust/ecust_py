import subprocess
import os
import sys
import time
import shutil
import logging

sublist = "/home/users/jwzhang/sublist"
tem_sublist = "/home/users/jwzhang/sublist_temp"
logger = logging.getLogger("zjw")
z1 = logging.FileHandler("sub.log")
z1.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
z1.setFormatter(formatter)
logger.addHandler(z1)

while True:
    new_list = []
    fr = open(sublist)
    c_list = fr.readlines()

    if len(c_list) > 0:
        new_list = c_list[:]
        fw = open(tem_sublist, 'w')
        try:
            for i in c_list:
                os.chdir(i.strip())
                a = subprocess.call("qsub vasp.script", shell=True, stdout=open("/dev/null", "w"), stderr=subprocess.STDOUT)
                if a == 0:
                    # print "finish qsubing job %s" %(i.strip())
                    logger.info("finish subing job %s!" %(i.strip()))
                    new_list.remove(i)
                else:
                   # print "up to max number of job!"
                   logger.warn("The job list has to max number!")
                    break
        except KeyboardInterrupt as e:
            # print e, "manual stop the script"
            logger.error("Error manual stop the script!")
        except Exception:
            # print "other exceptions"
            logger.error("Error: other exceptions!")
        finally:
            fw.writelines(new_list)
            fr.close()
            fw.close()
            shutil.copy(tem_sublist, sublist)
        time.sleep(30)

    else:
        # print "sublist file is null, you should add more jobs"
        logger.critical("Sublist file is null, add more jobs!")
        sys.exit(0)
