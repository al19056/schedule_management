#C4.py

/***********************************************
Designer:荒井*** 
Date:2021.6.1*** 
Purpose:課題処理部モジュール
************************************************/

def taskQuery(userID,orderData)
    #課題データの入ったリストが呼び出されている
    newList=C6.taskQuerySub(userID,orderData)
    return newList

def taskEdit(userID,due,need,title,taskID)
    if len(due)!=16 or need>1000 or len(title)>256 :
        return "failed"
    else
        newDue=due
        newNeed=need
        newTitle=title
        newTaskID=taskID
        return newTaskID

    #更新削除処理の時？

def taskQueryMany(userID,orderData)

    return newList
