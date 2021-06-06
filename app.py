from flask import Flask, render_template, url_for, flash, redirect, request  # 追加
import ast
import json
import C1

app = Flask(__name__)
page = "W1"


@app.route("/", methods=["GET", "POST"])
def home():
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
                title=page,
                message="Enull",
                existedPlans=[
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
                existedTasks=[
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
    # url直打ち込み回避
    if request.method == "GET":
        return redirect(url_for("home"))

    resStr = request.get_data()
    resStr = resStr.decode()
    resStr = resStr.replace("'", '"')
    resDict = json.loads(resStr)

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
            else:
                return "success update"
    # 更新失敗
    else:
        return "failed"


# postは{"due":"・・・", "need":"・・・", "title":"・・・", "id":"・・・"}の形
@app.route("/task/edit", methods=["GET", "POST"])
def taskEdit():
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
            else:
                return "success update"
    # 更新失敗
    else:
        return "failed"


@app.route("/plan/query", methods=["GET", "POST"])
def planQuery():
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
