"""
***Designer:山川
***Date:2021.6.6
***Purpose:サーバー側プログラム
"""
from flask import Flask, render_template, url_for, flash, redirect, request  # 追加
import ast
import json
import C1

app = Flask(__name__)
page = "W1"


@app.route("/", methods=["GET", "POST"])
def home():
    """
    機能概要
        テスト用です
        W1,2,3,4,5,6へ遷移できるボタンがあります
        putfuncボタンは遷移先を指定してないのでエラーがでます
    """
    title = "home"

    # 初回?
    if request.method != "POST":
        return render_template("home.html", title=title)
    # ボタンで画面遷移
    else:
        # 画面遷移request
        if request.form.get("send") not in ("決定", "戻る"):
            page = request.form.get("send", None)
            # messageを与えるとエラーalart(E1,E2,・・・,E8)
            return render_template(
                page + ".html",
                title=page,  # htmlのtitleにpage名を渡す
                # message="E1",
                existedPlans=[  # 既に存在している予定
                    {
                        "start": "2021-06-10T15:37",
                        "end": "2021-07-10T15:01",
                        "title": "test1",
                        "id": "111fd1111",
                    },
                    {
                        "start": "2022-06-10T15:37",
                        "end": "2022-07-10T15:01",
                        "title": "test2",
                        "id": "22222222",
                    },
                ],
                existedTasks=[  # 既に存在している課題
                    {
                        "due": "2021-06-10T15:37",
                        "need": "7",
                        "title": "test1",
                        "id": "111fd1111",
                    },
                    {
                        "due": "2022-06-10T15:37",
                        "need": "4",
                        "title": "test2",
                        "id": "22222222",
                    },
                ],
            )
        else:
            return render_template("home.html")


# postは{"start":"・・・", "end":"・・・", "title":"・・・", "id":"・・・"}の形
@app.route("/plan/edit", methods=["GET", "POST"])
def planEdit():
    """
    機能概要:
        W4予定編集画面で決定ボタン・削除ボタン(既に存在していた予定の削除時のみ)
        を押下した時呼び出される関数

            引数:
                クライアント側から{"start":"・・・", "end":"・・・", "title":"・・・", "id":"・・・"}
                の形でバイト列が送られてくる

            戻り値:
                更新成功:
                    新規追加時:新規作成ID
                        削除時:'success del'
                        更新時:'success update'
                    更新失敗時:'failed'
    """
    # url直打ち込み回避
    if request.method == "GET":
        return redirect(url_for("home"))

    resStr = request.get_data()  # postされたバイト文字列
    resStr = resStr.decode()  # バイト文字列を文字列に変換
    resStr = resStr.replace("'", '"')
    resDict = json.loads(resStr)  # 辞書へ変換

    # 更新成功:ID, 失敗:'Failed'が返される
    result = C1.planEdit(
        resDict["start"], resDict["end"], resDict["title"], resDict["id"]
    )
    # 更新成功
    if result != "Failed":
        # 追加処理の時
        if resDict["id"] == "":
            return result  # かぶりがないIDを作る関数が必要
        else:
            # 削除処理の時
            if resDict["start"] == "":
                return "success del"
            # 更新処理の時
            else:
                return "success update"
    # 更新失敗
    else:
        return "failed"


# postは{"due":"・・・", "need":"・・・", "title":"・・・", "id":"・・・"}の形
@app.route("/task/edit", methods=["GET", "POST"])
def taskEdit():
    """
    機能概要:
        W5,6予定編集画面で決定ボタン・削除ボタン(既に存在していた課題の削除時のみ)
        を押下した時呼び出される関数

            引数:
                クライアント側から{"due":"・・・", "need":"・・・", "title":"・・・", "id":"・・・"}
                の形でバイト列が送られてくる

            戻り値:
                更新成功:
                    新規追加時:新規作成ID
                        削除時:'success del'
                        更新時:'success update'
                    更新失敗時:'failed'
    """
    # url直打ち込み回避
    if request.method == "GET":
        return redirect(url_for("home"))

    resStr = request.get_data()
    resStr = resStr.decode()
    resStr = resStr.replace("'", '"')
    resDict = json.loads(resStr)

    # 更新成功:ID, 失敗:'Failed'が返される
    result = C1.taskEdit(
        resDict["due"], resDict["need"], resDict["title"], resDict["id"]
    )
    # 更新成功
    if result != "Failed":
        # 追加処理の時
        if resDict["id"] == "":
            return result  # かぶりがないID
        else:
            # 削除処理の時
            if resDict["due"] == "":
                return "success del"
            # 更新処理の時
            else:
                return "success update"
    # 更新失敗
    else:
        return "failed"


# YYYY-MM-DDの形でpost
@app.route("/plan/query", methods=["GET", "POST"])
def planQuery():
    """
    機能概要:
        要求された日付のデータを返す

        引数:
            クライアント側から'YYYY-MM-DD'の形でpostされる

        戻り値:
            要求された日付のデータをリストとして返す

    """
    # url直打ち込み回避
    if request.method == "GET":
        return redirect(url_for("home"))

    # 指定日のplanを返す
    orderDate = request.get_data()  # バイト文字列
    orderDate = orderDate.decode()  # バイト文字からテキスト文字列へ
    orderDataList = C1.planQuery(orderDate)
    return orderDataList


# YYYY-MM-DDの形でpost
@app.route("/task/query", methods=["GET", "POST"])
def taskQuery():
    """
    機能概要:
        要求された日付のデータを返す

        引数:
            クライアント側から'YYYY-MM-DD'の形でpostされる

        戻り値:
            要求された日付のデータをリストとして返す

    """
    # url直打ち込み回避
    if request.method == "GET":
        return redirect(url_for("home"))

    # 指定日のtaskを返す
    orderDate = request.get_data()  # バイト文字列
    orderDate = orderDate.decode()  # バイト文字からテキスト文字列へ
    orderDataList = C1.taskQuery(orderDate)
    return orderDataList


# 定義していないurl
@app.errorhandler(404)
def pageNotFound(error):
    return "404 not found."


if __name__ == "__main__":
    app.run(debug=True)
