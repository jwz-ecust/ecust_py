import os  # load the library module
directory = '/Users/zhangjiawei/Onedrive'  # set the vriable directory and all subdirectories and display the size
dir_size = 0  #set the size to zero


fsizedicr = {'Bits':1,'KB':float(1)/1024,'MB':float(1)/(1024*1024),'GB':float(1)/(1024*1024*1024)}


for (path,dirs,files) in os.walk(directory):  # walk through all the directories, for each iteration,os.walk returns the folders,subfolders and files in the dir.
    for file in files:   # get all the files
        filename = os.path.join(path,file)
        dir_size += os.path.getsize(filename)  # add the size of each file in the root dir to get the total size

for key in fsizedicr:   #iterating through the dictionary
    print "Folder Size: ",str(round(fsizedicr[key]*dir_size,2)),key #round function example:  round(4.2384,2) ==> 4.23
