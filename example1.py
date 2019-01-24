import postgresql

db = postgresql.open("pq://postgres:G24O02d24230303@127.0.0.1:5432/my_db")
get_emp_with_salary_lt = db.prepare("SELECT emp_name FROM emp WHERE emp_salary < $1")

with db.xact():
    for row in get_weather_with_family_lt:
        print(row)

