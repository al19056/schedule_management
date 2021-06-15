"""***********************************************
Designer:荒井*** 
Date:2021.6.1*** 
Purpose:課題処理部モジュール
************************************************"""

def taskQuery(userID,orderData)
    """
    機能概要    :日付の指定を受け取ったときに,その日付の課題の情報を要求し,リスト形式で返す.
    引数        :orderData(str)
                :userID(str)



    戻り値



    """
    newList=C6.taskQuerySub(userID,orderData)
    return newList

def taskEdit(userID,due,need,title,taskID)
    if taskID is None:
        a=1    #追加
        newTaskID=C6.taskEditSub(userID,due,need,title,taskID)
        if len(due)!=16 or need>1000 or len(title)>256 :
            return "failed"
        else: 
            return newTaskID
    elif due is None:
        a=2    #削除
        newTaskID=C6.taskEditSub(userID,due,need,title,taskID)
        return newTaskID
    else:
        a=3    #更新
        newTaskID=C6.taskEditSub(userID,due,need,title,taskID)
        if len(due)!=16 or need>1000 or len(title)>256 :
            return "failed"
        else: 
            return newTaskID

def taskQueryMany(userID,orderData)
    newList=C6.taskQueryManySub(userID,orderData)
    return newList

def taskQueryAll(userID)
    newList=C6.taskQueryAllSub(userID)
    return newList