'''************************************************************************
***Designer :原田
***Date     :2021.6.5
***Purpose  :予定情報管理プログラム
************************************************************************'''




def planSearch(userID,orderDate):
    '''
    機能概要    :指定日の予定を検索し,リスト形式で返す
    引数        :userID(str)    :ユーザID
                :orderDate(str) :指定された日付
    戻り値      :planList(List) :指定日の予定のリスト(成功時)
                :"Failed"       :文字列"Failed"(失敗時)
    '''
    if(エラー発生):
        return "Failed"
    else:
        #処理
        return planList




def planInsert(userID,start,end,title,planID):
    '''
    機能概要    :予定の編集情報を受け取り,その日の予定の情報をデータベースに追加する
    引数        :userID(str)    :ユーザID
                :start(str)     :予定の開始日時
                :end(str)       :予定の終了日時
                :title(str)     :予定の名称
                :planID(str)    :予定ID

    戻り値      :planID(str)    :予定ID(成功時)
                :"Failed"       :文字列"Failed"(失敗時)
    '''
    if(エラー発生):
        return "Failed"
    else:
        #処理
        return planID
    



def planInsert(userID,start,end,title):
    '''
    機能概要    :予定の編集情報を受け取り,その日の予定の情報を更新する
    引数        :userID(str)    :ユーザID
                :start(str)     :予定の開始日時
                :end(str)       :予定の終了日時
                :title(str)     :予定の名称

    戻り値      :planID(str)    :予定ID(成功時)
                :"Failed"       :文字列"Failed"(失敗時)
    ''' 
    if(エラー発生):
        return "Failed"
    else:
        #処理
        return planID




def planInsert(userID,planID):
    '''
    機能概要    :指定された予定IDを持つ予定の情報をデータベースから削除する
    引数        :userID(str)    :ユーザID
                :planID(str)    :予定ID

    戻り値      :planID(str)    :予定ID(成功時)
                :"Failed"       :文字列"Failed"(失敗時)
    ''' 
    if(エラー発生):
        return "Failed"
    else:
        #処理
        return planID




def planSearchMany(userID,orderDate):
    '''
    機能概要    :指定日以降の予定データをリスト形式で返す
    引数        :userID(str)    :ユーザID
                :orderDate(str) :指定された日付

    戻り値      :planListMany(List) :指定日以降の予定データのリスト(成功時)
                :"Failed"           :文字列"Failed"(失敗時)
    ''' 
    if(エラー発生):
        return "Failed"
    else:
        #処理
        return planListMany








