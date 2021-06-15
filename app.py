"""
***Designer:山川
***Date:2021.6.6
***Purpose:サーバー側プログラム
"""
from flask import (
    Flask,
    render_template,
    url_for,
    flash,
    redirect,
    request,
    session,
)  # 追加
import ast
import json
import os
import sqlite3
import datetime
import C1

planConn = sqlite3.connect("db/plans.db")
taskConn = sqlite3.connect("db/tasks.db")
userConn = sqlite3.connect("db/users.db")

app = Flask(__name__)
page = "W1"
app.secret_key = os.urandom(16)

# ログイン画面
@app.route("/login", methods=["GET", "POST"])
def W1():
    session["restTime"] = 13  # default
    # login・registerボタン押下時
    if request.form:
        if request.form.get("login"):
            return C1.requestLogin(
                request.form.get("email"), request.form.get("password")
            )
        elif request.form.get("register"):
            return C1.requestAddUser(
                request.form.get("email"), request.form.get("password")
            )

    return render_template("W1.html")


# 初期画面
@app.route("/home", methods=["GET", "POST"])
def W2():
    # 非ログイン時
    if not "status" in session.keys():
        print("non status")
        return redirect(url_for("W1"))
    if session["status"] != "True":
        print("status!=true")
        return redirect(url_for("W1"))

    if request.method == "POST":
        # 課題追加ボタン押下時
        if request.form.get("addTask", None) != None:
            return redirect(url_for("W6"))
        # 更新ボタン押下時
        elif request.form.get("update", None) != None:
            session["restTime"] = request.form.get("restTime", None)
            return render_template(
                "W2.html",
                restTime=session["restTime"],
                mustDoList=C1.mustDo(
                    session["userID"],
                    datetime.datetime.now().isoformat()[:10],
                    session["restTime"],
                ),
                toDoList=C1.taskQuery(
                    session["userID"], datetime.datetime.now().isoformat()[:10], "over"
                ),
                planEvents=C1.planQuery(
                    session["userID"], datetime.datetime.now().isoformat()[:10], "all"
                ),
                taskEvents=C1.taskQuery(
                    session["userID"], datetime.datetime.now().isoformat()[:10], "all"
                ),
            )
        # 日付ボタン押下時
        else:
            dictKeys = request.form.keys()
            resDate = ""
            for key in dictKeys:
                resDate = key
            return resDate[:10]  # jqueryでの応答によるリダイレクト・レンダーはできないため日付を返しjqueryで遷移

    if request.method == "GET":
        return render_template(
            "W2.html",
            restTime=session["restTime"],
            mustDoList=C1.mustDo(
                session["userID"],
                datetime.datetime.now().isoformat()[:10],
                session["restTime"],
            ),
            toDoList=C1.taskQuery(
                session["userID"], datetime.datetime.now().isoformat()[:10], "over"
            ),
            planEvents=C1.planQuery(
                session["userID"], datetime.datetime.now().isoformat()[:10], "all"
            ),
            taskEvents=C1.taskQuery(
                session["userID"], datetime.datetime.now().isoformat()[:10], "all"
            ),
        )


@app.route("/homeDetails/<date>", methods=["GET", "POST"])
def W3(date):
    # 非ログイン時
    if not "status" in session.keys():
        print("non status")
        return redirect(url_for("W1"))
    if session["status"] != "True":
        print("status!=true")
        return redirect(url_for("W1"))

    return render_template("W3.html")


@app.route("/planDetails/<date>", methods=["GET", "POST"])
def W4(date):
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


@app.route("/taskDetails/<date>", methods=["GET", "POST"])
def W5(date):
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


@app.route("/taskAddition", methods=["GET", "POST"])
def W6():
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

            引数:
                クライアント側から{"start":"・・・", "end":"・・・", "title":"・・・", "id":"・・・"}
                の形でバイト列が送られてくる
                時間はYYYY-MM-DDThh:mmの形

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

            引数:
                クライアント側から{"due":"・・・", "need":"・・・", "title":"・・・", "id":"・・・"}
                の形でバイト列が送られてくる
                時間はYYYY-MM-DDThh:mmの形

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


'''
# YYYY-MM-DDの形でpost
@app.route("/plan/query", methods=["POST"])
def planQuery():
    """
    機能概要:
        要求された日付のデータを返す

        引数:
            クライアント側から'YYYY-MM-DD'の形でpostされる

        戻り値:
            要求された日付のデータをリストとして返す

    """

    # 指定日のplanを返す
    orderDate = request.get_data()  # バイト文字列
    orderDate = orderDate.decode()  # バイト文字からテキスト文字列へ
    orderDataList = C1.planQuery(session["userID"], orderDate, False)
    return orderDataList


# YYYY-MM-DDの形でpost
@app.route("/task/query", methods=["POST"])
def taskQuery():
    """
    機能概要:
        要求された日付のデータを返す

        引数:
            クライアント側から'YYYY-MM-DD'の形でpostされる

        戻り値:
            要求された日付のデータをリストとして返す

    """

    # 指定日のtaskを返す
    orderDate = request.get_data()  # バイト文字列
    orderDate = orderDate.decode()  # バイト文字からテキスト文字列へ
    orderDataList = C1.taskQuery(session["userID"], orderDate, False)
    return orderDataList


# YYYY-MM-DDの形でpost, mustDoリストを返す(titleが入ったリスト)
@app.route("/mustDo/query", methods=["POST"])
def mustDoQuery():
    orderDate = request.get_data()  # バイト文字列
    orderDate = orderDate.decode()  # バイト文字からテキスト文字列へ
    return C1.mustDo(session["userID"], orderDate, int(session["restTime"]))
'''


if __name__ == "__main__":
    app.run(
        debug=True
    )  ###############host='0.0.0.0'とport=とthreaded=True,debug=Falseを指定する
