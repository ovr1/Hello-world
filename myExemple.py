import postgresql
file_name = 'tablWeather.txt'

db = postgresql.open("pq://postgres:G24O02d24230303@192.168.0.13:5432/my_db")

tablWeather = db.prepare("select * from weather")

print('TablWeather :')
with db.xact():
    with open(file_name,'w', encoding = 'UTF-8') as f:
        for row in tablWeather:
            f.write(str(row)+'\n')

with open(file_name, 'r', encoding='UTF-8') as file:
    tablWeather = file.readlines()
    for taple in tablWeather:
        print(taple.rstrip())


