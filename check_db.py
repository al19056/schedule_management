import sqlite3

plansdb = sqlite3.connect("db/plans.db")
taskdb = sqlite3.connect("db/tasks.db")

plan = plansdb.cursor()
task = taskdb.cursor()

print("plans")
plan.execute("SELECT * FROM plans")
print(plan.fetchall())
print("\n\n\ntasks")
task.execute("SELECT * FROM tasks")
print(task.fetchall())

plan.close()
task.close()
plansdb.close()
taskdb.close()
