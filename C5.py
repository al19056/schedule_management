'''************************************************************************
***Designer :原田
***Date     :2021.6.5
***Purpose  :予定情報管理プログラム
************************************************************************'''

from app import planConn
import uuid
import sqlite3



def planSearch(userIDArg,orderDateArg):
    '''
    機能概要    :指定日の予定を検索し,リスト形式で返す
    引数        :userIDArg(str)        :ユーザID
                :orderDateArg(str)  :指定された日付

    戻り値      :planList(List) :指定日の予定のリスト(成功時)
                :"Failed"       :文字列"Failed"(失敗時)
    '''
    cur=planConn.Cursor() 
    
    #plan.dbテーブルから指定された予定の検索
    cur.execute('SELECT * FROM plan.db WHERE useID='+str(userIDArg)+'AND orderDate='+str(orderDateArg))
    tempList=cur.fetchall()
    
    #戻り値のリストへ指定された順番に代入
    planList=[]
    keys=['start','end','title','planID']
    for x in range(len(tempList)):
        values=[tempList[x][1],tempList[x][2],tempList[x][3],tempList[x][4]]
        planList.append(dict(zip(keys,values)))
    
    cur.close()

    if(planList is None): #エラーの場合
        return "Failed"
    else:
        return planList




def planInsert(userIDArg,startArg,endArg,titleArg):
    '''
    機能概要    :予定の編集情報を受け取り,その日の予定の情報をデータベースに追加する
    引数        :userIDArg(str)        :ユーザID
                :startArg(str)      :予定の開始日時
                :endArg(str)        :予定の終了日時
                :titleArg(str)      :予定の名称

    戻り値      :planIDArg(str)    :予定ID(成功時)
                :"Failed"       :文字列"Failed"(失敗時)
    '''
    planIDArg=str(uuid.uuid4()) #planIDを新たに作成

    cur=planConn.Cursor() 

    #plan.dbテーブルへ指定された予定の追加
    cur.execute('INSERT INTO plan.db values('+str(userIDArg)+','+str(startArg)+','+str(endArg)+','+str(titleArg)+','+str(planIDArg)+')')
    
    #エラー確認用にtempListへ代入
    cur.execute('SELECT * FROM plan.db WHERE userID='+str(userIDArg)+' AND planID='+str(planIDArg))
    tempList=cur.fetchall()

    cur.close()

    if(tempList is None): #エラーの場合
        return "Failed"
    else:
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
                :"Failed"       :文字列"Failed"(失敗時)
    ''' 
    cur=planConn.Cursor() 

    #plan.dbテーブルへ指定された予定の更新
    cur.execute('UPDATE plan.db SET start='+str(startArg)+',end='+str(endArg)+',title='+str(titleArg)+ 'WHERE planID='+str(planIDArg))    
    
    #エラー確認用にtempListへ代入
    cur.execute('SELECT * FROM plan.db WHERE planID='+str(planIDArg)+'AND userID='+str(userIDArg))
    tempList=cur.fetchall()

    cur.close()

    if(tempList is None): #エラーの場合
        return "Failed"
    else:
        return planIDArg




def planDelete(userIDArg,planIDArg):
    '''
    機能概要    :指定された予定IDを持つ予定の情報をデータベースから削除する
    引数        :userIDArg(str)    :ユーザID
                :planIDArg(str)    :予定ID

    戻り値      :planIDArg(str)    :予定ID(成功時)
                :"Failed"       :文字列"Failed"(失敗時)
    ''' 
    cur=planConn.Cursor() 

    #plan.dbテーブルの指定された予定の削除
    cur.execute('DELETE FROM plan.db WHERE planID='+str(planIDArg)+'AND userID='+str(userIDArg))
    
    #エラー確認用にtempListへ代入
    cur.execute('SELECT * FROM plan.db WHERE planID='+str(planIDArg)+'AND userID='+str(userIDArg))
    tempList=cur.fetchall()

    cur.close()

    if(tempList is None):
        return planIDArg
    else:
        return "Failed" #エラーの場合




def planSearchMany(userIDArg,orderDate):
    '''
    機能概要    :指定日以降の予定データをリスト形式で返す
    引数        :userIDArg(str)    :ユーザID
                :orderDate(str) :指定された日付

    戻り値      :planListMany(List) :指定日以降の予定データのリスト(成功時)
                :"Failed"           :文字列"Failed"(失敗時)
    ''' 
    cur=planConn.Cursor() 

    #plan.dbテーブルの指定日以降の予定の検索
    cur.executemany('SELECT * FROM plan.db WHERE start>='+str(orderDate)+'AND userID='+str(userIDArg))
    tempList=cur.fetchall()

    #戻り値のリストへ指定された順番に代入
    planListMany=[]
    keys=['start','end','title','planID']
    for x in range(len(tempList)):
        values=[tempList[x][1],tempList[x][2],tempList[x][3],tempList[x][4]]
        planListMany.append(dict(zip(keys,values)))
    cur.close()

    if(planListMany is None): #エラーの場合
        return "Failed"
    else:
        return planListMany




def planSearchAll(userIDArg):
    '''
    機能概要    :ユーザのすべての予定データをリスト形式で返す
    引数        :userIDArg(str)    :ユーザID

    戻り値      :planListAll(List) :ユーザのすべての予定データのリスト(成功時)
                :"Failed"           :文字列"Failed"(失敗時)
    ''' 
    cur=planConn.Cursor() 

    #plan.dbテーブルの指定されたユーザのすべての予定の検索
    cur.executemany('SELECT * FROM plan.db WHERE userID='+str(userIDArg))
    tempList=cur.fetchall()
    
    #戻り値のリストへ指定された順番に代入
    planListAll=[]
    keys=['start','end','title','planID']
    for x in range(len(tempList)):
        values=[tempList[x][1],tempList[x][2],tempList[x][3],tempList[x][4]]
        planListAll.append(dict(zip(keys,values)))

    cur.close()

    if(planListAll is None): #エラーの場合
        return "Failed"
    else:
        return planListAll
