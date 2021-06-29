import sqlite3
import pprint

plansdb = sqlite3.connect("db/plans.db")
taskdb = sqlite3.connect("db/tasks.db")

plan = plansdb.cursor()
task = taskdb.cursor()

print("plans")
plan.execute("SELECT * FROM plans")
pprint.pprint(plan.fetchall())
print("\n\n\ntasks")
task.execute("SELECT * FROM tasks")
pprint.pprint(task.fetchall())

plan.close()
task.close()
plansdb.close()
taskdb.close()
