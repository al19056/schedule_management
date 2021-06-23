################################
###Designer:山川
###Date:2021.6.17
###Purpose:サーバー側プログラム
################################
from flask import (
    Flask,
    render_template,
    url_for,
    redirect,
    request,
    session,
)
import json
import os
import sqlite3
import datetime

try:
    planConn = sqlite3.connect("db/plans.db")
    taskConn = sqlite3.connect("db/tasks.db")
    userConn = sqlite3.connect("db/users.db")
except sqlite3.Error as err:
    print("catch error:", err)
    exit()

import C1

app = Flask(__name__)
app.secret_key = os.urandom(16)  # Cookie暗号化に使用

# ログイン画面
@app.route("/login", methods=["GET", "POST"])
def W1():
    """
    機能概要:
        W1ログイン画面におけるPOST,GET要求への応答の定義

    引数：なし

    戻り値：
        POST時：
            ログイン成功時　：W2へリダイレクト
            ログイン失敗時　：エラーメッセージ表示
            ユーザ登録時  　：W2へリダイレクト
            ユーザ登録失敗時：エラーメッセージ表示

        GET時：
            W1を表示
    """
    session["restTime"] = 13  # defaultの休憩時間を設定

    # post時(htmlフォームからpost)
    if request.method == "POST":
        # loginボタン押下時
        if request.form.get("login"):
            return C1.requestLogin(
                request.form.get("email"), request.form.get("password")
            )
        # registerボタン押下時
        elif request.form.get("register"):
            return C1.requestAddUser(
                request.form.get("email"), request.form.get("password")
            )
        # その他はエラー
        else:
            return "error"

    # 通常読み込み時
    if request.method == "GET":
        return render_template("W1.html")


# 初期画面
@app.route("/home", methods=["GET", "POST"])
def W2():
    """
    機能概要:
        W2初期画面におけるPOST,GET要求への応答の定義

    引数：なし

    戻り値：
        非ログイン時：W1へリダイレクト

        POST時：
            課題追加ボタン押下時　：W6へリダイレクト
            更新ボタン押下時　  　：mustDoリストを更新しW2を表示
            日付ボタン押下時  　　：W3へリダイレクト

        GET時：
            既ログイン時：W2表示
    """
    # 非ログイン時
    if not "status" in session.keys():
        print("non status")
        return redirect(url_for("W1"))
    if session["status"] != "True":
        print("status!=true")
        return redirect(url_for("W1"))

    # post時
    if request.method == "POST":
        # 課題追加ボタン押下時(htmlフォームからpost)
        if request.form.get("addTask", None) != None:
            return redirect(url_for("W6"))
        # 更新ボタン押下時(htmlフォームからpost)
        elif request.form.get("update", None) != None:
            nowDay = datetime.datetime.now().isoformat()[:10]  # 本日(YYYY-MM-DD)
            session["restTime"] = request.form.get("restTime", None)
            return render_template(
                "W2.html",
                restTime=session["restTime"],
                mustDoList=C1.mustDo(session["userID"], nowDay, session["restTime"]),
                toDoList=C1.taskQuery(session["userID"], nowDay, "over"),
                planEvents=C1.planQuery(session["userID"], nowDay, "all"),
                taskEvents=C1.taskQuery(session["userID"], nowDay, "all"),
            )
        # 日付ボタン押下時(jQueryからpost)
        else:
            dictKeys = request.form.keys()
            resDate = ""
            for key in dictKeys:
                resDate = key
            return resDate[:10]  # 日付を返し日付のW3へjQueryで遷移

    # 通常読み込み時
    if request.method == "GET":
        nowDay = datetime.datetime.now().isoformat()[:10]  # 本日(YYYY-MM-DD)
        # 休憩時間・mustDoリスト・toDoList・予定情報(全日程)・課題情報(全日程)を引数にW2へ遷移
        return render_template(
            "W2.html",
            restTime=session["restTime"],
            mustDoList=C1.mustDo(session["userID"], nowDay, session["restTime"]),
            toDoList=C1.taskQuery(session["userID"], nowDay, "over"),
            planEvents=C1.planQuery(session["userID"], nowDay, "all"),
            taskEvents=C1.taskQuery(session["userID"], nowDay, "all"),
        )


# 予定・課題の確認画面
@app.route("/homeDetails/<date>", methods=["GET", "POST"])
def W3(date):
    """
    機能概要:
        W3予定・課題確認画面におけるPOST,GET要求への応答の定義

    引数：
        date (文字列):選択された日付

    戻り値：
        非ログイン時：W1へリダイレクト

        POST時：
            予定欄の編集ボタン押下時　：W4へリダイレクト
            課題欄の編集ボタン押下時　：W5へリダイレクト
            戻るボタン押下時　　      ：W2へリダイレクト
            日付ボタン押下時  　    　：押された日付を返す

        GET時：
            既ログイン時：W3表示
    """
    # 非ログイン時
    if not "status" in session.keys():
        print("non status")
        return redirect(url_for("W1"))
    if session["status"] != "True":
        print("status!=true")
        return redirect(url_for("W1"))

    # post時
    if request.method == "POST":
        # 予定欄の編集ボタン押下時
        if request.form.get("planEdit", None) != None:
            return redirect(url_for("W4", date=date))
        # 課題欄の編集ボタン押下時
        elif request.form.get("taskEdit", None) != None:
            return redirect(url_for("W5", date=date))
        # 戻るボタン押下
        elif request.form.get("back", None) != None:
            return redirect(url_for("W2"))
        # 日付ボタン押下
        else:
            dictKeys = request.form.keys()
            resDate = ""
            for key in dictKeys:
                resDate = key
            return resDate[:10]  # 日付を返し日付のW3へjQueryで遷移

    # 通常読み込み時
    if request.method == "GET":
        # 休憩時間・mustDoリスト・toDoList・予定情報(全日程)・課題情報(全日程)を引数にW2へ遷移
        return render_template(
            "W3.html",
            planEvents=C1.planQuery(session["userID"], date, "all"),
            taskEvents=C1.taskQuery(session["userID"], date, "all"),
            planTheDate=C1.planQuery(session["userID"], date, "day"),
            taskTheDate=C1.taskQuery(session["userID"], date, "day"),
            date=date,
        )


# 予定編集画面
@app.route("/planDetails/<date>", methods=["GET", "POST"])
def W4(date):
    """
    機能概要:
        W4予定編集画面におけるPOST,GET要求への応答の定義

    引数：
        date (文字列):選択された日付

    戻り値：
        非ログイン時：W1へリダイレクト

        POST時：
            戻るボタン押下時　　      ：W3へリダイレクト

        GET時：
            既ログイン時：W4表示
    """
    # 非ログイン時
    if not "status" in session.keys():
        return redirect(url_for("W1"))
    if session["status"] != "True":
        return redirect(url_for("W1"))

    # 戻るボタン
    if request.form.get("send"):
        return redirect(url_for("W3", date=date))

    existedPlans = C1.planQuery(session["userID"], date, "day")
    return render_template("W4.html", existedPlans=existedPlans)


# 課題編集画面
@app.route("/taskDetails/<date>", methods=["GET", "POST"])
def W5(date):
    """
    機能概要:
        W5課題編集画面におけるPOST,GET要求への応答の定義

    引数：
        date (文字列):選択された日付

    戻り値：
        非ログイン時：W1へリダイレクト

        POST時：
            戻るボタン押下時：W3へリダイレクト

        GET時：
            既ログイン時：W5表示
    """
    # 非ログイン時
    if not "status" in session.keys():
        return redirect(url_for("W1"))
    if session["status"] != "True":
        return redirect(url_for("W1"))

    # 戻るボタン
    if request.form.get("send"):
        return redirect(url_for("W3", date=date))

    existedTasks = C1.taskQuery(session["userID"], date, "day")
    return render_template("W5.html", existedTasks=existedTasks)


# 課題追加画面
@app.route("/taskAddition", methods=["GET", "POST"])
def W6():
    """
    機能概要:
        W6課題追加画面におけるPOST,GET要求への応答の定義

    引数：なし

    戻り値：
        非ログイン時：W1へリダイレクト

        POST時：
            戻るボタン押下時　　      ：W2へリダイレクト

        GET時：
            既ログイン時：W6表示
    """
    # 非ログイン時
    if not "status" in session.keys():
        return redirect(url_for("W1"))
    if session["status"] != "True":
        return redirect(url_for("W1"))

    # 戻るボタン
    if request.form.get("send"):
        return redirect(url_for("W2"))

    return render_template("W6.html")


# W4で呼ばれる
# postは{"start":"・・・", "end":"・・・", "title":"・・・", "planID":"・・・"}の形
@app.route("/plan/edit", methods=["POST"])
def planEdit():
    """
    機能概要:
        W4予定編集画面で決定ボタン・削除ボタン(既に存在していた予定の削除時のみ)
        を押下した時呼び出される関数

    引数:なし

    戻り値:
        更新成功:
            新規追加時:新規作成ID
                削除時:'success del'
                更新時:'success update'
            更新失敗時:'failed'
    """

    resStr = request.get_data()  # postされたバイト文字列
    resStr = resStr.decode()  # バイト文字列を文字列に変換
    resStr = resStr.replace("'", '"')
    resDict = json.loads(resStr)  # 辞書へ変換

    # 更新成功:newID, 失敗:'failed'が返される
    result = C1.planEdit(
        session["userID"],
        resDict["start"],
        resDict["end"],
        resDict["title"],
        resDict["planID"],
    )
    return result


# W5,6で呼ばれる
# postは{"due":"・・・", "need":"・・・", "title":"・・・", "taskID":"・・・"}の形
@app.route("/task/edit", methods=["POST"])
def taskEdit():
    """
    機能概要:
        W5,6予定編集画面で決定ボタン・削除ボタン(既に存在していた課題の削除時のみ)
        を押下した時呼び出される関数

    引数:なし

    戻り値:
        更新成功:
            新規追加時:新規作成ID
                削除時:'success del'
                更新時:'success update'
            更新失敗時:'failed'
    """

    resStr = request.get_data()
    resStr = resStr.decode()
    resStr = resStr.replace("'", '"')
    resDict = json.loads(resStr)
    print(resDict)
    # 更新成功:newID, 失敗:'failed'が返される
    result = C1.taskEdit(
        session["userID"],
        resDict["due"],
        resDict["need"],
        resDict["title"],
        resDict["taskID"],
    )
    return result


# 指定されていないurlにアクセスしたとき
@app.errorhandler(404)
def errorPage(error):
    """
    機能概要:
        存在しないurlにアクセスしたときにW1へリダイレクトする

    引数：
        error: エラー情報

    戻り値：
        W1へリダイレクト
    """
    return redirect(url_for("W1"))


if __name__ == "__main__":
    app.run(
        debug=False, port=50280, host="160.16.141.77", threaded=True
    )  ###############host='0.0.0.0'とport=とthreaded=True,debug=Falseを指定する
