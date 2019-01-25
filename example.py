import postgresql

db = postgresql.open("pq://postgres:G24O02d24230303@127.0.0.1:5432/my_")
db.execute("CREATE TABLE test (test_name text PRIMARY KEY, test_salary numeric)")

make_test = db.prepare("INSERT INTO test VALUES ($1, $2)")
raise_test = db.prepare("UPDATE test SET test_salary = test_salary + $2 WHERE test_name = $1")
get_test_with_salary_lt = db.prepare("SELECT test_name FROM test WHERE test_salary < $1")

with db.xact():
    make_test("John Doe", 150)
    make_test("Jane Doe", 150)
    make_test("Andrew Doe", 55)
    make_test("Susan Doe", 60)

with db.xact():
    for row in get_emp_with_salary_lt(125):
        print(row["emp_name"])
        raise_emp(row["emp_name"], 10)