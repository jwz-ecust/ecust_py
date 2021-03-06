import pandas as pd
unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table('users.dat',sep='::',header=None,names=unames,engine='python')

rnames = ['user_id','movie_id','rating','timestamp']
ratings = pd.read_table('ratings.dat',sep="::",header=None,names=rnames,engine='python')

mnames = ['movie_id','title','genres']
movies = pd.read_table('movies.dat',sep="::",header=None,names=mnames,engine='python')

