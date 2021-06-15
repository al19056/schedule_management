##############################################
###***Designer:池之上
###***Date:2021.6.12
###***Purpose:C2コンポーネント
##############################################
import C7
import sys
import logging
import math
import argparse

#authenticationProcessing 認証処理
def authenticationProcessing(userID,password):

    """
    C1 UI処理部とC7 顧客情報管理部からの情報を照合することで、顧客の認証を行う。

    引数:  
        userID (str):W1ログイン画面からPOSTされたemailフィールド
        password (str):W1ログイン画面からPOSTされたpasswordフィールド

    戻り値:
        失敗時:
            'failed':C1に返す
        成功時:
            'success':C1に返す
    """
    
 #for文を使って、顧客情報のuserIDを照合する    
    for num in C7.CISu():
 #CISu()が引数のuserIDと合ったら、for文を抜ける
        if num is userID:
            break
 #for文の終了後
    else:    
        return "failed"
    
#for文を使って、顧客情報のpasswordを照合する
    for mum in C7.CISp():
#CISp()と引数のpasswordが合ったら、successを返し、for文を抜ける
        if mum == password:
            return "success"
        break
#for文の終了後
    else:
        return "failed" 

def addUser(userID,password):
    """
    新規登録ユーザのユーザIDとパスワードを顧客管理部に登録する

    引数:  
    userID (str):W1ログイン画面からPOSTされたemailフィールド
    password (str):W1ログイン画面からPOSTされたpasswordフィールド

    戻り値:
    exited : 既に存在していた場合にC1に返す
    failed : エラーが起こった場合にC1に返す
    success : 登録に成功した場合にC1に返す
    """
    result = authenticationProcessing(userID,password)
#既に登録済み
    if result == "success":
        return "exited"
    x = C7.CIR(userID,password)
    if x == 0:
        return "failed"
    else:
        return "success"
