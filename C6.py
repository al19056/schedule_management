#####################################################
###***Designer:荒井
###***Date:2021.6.18
###***Purpose:C6コンポーネント
#####################################################


from app import taskConn
import sqlite3
import uuid


def taskQuerySub(userID,orderData):
    """
    機能概要    :指定日の課題の情報を検索する.

    引数        :
        userID(str)     :ユーザID
        orderData(str)  :指定された日付

    戻り値      
        失敗:
            文字列"failed"

        成功:
            newList(list):指定日の課題リスト
    """

    #課題情報データーベースに登録された課題の検索
    cur=taskConn.Cursor()
    cur.execute('SELECT * FROM tasks WHERE userID=? AND due[0:10]=? ',[userID,orderData])
    tempList=cur.fetchall()
    
    #戻り値のリストに代入
    newList=[[]]
    for x in range(len(tempList)):
        newList.append=[{"due":tempList[x][1], "need":tempList[x][2], "title":tempList[x][3], "taskID":tempList[x][4]}]
    cur.close()
    
    return newList

def taskEditSub(userID,due,need,title,taskID):
    """
    機能概要    :課題の情報を更新する.

    引数        :
        userID(str)     :ユーザID
        due(str)        :課題の締め切り時間
        need(str)       :課題の必要時間
        title(str)      :課題の名称
        taskID(str)     :課題ID

    戻り値      
        失敗:
            文字列"failed"

        成功:
            newTaskID   :新たな課題のID
    """

    #課題の情報を追加
    if taskID == None: 
        newTaskID=str(uuid.uuid4())　#taskIDを乱数を用いて定義

        cur=taskConn.Cursor()
        cur.execute('INSERT INTO tasks values(?,?,?,?,?)'[userID,due,need,title,newTaskID])
        cur.close()

        return newTaskID

    #課題の情報を削除
    elif due == None: 
        newTaskID=taskID

        cur=taskConn.Cursor()
        cur.execute('DELETE FROM tasks WHERE userID=? AND taskID=?',[userID,newTaskID])
        cur.close()

        return newTaskID

    #課題の情報を変更
    else: 
        newTaskID=taskID

        cur=taskConn.Cursor()
        cur.execute('UPDATE tasks SET due=?,need=?,title=? WHERE taskID=?',[due,need,title,newTaskID])
        cur.close()

        return newTaskID

def taskQueryManySub(userID,orderData):
    """
    機能概要    :指定日以降の課題の情報を検索する.

    引数        :
        userID(str)     :ユーザID
        orderData(str)  :指定された日付

    戻り値      
        失敗:
            文字列"failed"

        成功:
            newList(list):指定日の課題リスト
    """

    #課題情報データーベースに登録された課題の検索
    cur=taskConn.Cursor()
    cur.execute('SELECT * FROM tasks WHERE userID=? AND due[0:10]>=? ',[userID,orderData])
    tempList=cur.fetchall()
    
    #戻り値のリストに代入
    newList=[[]]
    for x in range(len(tempList)):
        newList.append=[{"due":tempList[x][1], "need":tempList[x][2], "title":tempList[x][3], "taskID":tempList[x][4]}]
    cur.close()
    
    return newList


def taskQueryAllSub(userID):
    """
    機能概要    :ユーザの登録した全ての課題の情報を検索する.

    引数        :
        userID(str)     :ユーザID

    戻り値      
        失敗:
            文字列"failed"

        成功:
            newList(list):指定日の課題リスト
    """

    #課題情報データーベースに登録された課題の検索
    cur=taskConn.Cursor()
    cur.execute('SELECT * FROM tasks WHERE userID=?',[userID])
    tempList=cur.fetchall()
    
    #戻り値のリストに代入
    newList=[[]]
    for x in range(len(tempList)):
        newList.append=[{"due":tempList[x][1], "need":tempList[x][2], "title":tempList[x][3], "taskID":tempList[x][4]}]
    cur.close()

    return newList