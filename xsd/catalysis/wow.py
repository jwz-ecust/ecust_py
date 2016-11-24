import os
import shutil

work_dir = '/home/users/jwzhang/machine-learning-data/NiP-ads/work'
save_file = work_dir + '/ss'

dirs = os.listdir(work_dir)
with open(save_file, 'wa') as fuck:
    for i in dirs:
        if i.startswith('USPEX') and not i.endswith('108'):
            slab_path = work_dir + '/' + i
            dos_path = work_dir + '/' + i + '/dos_cal/step1'
            if not os.path.exists(os.path.join(dos_path, 'POSCAR')):
                fuck.write(dos_path + '\n')
                shutil.copy(os.path.join(slab_path, 'CONTCAR'), dos_path)
