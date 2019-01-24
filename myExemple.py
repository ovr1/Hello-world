import postgresql
file_name = 'tablWeather.txt'

db = postgresql.open("pq://postgres:G24O02d24230303@127.0.0.1:5432/my_db")

tablWeather = db.prepare("select * from weather")

print('TablWeather :')
with db.xact():
    for row in tablWeather:
        ...

        with open(file_name,'w', encoding = 'UTF-8') as f:
            f.write(str(row))

        with open(file_name, 'r', encoding='UTF-8') as file:
            tablWeather = file.readlines()
            print(tablWeather)


