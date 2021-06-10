import C2
import C3
import C4
from flask import redirect, session, url_for

#########################################
###***Designer:山川
###***Date:2021.6.10
###***Purpose:ログイン要求モジュール
#########################################
def requestLogin(userID, password):
    """
    C2認証処理部にログインを要求をし、結果によって画面遷移やCookieへの値の追加を行う

      引数:
        userID   (str):W1ログイン画面からPOSTされたemailフィールド
        password (str):W1ログイン画面からPOSTされたpasswordフィールド

      戻り値:
        失敗時:
          'failed':W1ログイン画面で再入力要求アラートを表示

        成功時:
          homeへリダイレクトし、W2初期画面を表示する
    """
    result = C2.AuthenticationProcessing(userID, password)
    # ログイン失敗
    if result == 0:
        return "failed"
    # ログイン成功
    else:
        session["userID"] = userID
        session["password"] = password
        session["status"] = "True"
        return redirect(url_for("home"))


#########################################
###***Designer:山川
###***Date:2021.6.10
###***Purpose:予定情報問い合わせモジュール
#########################################
def planQuery(userID, orderDate):
    """
    C3予定処理部に予定情報の要求を行い、結果を返す

      引数:
        orderDate (str):要求年月日 YYYY-MM-DDの形式

      戻り値:
        dataList (list):予定情報の入ったリスト(予定情報は辞書形式)
        例:[{"start":"2021-06-10T12:00",　"end":"2021-06-10T15:00",　"title":"宿題",　"planID":"uqwpruedfqer"},{"start":"2021-...}]
    """
    dataList = C3.planOrder(userID, orderDate)
    return dataList


#########################################
###***Designer:山川
###***Date:2021.6.10
###***Purpose:予定情報更新モジュール
#########################################
def planEdit(userID, start, end, title, planID):
    """
    C3予定処理部に予定情報の更新要求を行い、結果を返す

      引数:
        userID (str):ユーザのID
        start  (str):予定の開始時刻
        end    (str):予定の終了時刻
        title  (str):予定の名称
        planID (str):編集する予定のID 予定の追加時は''

      戻り値:
        失敗時:
          'failed'
        成功時:
          削除:'success del'
          更新:'success update'
          追加:newID C3から返された新たに作成された予定ID
    """
    newID = C3.planEdit(userID, start, end, title, planID)
    # 失敗時
    if newID == "failed":
        return "failed"
    # 成功時(削除)
    elif start == "":
        return "success del"
    # 成功時(追加)
    elif planID == "":
        return newID
    # 成功時(更新)
    else:
        return "success update"


#########################################
###***Designer:山川
###***Date:2021.6.10
###***Purpose:課題情報問い合わせモジュール
#########################################
def taskQuery(userID, orderDate):
    """
    C4課題処理部に課題情報の要求を行い、結果を返す

      引数:
        orderDate (str):要求年月日 YYYY-MM-DDの形式

      戻り値:
        dataList (list):課題情報の入ったリスト(課題情報は辞書形式)
        例:[{"due":"2021-06-10T12:00",　"need":"7",　"title":"宿題",　"taskID":"uqwpruedfqer"},{"due":"2021-...}]
    """
    dataList = C4.taskOrder(userID, orderDate)
    return dataList


#########################################
###***Designer:山川
###***Date:2021.6.10
###***Purpose:課題情報更新モジュール
#########################################
def taskEdit(userID, due, need, title, taskID):
    """
    C4課題処理部に課題情報の更新要求を行い、結果を返す

      引数:
        userID (str):ユーザのID
        due    (str):課題の締切時刻
        need   (str):課題の必要時間
        title  (str):課題の名称
        taskID (str):編集する課題のID 課題の追加時は''

      戻り値:
        失敗時:
          'failed'
        成功時:
          削除:'success del'
          更新:'success update'
          追加:newID C4から返された新たに作成された予定ID
    """
    newID = C4.planEdit(userID, due, need, title, taskID)
    # 失敗時
    if newID == "failed":
        return "failed"
    # 成功時(削除)
    elif due == "":
        return "success del"
    # 成功時(追加)
    elif taskID == "":
        return newID
    # 成功時(更新)
    else:
        return "success update"
