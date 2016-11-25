import os

work_dir = '/home/users/jwzhang/machine-learning-data/NiP-ads/work'

dirs = os.listdir(work_dir)
for i in dirs:
    dos_path = work_dir + '/' + i + '/dos_cal/step1'
    if not os.path.exists(os.path.join(dos_path, 'OUTCAR')):
        print 'find', dos_path
