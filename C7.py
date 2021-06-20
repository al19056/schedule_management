##################################################
###***Designer:池之上
###***Date:2021.6.12
###***Purpose:C7コンポーネント
##################################################

#CustomerInformationRegistration 顧客情報登録
import sys
from typing import Counter
import os


list1 = []
list2 = []
#list1 : 引数のuserIDを一時保存する
#list2 : 引数のpasswordを一時保存する 
# ここに各々のデータを格納する



def CIR(userID,password):
    import math
    import argparse
    #userIDlist : userIDの配列
    #passwordlist : passwordの配列 
    # ここに各々のデータを格納する 
    """
        C2 認証処理部から送られてきたデータを登録する。
        引数:
            userID (str):W1ログイン画面からPOSTされたemailフィールド
            password (str):W1ログイン画面からPOSTされたpasswordフィールド


    """
    #userIDとpasswordを各々のlistに追加する
    list1.append(userID)
    list2.append(password)

    """
    userIDfile.txt ----> userIDのデータを保存する
    passwordfile.txt ----> passwordのデータを保存する
    """

    #userIDfile.txtを追記状態で開き、userIDを追加する
    with open("userIDfile.txt","a",encoding = "utf-8",errors="ignore") as f1:
        f1.write(userID)
        f1.write("\n")
        f1.close
    #passwordfile.txtが存在しない場合
    if os.path.exists('passwordfile.txt') is False:
        #passwordfile.txtを新規書き込み状態で開き、passwordを追加する
        with open("passwordfile.txt","w",encoding = "utf-8",errors = "ignore") as f2:
            f2.write(password)
            f2.write("\n")
            f2.close
    #passwordfile.txtが存在する場合
    else:
        #passwordfile.txtを追記状態で開き、passwordを追加する
        with open("passwordfile.txt","a",encoding = "utf-8",errors = "ignore") as f2:
            f2.write(password)
            f2.write("\n")
            f2.close

    #先ほど入れた配列の中身があるかどうか調べる
    if list1[0] is None:
        return 0
    else:
        return 1

    
#CustomerInformationSuvey(userID) 顧客情報調査(userID)
def CISu():
    """
    userIDの情報をC2 認証処理部にデータを送る
    戻り値　:　userIDlist
    """

    #userIDlist ---> userIDのlistを格納するためのlist
    #userIDfile.txtが存在しない場合
    if os.path.exists('userIDfile.txt') is False:
        #userIDfile.txtを作り、その後読み込み状態にする
        with open("userIDfile.txt","w",encoding = "utf-8",errors = "ignore") as f3:
            f3.close()
        with open("userIDfile.txt","r",encoding = "utf-8",errors = "ignore") as f4: 
            userIDlist = f4.readlines()    #f4をlist型にして、userIDlistに渡す
            f4.close()
        return userIDlist      
    #userIDfile.txtが存在する場合
    else:
        #userIDfile.txtを読み込み状態にする    
        with open("userIDfile.txt","r",encoding = "utf-8",errors = "ignore") as f3:
            userIDlist = f3.readlines()    #f3をlist型にして、userIDlistに渡す
            f3.close() 
        return userIDlist      #f3をlist型の状態で返す

#CustomerInformationSuvey(password) 顧客情報調査(password)
def CISp():
    """
    passwordの情報をC2 認証処理部にデータを送る
    戻り値: passwordlist
    """
    #passwordlist ---> passwordのlistを格納するためのlist    
    #最初からpasswordfileを読み込み状態にする
    # coding: utf-8
    with open("passwordfile.txt","r",encoding = "utf-8",errors = "ignore") as f5:
        passwordlist = f5.readlines() #f5をlist型にして、passwordlistに渡す
        f5.close()
    return passwordlist          

