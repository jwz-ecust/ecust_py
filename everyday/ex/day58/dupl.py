import os
import re
import sys
from threading  import Thread
from datetime import datetime
import subprocess
import cPickle
import argparse
import hashlib
import collections



def md5(fname, size=4096):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(size), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def all_duplicate(file_dict, path=""):
    file_txt = open("duplicate.txt", 'w')
    all_file_list = [ v for k, v in file_txt.items()]
    for each in all_file_list:
        if len(each) > 2:
            file_txt.write("---------------\n")
            for i in each:
                str1 = i + "\n"
                file_txt.write(str1)
    file_txt.close()


def get_drivers():
    response = os.popen("wmic logicaldisk get caption")
    list1 = []
    total_file = []
    t1 = datetime.now()
    for line in response.readlines():
        line = line.strip("\n")
        line = line.strip("\r")
        line = line.strip(" ")
        if (line == "Caption" or line == ""):
            continue
        list1.append(line)
    return list1


def search1(drive, size):
    for root, dir, files in os.walk(drive, topdown=True):
        try:
            for file in files:
                try:
                    if os.access(root, os.X_OK):
                        orig = file
                        file = root + "/" + file
                    if os.access(file, os.F_OK):
                        if os.access(file, os.R_OK):
                            s1 = md5(file, size)
                        dict1[s1].append(file)
                except Exception as e:
                    pass
        except Exception as e:
            pass


def create(size):
    t1 = datetime.now()
    list2 = []
    list1 = get_drivers()
    print "Drives are \n"
    for d in list1:
        print d, " ",
    print "\nCreating Indeax..."
    for each in list1:
        process1 = Thread(target=search1, args=(each, size))
        process1.start()
        list2.append(process1)

    for t in list2:
        t.join()

    print len(dict1)
    pickle_file = open("mohit.dup1", "w")
    cPickle.dump(dict1, pickle_file)
    pickle_file.close()
    t2 = datetime.now()
    total = t2 - t1
    print "Time taken to create", total



def file_open():
    pickle_file = open("mohit.dup1", "r")
    file_dict = cPickle.load(pickle_file)
    pickle_file.close()
    return file_dict


def file_search(file_name):
    t1 = datetime.now()
    try:
        file_dict = file_open()
    except IOError:
        create()
        file_dict = file_open()
    except Exception as e:
        print e
        sys.exit()
    file_name1 = file_name.rsplit("\\", 1)
    os.chdir(file_name[0])

    file_to_be_searched = file_name[1]
    if os.access(file_name, os.F_OK):
        if os.access(file_name, os.R_OK):
            sign = md5(file_to_be_searched)
            files = file_dict.get(sign, None)
            if files:
                print "File(s) are"
                files.sort()
                for index, item in enumerate(files):
                    print index+1, " ", item
                    print "--------------------"
            else:
                print "File is not present or accessible"
    t2 = datetime.now()
    total = t2 - t1
    print "Time taken to search ", total




def main():
