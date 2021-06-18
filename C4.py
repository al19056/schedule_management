#####################################################
###***Designer:荒井
###***Date:2021.6.18
###***Purpose:C4コンポーネント
#####################################################

import C6

def taskQuery(userID,orderData):
    """
    機能概要    :日付の指定を受け取ったときに,その日付の課題の情報を要求し,リスト形式で返す.
    引数        :
        userID(str)     :ユーザID
        orderData(str)  :指定された日付
    戻り値      
        失敗:
            文字列"failed"
        成功:
            newList(list):指定日の課題リスト
    """
    newList=C6.taskQuerySub(userID,orderData)
    if newList==[[]]:
        return "failed"
    else:
        return newList

def taskEdit(userID,due,need,title,taskID):
    """
    機能概要    :課題の編集情報を受け取ったときに,その編集情報の更新の要求をし,更新後の課題IDを返す.
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
            newTaskID   :更新後の課題ID
    """
    if taskID is None:
        a=1    #追加
        newTaskID=C6.taskEditSub(userID,due,need,title,taskID)
        if len(due)!=16 or len(need)>3 or len(title)>256 :
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
        if len(due)!=16 or len(need)>3 or len(title)>256 :
            return "failed"
        else: 
            return newTaskID

def taskQueryMany(userID,orderData):
    """
    機能概要    :日付の指定を受け取ったときに,その日付以降の課題の情報を要求し,リスト形式で返す.
    引数        :
        userID(str)     :ユーザID
        orderData(str)  :指定された日付
    戻り値      
        失敗:
            文字列"failed"
        成功:
            newList(list):指定日以降の課題リスト
    """
    newList=C6.taskQueryManySub(userID,orderData)
    if newList==[[]]:
        return "failed"
    else:
        return newList

def taskQueryAll(userID):
    """
    機能概要    :登録されている全ての課題の情報を要求し,リスト形式で返す.
    引数        :
        userID(str)     :ユーザID
    戻り値      
        失敗:
            文字列"failed"
        成功:
            newList(list):ユーザの全ての課題リスト
    """
    newList=C6.taskQueryAllSub(userID)
    if newList==[[]]:
        return "failed"
    else:
        return newList