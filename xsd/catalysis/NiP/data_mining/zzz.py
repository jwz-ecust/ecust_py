def read_bader(bader_path):
    bader = []
    with open(bader_path) as bd:
        content = bd.readlines()
        for i in content[2:-4]:
            print i.strip().split(" " * 5)[4]


bader_path = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/NiP/data_mining/ACF_1 copy.dat"
read_bader(bader_path)
