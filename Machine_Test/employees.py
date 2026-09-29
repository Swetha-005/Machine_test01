import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="company"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM employees")
for i in employees:
    print(i)
sql = "INSERT INTO employees (emp_id, name, department, salary) VALUES (%s, %s, %s, %s)"
values = (6, "swetha", "cs", 55000)
cursor.execute(sql, values)
db.commit()
sql = "UPDATE employees SET salary = %s WHERE emp_id = %s"
values = (60000, 6)
cursor.execute(sql, values)
db.commit()
sql = "DELETE FROM employees WHERE emp_id = %s"
cursor.execute(sql, (6,))
db.commit()
cursor.execute("SELECT * FROM employees WHERE salary > %s", (50000,))
cursor.close()
db.close()
