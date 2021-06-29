'''************************************************************************
***Designer :原田
***Date     :2021.6.5
***Purpose  :予定情報管理プログラム
************************************************************************'''

import uuid
import sqlite3



def planSearch(userIDArg,orderDateArg):
    '''
    機能概要    :指定日の予定を検索し,リスト形式で返す
    引数        :userIDArg(str)        :ユーザID
                :orderDateArg(str)  :指定された日付

    戻り値      :planList(List) :指定日の予定のリスト(成功時)
                :"failed"       :文字列"failed"(失敗時)
    '''
    planConn = sqlite3.connect("db/plans.db")

    cur=planConn.cursor() 
    
    #plansテーブルから指定された日付の予定の検索
    cur.execute('SELECT * FROM plans WHERE userID=? AND start like ?',[userIDArg,orderDateArg+'T'+'%'])
    tempList=cur.fetchall()
    
    #戻り値のリストへ指定された順番に代入
    planList=[]
    keys=['start','end','title','planID']
    for x in range(len(tempList)):
        values=[tempList[x][1],tempList[x][2],tempList[x][3],tempList[x][4]]
        planList.append(dict(zip(keys,values)))
    
    cur.close()
    planConn.close()


    return planList




def planInsert(userIDArg,startArg,endArg,titleArg):
    '''
    機能概要    :予定の編集情報を受け取り,その日の予定の情報をデータベースに追加する
    引数        :userIDArg(str)        :ユーザID
                :startArg(str)      :予定の開始日時
                :endArg(str)        :予定の終了日時
                :titleArg(str)      :予定の名称

    戻り値      :planIDArg(str)    :予定ID(成功時)
                :"failed"          :文字列"failed"(失敗時)
    '''
    planIDArg=str(uuid.uuid4()) #planIDを新たに作成

    planConn = sqlite3.connect("db/plans.db")

    cur=planConn.cursor() 

    #plansテーブルへ指定された予定の追加
    cur.execute('INSERT INTO plans values(?,?,?,?,?)',[userIDArg,startArg,endArg,titleArg,planIDArg])
    
    #エラー確認用にtempListへ代入
    cur.execute('SELECT * FROM plans WHERE userID=? AND planID=?',[userIDArg,planIDArg])
    tempList=cur.fetchall()

    planConn.commit()

    cur.close()
    planConn.close()

    

    return planIDArg
    



def planUpdate(userIDArg,startArg,endArg,titleArg,planIDArg):
    '''
    機能概要    :予定の編集情報を受け取り,その日の予定の情報を更新する
    引数        :userIDArg(str)        :ユーザID
                :startArg(str)      :予定の開始日時
                :endArg(str)        :予定の終了日時
                :titleArg(str)      :予定の名称
                :planIDArg(str)        :予定ID

    戻り値      :planIDArg(str)    :予定ID(成功時)
                :"failed"          :文字列"failed"(失敗時)
    ''' 
    planConn = sqlite3.connect("db/plans.db")

    cur=planConn.cursor() 

    #plansテーブルへ指定された予定の更新
    cur.execute('UPDATE plans SET start=? ,end=? ,title=? WHERE planID=?',[startArg,endArg,titleArg,planIDArg])    
    
    #エラー確認用にtempListへ代入
    cur.execute('SELECT * FROM plans WHERE planID=? AND userID=?',[planIDArg,userIDArg])
    tempList=cur.fetchall()

    planConn.commit()

    cur.close()
    planConn.close()

    
    return planIDArg




def planDelete(userIDArg,planIDArg):
    '''
    機能概要    :指定された予定IDを持つ予定の情報をデータベースから削除する
    引数        :userIDArg(str)    :ユーザID
                :planIDArg(str)    :予定ID

    戻り値      :planIDArg(str)    :予定ID(成功時)
                :"failed"          :文字列"failed"(失敗時)
    ''' 
    planConn = sqlite3.connect("db/plans.db")

    cur=planConn.cursor() 

    #plansテーブルの指定された予定の削除
    cur.execute('DELETE FROM plans WHERE planID=? AND userID=?',[planIDArg,userIDArg])
    
    #エラー確認用にtempListへ代入
    cur.execute('SELECT * FROM plans WHERE planID=? AND userID=?',[planIDArg,userIDArg])
    tempList=cur.fetchall()

    planConn.commit()
    
    cur.close()
    planConn.close()

    
    
    return "failed" #エラーの場合




def planSearchMany(userIDArg,orderDate):
    '''
    機能概要    :指定日以降の予定データをリスト形式で返す
    引数        :userIDArg(str)    :ユーザID
                :orderDate(str) :指定された日付

    戻り値      :planListMany(List) :指定日以降の予定データのリスト(成功時)
                :"failed"           :文字列"failed"(失敗時)
    ''' 
    planConn = sqlite3.connect("db/plans.db")

    cur=planConn.cursor() 

    #plansテーブルの指定日以降の予定の検索
    cur.execute('SELECT * FROM plans WHERE start>=? AND userID=?',[orderDate,userIDArg])
    tempList=cur.fetchall()

    #戻り値のリストへ指定された順番に代入
    planListMany=[]
    keys=['start','end','title','planID']
    for x in range(len(tempList)):
        values=[tempList[x][1],tempList[x][2],tempList[x][3],tempList[x][4]]
        planListMany.append(dict(zip(keys,values)))
    
    cur.close()
    planConn.close()


    return planListMany




def planSearchAll(userIDArg):
    '''
    機能概要    :ユーザのすべての予定データをリスト形式で返す
    引数        :userIDArg(str)    :ユーザID

    戻り値      :planListAll(List) :ユーザのすべての予定データのリスト(成功時)
                :"failed"          :文字列"failed"(失敗時)
    ''' 
    planConn = sqlite3.connect("db/plans.db")

    cur=planConn.cursor() 

    #plansテーブルの指定されたユーザのすべての予定の検索
    cur.execute('SELECT * FROM plans WHERE userID=?',[userIDArg])
    tempList=cur.fetchall()
    
    #戻り値のリストへ指定された順番に代入
    planListAll=[]
    keys=['start','end','title','planID']
    for x in range(len(tempList)):
        values=[tempList[x][1],tempList[x][2],tempList[x][3],tempList[x][4]]
        planListAll.append(dict(zip(keys,values)))

    cur.close()
    planConn.close()


    return planListAll
