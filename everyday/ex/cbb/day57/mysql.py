import MySQLdb


conn = MySQLdb.connect(host="localhost",user="root",passwd="Cbbzjw140308",db="mysql")

cursor = conn.cursor()

n = cursor.execute(sql,param)