'''************************************************************************
***Designer :原田
***Date     :2021.6.5
***Purpose  :予定情報管理プログラム
************************************************************************'''

from app import planConn
import sqlite3



def planSearch(userID,orderDateArg):
    '''
    機能概要    :指定日の予定を検索し,リスト形式で返す
    引数        :userID(str)        :ユーザID
                :orderDateArg(str)  :指定された日付

    戻り値      :planList(List) :指定日の予定のリスト(成功時)
                :"Failed"       :文字列"Failed"(失敗時)
    '''
    cur=planConn.Cursor() 
    
    #引数であるuserIDを名前にもつテーブルから予定の検索(未完)
    tempList=cur.execute('SELECT * FROM userID WHERE orderDate=orderDateArg')
    planList=[{"start":tempList[0], "end":tempList[1], "title":tempList[2], "planID":tempList[3]}]
    cur.close()

    if(planList is None): #エラーの場合
        return "Failed"
    else:
        return planList




def planInsert(userID,startArg,endArg,titleArg):
    '''
    機能概要    :予定の編集情報を受け取り,その日の予定の情報をデータベースに追加する
    引数        :userID(str)        :ユーザID
                :startArg(str)      :予定の開始日時
                :endArg(str)        :予定の終了日時
                :titleArg(str)      :予定の名称

    戻り値      :planIDArg(str)    :予定ID(成功時)
                :"Failed"       :文字列"Failed"(失敗時)
    '''
    planIDArg='ID' #planIDを新たに作成
    cur=app.planConn.Cursor() 

    #引数であるuserIDを名前にもつテーブルへ予定の追加(未完)
    cur.execute('INSERT INTO userID values(startArg,endArg,titleArg,titleArg)')
    tempList=cur.execute('SELECT * FROM userID WHERE planID=planIDArg')
    cur.close()

    if(tempList is None):
        return "Failed"
    else:
        return planIDArg
    



def planUpdate(userID,startArg,endArg,titleArg,planIDArg):
    '''
    機能概要    :予定の編集情報を受け取り,その日の予定の情報を更新する
    引数        :userID(str)        :ユーザID
                :startArg(str)      :予定の開始日時
                :endArg(str)        :予定の終了日時
                :titleArg(str)      :予定の名称
                :planIDArg(str)        :予定ID

    戻り値      :planIDArg(str)    :予定ID(成功時)
                :"Failed"       :文字列"Failed"(失敗時)
    ''' 
    cur=app.planConn.Cursor() 

    #引数であるuserIDを名前にもつテーブルの予定の更新(未完)
    cur.execute('UPDATE userID SET start=startArg, end=endArg, title=titleArg WHERE planID=planIDArg')    
    tempList=cur.execute('SELECT * FROM userID WHERE planID=planIDArg')
    cur.close()

    if(tempList is None):
        return "Failed"
    else:
        return planIDArg




def planDelete(userID,planIDArg):
    '''
    機能概要    :指定された予定IDを持つ予定の情報をデータベースから削除する
    引数        :userID(str)    :ユーザID
                :planIDArg(str)    :予定ID

    戻り値      :planIDArg(str)    :予定ID(成功時)
                :"Failed"       :文字列"Failed"(失敗時)
    ''' 
    cur=app.planConn.Cursor() 

    #引数であるuserIDを名前にもつテーブルの予定の削除(未完)
    cur.execute('DELETE FROM userID WHERE planID=planIDArg')
    tempList=cur.execute('SELECT * FROM userID WHERE planID=planIDArg')
    cur.close()

    if(tempList is None):
        return "Failed"
    else:
        return planIDArg




def planSearchMany(userID,orderDate):
    '''
    機能概要    :指定日以降の予定データをリスト形式で返す
    引数        :userID(str)    :ユーザID
                :orderDate(str) :指定された日付

    戻り値      :planListMany(List) :指定日以降の予定データのリスト(成功時)
                :"Failed"           :文字列"Failed"(失敗時)
    ''' 
    cur=app.planConn.Cursor() 

    #引数であるuserIDを名前にもつテーブルの指定日以降の予定の検索(未完)
    tempList=cur.execute('SELECT * FROM userID WHERE start>=orderDate')
    planListMany=[{"start":tempList[0], "end":tempList[1], "title":tempList[2], "planID":tempList[3]}]
    cur.close()

    if(planListMany is None):
        return "Failed"
    else:
        return planListMany


