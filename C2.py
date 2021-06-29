
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
    #num ---> for文を回すための引数    
    for num in C7.CISu():
        #numとuserIDが一致した場合、次の処理に移る
        if num == userID + "\n":
            #xにuserIDを格納している番号を入れる
            x = C7.CISu().index(num)
            #C7.CISp()のx番目の要素とpasswordが一致した場合、successを返す
            if C7.CISp()[x] == password +"\n":
                return "success"
    #for文終了後、何にも当てはまらない場合、failedを返す               
    else:
        return "failed"



def addUser(userID,password):
    """
    新規登録ユーザのユーザIDとパスワードを顧客管理部に登録する

    引数:  
    userID (str):W1ログイン画面からPOSTされたemailフィールド
    password (str):W1ログイン画面からPOSTされたpasswordフィールド

    戻り値:
    existed : 既に存在していた場合にC1に返す
    failed : エラーが起こった場合にC1に返す
    success : 登録に成功した場合にC1に返す
    """
    #既に登録済み
    #lum ---> for文を回すための引数
    #lumとuserIDが一致した場合、exitedを返す。
    for lum in C7.CISu():
        if lum == userID + "\n":
            return "existed"
    
     #lumとuserIDが一致しなかった場合、C7のCIR関数を呼び出す。
    else:
        x = C7.CIR(userID,password)
    if x == 0:
        return "failed"
    else:
        return "success"
