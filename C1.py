#####################################################
###***Designer:山川
###***Date:2021.6.11
###***Purpose:C1コンポーネント(サーバサイドの関数のみ)
#####################################################
import testC2 as C2
import testC3 as C3
import testC4 as C4

# import C2
# import C3
# import C4
from flask import redirect, session, url_for
import datetime
import hashlib

# M1-1 ログイン処理モジュール
def requestLogin(userID, password):
    """
    機能概要:
        C2認証処理部にログインを要求をし、結果によって画面遷移やCookieへの値の追加を行う

    引数:
        userID   (str):W1ログイン画面からPOSTされたemailフィールド
        password (str):W1ログイン画面からPOSTされたpasswordフィールド

    戻り値:
        失敗時:
            'failed':W1ログイン画面で再入力要求アラートを表示

        成功時:
            Cookieへログイン情報を保存
            homeへリダイレクトし、W2初期画面を表示する
    """
    hashPassword = hashlib.sha256(password.encode()).hexdigest()  # passwordのハッシュ化
    result = C2.authenticationProcessing(userID, hashPassword)
    # ログイン失敗
    if result == "failed":
        return "failed"
    # ログイン成功
    else:
        session["userID"] = userID
        session["password"] = hashPassword
        session["status"] = "True"
        return redirect(url_for("W2"))


# M1-2 ユーザ登録処理モジュール
def requestAddUser(userID, password):
    """
    機能概要:
        C2認証処理部にユーザ登録を要求をし、結果によって画面遷移やCookieへの値の追加を行う

    引数:
        userID   (str):W1ログイン画面からPOSTされたemailフィールド
        password (str):W1ログイン画面からPOSTされたpasswordフィールド

    戻り値:
        失敗時:
            'failed':W1ログイン画面で再入力要求アラートを表示

        成功時:
            Cookieへログイン情報を保存
            homeへリダイレクトし、W2初期画面を表示する
    """
    hashPassword = hashlib.sha256(password.encode()).hexdigest()  # passwordのハッシュ化
    result = C2.addUser(userID, hashPassword)
    if result == "existed":
        return "このIDはすでに登録済みです。正しいパスワードを入力してください。"
    # ログイン失敗
    elif result == "failed":
        return "failed"
    # ログイン成功
    else:
        session["userID"] = userID
        session["password"] = hashPassword
        session["status"] = "True"
        return redirect(url_for("W2"))


# M1-3 予定情報問い合わせ処理モジュール
def planQuery(userID, orderDate, mode):
    """
    機能概要:
        C3予定処理部に予定情報の要求を行い、結果を返す

    引数:
        userID    (str)    :ユーザのID
        orderDate (str)    :要求年月日 YYYY-MM-DDの形式
        mode      (str)    :'day'  :指定日
                            'month':指定月
                            'over' :指定日以降すべて
                            'all'  :すべて
    戻り値:
        dataList (list):予定情報の入ったリスト(予定情報は辞書形式)
        例:[{"start":"2021-06-10T12:00",　"end":"2021-06-10T15:00",　"title":"宿題",　"planID":"uqwpruedfqer"},{"start":"2021-...}]
    """
    if mode == "day":
        dataList = C3.planQuery(userID, orderDate[:10])
    elif mode == "over":
        dataList = C3.planQueryMany(userID, orderDate[:10])
    elif mode == "all":
        dataList = C3.planQueryAll(userID)
    return dataList


# M1-4 予定情報編集処理モジュール
def planEdit(userID, start, end, title, planID):
    """
    機能概要:
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


# M1-5 課題情報問い合わせ処理モジュール
def taskQuery(userID, orderDate, mode):
    """
    機能概要:
        C4課題処理部に課題情報の要求を行い、結果を返す

    引数:
        userID    (str)    :ユーザのID
        orderDate (str)    :要求年月日 YYYY-MM-DDの形式
        mode      (str)    :'day'  :指定日
                            'month':指定月
                            'over' :指定日以降すべて
                            'all'  :すべて

    戻り値:
        dataList (list):課題情報の入ったリスト(課題情報は辞書形式)
        例:[{"due":"2021-06-10T12:00",　"need":"7",　"title":"宿題",　"taskID":"uqwpruedfqer"},{"due":"2021-...}]
    """

    if mode == "day":
        dataList = C4.taskQuery(userID, orderDate[:10])
    elif mode == "over":
        dataList = C4.taskQueryMany(userID, orderDate[:10])
    elif mode == "all":
        dataList = C4.taskQueryAll(userID)
    return dataList


# M1-6 課題情報編集処理モジュール
def taskEdit(userID, due, need, title, taskID):
    """
    機能概要:
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
    newID = C4.taskEdit(userID, due, need, title, taskID)
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


# M1-7 mustDoリスト作成処理モジュール
def mustDo(userID, orderDate, restTime):
    """
    機能概要:
        要求された日のMustDoデータを返す(MustDoは締切前日に終わるように計算)

    引数:
        userID    (str):ユーザのID
        orderDate (str):mustDoリストを求める日付(YYYY-MM-DD)
        restTime  (str):一日の休憩時間

    戻り値:
        要求された日付のmustDoデータ(titleのみ)をリストとして返す
    """
    # 要求する予定、課題は次の日以降のもの
    orderDateTomorrow = datetime.datetime.strptime(orderDate, "%Y-%m-%d")
    orderDateTomorrow += datetime.timedelta(days=1)
    orderDateTomorrow = orderDateTomorrow.isoformat()[:10]

    planList = planQuery(userID, orderDateTomorrow, "over")  # 指定日以降の全予定データ
    planList = sorted(planList, key=lambda x: x["end"])
    taskList = taskQuery(userID, orderDateTomorrow, "over")  # 指定日以降の全課題データ
    taskList = sorted(taskList, key=lambda x: x["due"])

    if len(taskList) == 0:
        return []
    restTime = float(restTime)
    restTimeMin = (
        int(restTime) * 60 + (restTime - int(restTime)) * 60
    )  # restTimeを分変換(例:2.5時間->150分)
    canDoTime = 24 * 60 - restTimeMin  # 一日に課題を可能な時間(分)

    # 予定の必要時間を求める関数(分)
    def planNeedTime(p):
        resultSum = (int(p["end"][11:13]) - int(p["start"][11:13])) * 60  # 時間を分に
        resultSum += int(p["end"][14:16]) - int(p["start"][14:16])  # 分を足す
        return resultSum

    # 課題の必要時間を求める関数(分)
    def taskNeedTime(t):
        resultSum = int(t["need"]) * 60  # 時間を分に
        resultSum += (float(t["need"]) - int(t["need"])) * 60  # 少数部を分に
        return resultSum

    # 課題の締切時間の一日前を返す関数
    def taskBeforeDue(t):
        tdue = datetime.datetime.strptime(t["due"][:10], "%Y-%m-%d")
        tdue -= datetime.timedelta(days=1)
        tdue = tdue.isoformat()
        return tdue

    # 課題の残り時間(needMin)を更新する関数
    def taskNeedMinUpdate():
        nonlocal targetDay
        nonlocal orderDate
        nonlocal restCanTime
        nonlocal taskList
        nonlocal planList

        # 課題リストに課題が残ってない時
        if len(taskList) == 0:
            return
        # リストの最後の課題が処理日よりも前にある時
        if taskList[-1]["due"] < targetDay:
            targetDay = taskList[-1]["due"][:10]
            return

        # 課題をする時間が残っているとき
        if restCanTime > 0:
            # 課題が終わる時
            if taskList[-1]["needMin"] - restCanTime <= 0:
                restCanTime -= taskList[-1]["needMin"]
                del taskList[-1]
                taskNeedMinUpdate()

            # 課題が終わらない時
            else:
                taskList[-1]["needMin"] -= restCanTime  # 課題の残り必要時間を減らす
                # 考える日を一日前へ
                targetDay = datetime.datetime.strptime(targetDay, "%Y-%m-%d")
                targetDay -= datetime.timedelta(days=1)
                targetDay = targetDay.isoformat()[:10]
                if targetDay == orderDate:
                    return

        # 課題をする時間が残っていないとき
        else:
            # 考える日を一日前へ
            targetDay = datetime.datetime.strptime(targetDay, "%Y-%m-%d")
            targetDay -= datetime.timedelta(days=1)
            targetDay = targetDay.isoformat()[:10]

    # 予定辞書に必要時間(分)を追加
    for plan in planList:
        plan["needMin"] = planNeedTime(plan)
    # 課題辞書に必要時間(分)を追加
    for task in taskList:
        task["needMin"] = taskNeedTime(task)
    # 締め切り日を一日前に設定(締切日当日には課題の提出のみをするため)
    for task in taskList:
        task["due"] = taskBeforeDue(task)

    # 考える日付(一番最後の課題の日付で初期化)
    targetDay = datetime.datetime.strptime(taskList[-1]["due"][:10], "%Y-%m-%d")
    targetDay = targetDay.isoformat()[:10]

    mustDoList = []  # 返り値用リスト
    # 一番最後の課題の締切日より後にある予定をスキップする
    while True:
        if len(planList) == 0:
            break
        # 後にある
        if targetDay < planList[-1]["end"][:10]:
            del planList[-1]
        # 前にある
        else:
            break

    # 考える日付がorderDateより未来にある時繰り返す
    while targetDay > orderDate:
        planNeedSum = 0  # targetDayの予定の必要総時間
        while True:
            if len(planList) == 0:
                break
            if planList[-1]["end"][:10] == targetDay:
                planNeedSum += planNeedTime(planList[-1])
                del planList[-1]
            elif planList[-1]["end"][:10] < targetDay:
                break
        restCanTime = canDoTime - planNeedSum  # 課題遂行可能な時間
        taskNeedMinUpdate()
        if len(taskList) == 0:
            break

    # 最後まで残った課題のタイトルをmustDoListに入れる
    for task in taskList:
        mustDoList.append(task["title"])

    return mustDoList
