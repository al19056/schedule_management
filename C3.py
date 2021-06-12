'''************************************************************************
***Designer :原田
***Date     :2021.6.5
***Purpose  :予定処理プログラム
************************************************************************'''


def planQuery(userID,orderDate):
    '''
    Function Name:planQuery
    Designer     :原田
    Date         :2021.6.5
    Function     :指定日の予定の情報を要求する
    Return       :関数の戻り値(planList or "Failed")   --指定日の予定のリスト
    '''
    return C5.planSearch(orderDate)




def planEdit(userID,start,end,title,planID):
    '''
    Function Name:planEdit
    Designer     :原田
    Date         :2021.6.5
    Function     :予定の編集情報を受け取り,その編集情報の更新要求をする
    Return       :関数の戻り値(planID or "Failed")     --予定ID
    '''
    if(planID is None):
        return C5.planInsert(userID,start,end,title) #追加
    
    elif(title is None):
        return C5.planDelete(userID,planID) #削除
    else:
        return C5.planUpdate(userID,start,end,title,planID) #更新




def planQueryMany(userID,orderDate):
    '''
    Function Name:planQueryMany
    Designer     :原田
    Date         :2021.6.12
    Function     :指定日以降の予定データをリスト形式で返す
    Return       :関数の戻り値(planListMany or "Failed")   --指定日以降の予定のリスト
    '''
    return C5.planSearchMany(orderDate,userID)

