###########################################
###Designer:山川
###Date    :2021-06-16
###Purpose :データベース初期化プログラム
###########################################
import sqlite3
import os

if not os.path.exists("db"):
    os.makedirs("db")

if os.path.exists("db/plans.db"):
    os.remove("db/plans.db")
if os.path.exists("db/tasks.db"):
    os.remove("db/tasks.db")
if os.path.exists("db/users.db"):
    os.remove("db/users.db")


try:
    # 予定データベース作成(userID,start,end,title,planID)
    conn = sqlite3.connect("db/plans.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE plans(userID STRING,start STRING, end STRING,title STRING,planID STRING PRIMARY KEY)"
    )
    conn.commit()
    conn.close()

    # 課題データベース作成(userID,due,need,title,taskID)
    conn = sqlite3.connect("db/tasks.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE tasks(userID STRING,due STRING, need STRING,title STRING,taskID STRING PRIMARY KEY)"
    )
    conn.commit()
    conn.close()

    # ユーザ情報データベース作成(userID,password)
    conn = sqlite3.connect("db/users.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE users(userID STRING PRIMARY KEY,password STRING)")
    conn.commit()
    conn.close()

except sqlite3.Error as err:
    print("error:", err)
