#####################################################
###***Designer:荒井
###***Date:2021.6.18
###***Purpose:C4コンポーネント
#####################################################

import C6

def taskQuery(userID,orderDate):
    """
    機能概要    :日付の指定を受け取ったときに,その日付の課題の情報を要求し,リスト形式で返す.
    引数        :
        userID(str)     :ユーザID
        orderDate(str)  :指定された日付
    戻り値      :   
        newList(list):指定日の課題リスト
    """

    newList=C6.taskQuerySub(userID,orderDate)

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

    #課題の情報を追加
    if taskID == None: #追加時はtaskIDが存在しない
        newTaskID=C6.taskEditSub(userID,due,need,title,taskID)
        return newTaskID

    #課題の情報を削除
    elif due == None: #削除時はdue,need,titleが存在しない
        newTaskID=C6.taskEditSub(userID,due,need,title,taskID)
        return newTaskID

    #課題の情報を変更
    else: 
        newTaskID=C6.taskEditSub(userID,due,need,title,taskID)
        return newTaskID

def taskQueryMany(userID,orderDate):
    """
    機能概要    :日付の指定を受け取ったときに,その日付以降の課題の情報を要求し,リスト形式で返す.
    引数        :
        userID(str)     :ユーザID
        orderDate(str)  :指定された日付
    戻り値      :
        newList(list):指定日以降の課題リスト
    """

    newList=C6.taskQueryManySub(userID,orderDate)

    return newList

def taskQueryAll(userID):
    """
    機能概要    :登録されている全ての課題の情報を要求し,リスト形式で返す.
    引数        :
        userID(str)     :ユーザID
    戻り値      
        newList(list):ユーザの全ての課題リスト
    """
    
    newList=C6.taskQueryAllSub(userID)

    return newList