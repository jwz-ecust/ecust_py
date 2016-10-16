import pickle

class AthleteList(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

print AthleteList('zjw','cbb',[1,2,3])

def get_coach_data(file):
    try:
        with open(file) as f:
            data = f.readline()
            temp1 = data.strip().split(',')
            return AthleteList(temp1.pop(0),temp1.pop(0),temp1)
    except IOError as ioerr:
        print "File error" + str(ioerr)
        return None

def put_to_strore(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name]=ath
    try:
        with open('athletes.pickle','wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as ioerror:
        print "File error (put_and_store):" + str(ioerror)
    return all_athletes

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle','rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print "File error (get from store):" + str(ioerr)
    return all_athletes


the_file = ['ss.txt']
data = put_to_strore(the_file)

print data

# for each_athlete in data:
#     print data[each_athlete].name + ' '+ data[each_athlete].dob


