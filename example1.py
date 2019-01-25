import postgresql
file_name = 'tablStudent.txt'

db = postgresql.open("pq://postgres:G24O02d24230303@127.0.0.1:5432/my_db")
tablStudent = db.prepare("select * from tstudent")

print('TablStudent :')
with db.xact():
        with open(file_name,'w', encoding = 'UTF-8') as f:
            for row in tablStudent:
                f.write(str(row)+'\n')

with open(file_name, 'r', encoding='UTF-8') as file:
    tablStudent = file.readlines()
    for row in tablStudent:
        print(row.rstrip())

