'''************************************************************************
***Designer :原田
***Date     :2021.6.5
***Purpose  :予定処理プログラム
************************************************************************'''


def planQuery(userID,orderDate):
    '''
    機能概要    :指定日の予定の情報を要求する
    引数        :userID(str)    :ユーザID
                :orderDate(str) :指定された日付

    戻り値      :planSearchの戻り値(planList)   :指定日の予定のリスト(成功時)
                :"Failed"                       :文字列"Failed"(失敗時)
    ''' 
    return C5.planSearch(orderDate)




def planEdit(userID,start,end,title,planID):
    '''
    機能概要    :予定の編集情報を受け取り,その編集情報の更新要求をする
    引数        :userID(str)    :ユーザID
                :start(str)     :予定の開始日時
                :end(str)       :予定の終了日時
                :title(str)     :予定の名称
                :planID(str)    :予定ID

    戻り値      :planInsert or planDelete or planUpdateの戻り値(planID) :予定ID (成功時)
                :"Failed"                                               :文字列"Failed"(失敗時)
    '''
    if(planID is None):
        return C5.planInsert(userID,start,end,title) #追加
    
    elif(title is None):
        return C5.planDelete(userID,planID) #削除
    else:
        return C5.planUpdate(userID,start,end,title,planID) #更新




def planQueryMany(userID,orderDate):
    '''
    機能概要    :指定日以降の予定データをリスト形式で返す
    引数        :userID(str)    :ユーザID
                :orderDate(str) :指定された日付

    戻り値      :planSearchManyの戻り値(planListMany)   :指定日以降の予定のリスト(成功時)
                :"Failed"                               :文字列"Failed"(失敗時)
    '''
    return C5.planSearchMany(orderDate,userID)

