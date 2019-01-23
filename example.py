import postgresql

db = postgresql.open("pq://postgres:G24O02d24230303@127.0.0.1:5432/postgres")
db.execute("CREATE TABLE emp (emp_name text PRIMARY KEY, emp_salary numeric)")

make_emp = db.prepare("INSERT INTO emp VALUES ($1, $2)")
raise_emp = db.prepare("UPDATE emp SET emp_salary = emp_salary + $2 WHERE emp_name = $1")
get_emp_with_salary_lt = db.prepare("SELECT emp_name FROM emp WHERE emp_salary < $1")

with db.xact():
    make_emp("John Doe", 150)
    make_emp("Jane Doe", 150)
    make_emp("Andrew Doe", 55)
    make_emp("Susan Doe", 60)

with db.xact():
    for row in get_emp_with_salary_lt(125):
        print(row["emp_name"])
   pi     raise_emp(row["emp_name"], 10)