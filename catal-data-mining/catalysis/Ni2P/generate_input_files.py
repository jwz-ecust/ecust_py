import os
import shutil

work_path = "/home/users/jwzhang/machine-learning-data/Ni2P/work"
poscars_path = "/home/users/jwzhang/machine-learning-data/Ni2P/poscars"
model_path = "/home/users/jwzhang/machine-learning-data/Ni2P/model"
step1_path = "/home/users/jwzhang/machine-learning-data/Ni2P/model/step1"
step2_path = "/home/users/jwzhang/machine-learning-data/Ni2P/model/step2"

poscars = os.listdir(poscars_path)

for name in poscars:
    _name = name.split('_')[0]
    job = os.path.join(work_path, _name)
    job_co = os.path.join(job, "CO")
    job_dos = os.path.join(job, "dos")
    job_step1 = os.path.join(job_dos, 'step1')
    job_step2 = os.path.join(job_dos, 'step2')
    os.mkdir(job)
    os.mkdir(job_co)
    os.mkdir(job_dos)
    os.mkdir(job_step1)
    os.mkdir(job_step2)
    pos_path = os.path.join(poscars_path, name)
    tar_pos = os.path.join(job, 'POSCAR')
    shutil.copy(pos_path, tar_pos)
    input_files = ['INCAR', 'KPOINTS', 'POTCAR', 'vasp.script']
    for i in input_files:
        source = os.path.join(model_path, i)
        target = os.path.join(job, i)
        target_co = os.path.join(job_co, i)
        source_step1 = os.path.join(step1_path, i)
        source_step2 = os.path.join(step2_path, i)
        tar_step1 = os.path.join(job_step1, i)
        tar_step2 = os.path.join(job_step2, i)
        shutil.copy(source, target)
        shutil.copy(source, target_co)
        shutil.copy(source_step1, tar_step1)
        shutil.copy(source_step2, tar_step2)
