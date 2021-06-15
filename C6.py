/***********************************************
Designer:荒井*** 
Date:2021.6.1*** 
Purpose:課題情報管理部モジュール
************************************************/

from app import taskConn
import sqlite3
import uuid


def taskQuerySub(userID,orderData)
    cur=taskConn.Cursor()
    cur.execute('SELECT * FROM task.db WHERE orderDate='+str(due[0:10])+'AND userID='+str(userID))
    tempList=cur.fetchall()
    
    #戻り値のリストへ指定された順番に代入
    newList=[[]]
    for x in range(len(tempList)):
        newList.append=[{"due":tempList[x][1], "need":tempList[x][2], "title":tempList[x][3], "taskID":tempList[x][4]}]
    cur.close()
    
    return newList

def taskEditSub(userID,due,need,title,taskID)
    if a=1:
        newTaskID=str(uuid.uuid4())

        cur=taskConn.Cursor()
        cur.execute('INSERT INTO task.db values('+str(userID)+','+str(due)+','+str(need)+','+str(title)+','+str(newTaskID)+')')
        cur.close()

        return newTaskID

    elif a=2:
        newTaskID=taskID

        cur=taskConn.Cursor()
        cur.execute('DELETE FROM task.db WHERE taskID='+str(newTaskID)+'AND userID='+str(userID))
        cur.close()

        return newTaskID

    else:
        newDue=due
        newNeed=need
        newTitle=title
        newTaskID=taskID

        cur=taskConn.Cursor()
        cur.execute('UPDATE task.db SET due='+str(newDue)+',need='+str(newNeed)+',title='+str(newTitle)+ 'WHERE taskID='+str(newTaskID))
        cur.close()

        return newTaskID

def taskQueryManySub(userID,orderData)
    cur=taskConn.Cursor()
    cur.execute('SELECT * FROM task.db WHERE orderDate>='+str(due[0:10])+'AND userID='+str(userID))
    tempList=cur.fetchall()
    
    #戻り値のリストへ指定された順番に代入
    newList=[[]]
    for x in range(len(tempList)):
        newList.append=[{"due":tempList[x][1], "need":tempList[x][2], "title":tempList[x][3], "taskID":tempList[x][4]}]
    cur.close()
    
    return newList


def taskQueryAllSub(userID)
    cur=taskConn.Cursor()
    cur.execute('SELECT * FROM task.db WHERE userID='+str(userID))
    tempList=cur.fetchall()
    
    #戻り値のリストへ指定された順番に代入
    newList=[[]]
    for x in range(len(tempList)):
        newList.append=[{"due":tempList[x][1], "need":tempList[x][2], "title":tempList[x][3], "taskID":tempList[x][4]}]
    cur.close()
    
    return newList