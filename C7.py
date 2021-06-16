##################################################
###***Designer:池之上
###***Date:2021.6.12
###***Purpose:C7コンポーネント
##################################################

#CustomerInformationRegistration 顧客情報登録
from typing import Counter
import os


userIDlist = []
passwordlist = []
#userIDlist : userIDの配列
#passwordlist : passwordの配列 
# ここに各々のデータを格納する



def CIR(userID,password):
    import sys
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
    userIDlist.append(userID)
    passwordlist.append(password)

    """
    file1.txt ----> userIDのデータを保存する
    file2.txt ----> passwordのデータを保存する
    """

    #file1.txtを追記状態で開き、userIDを追加する
    f1 = open("file1.txt","a")
    f1.write(userID)
    f1.write("\n")
    f1.close
    #file2.txtが存在しない場合
    if os.path.exists('file2.txt') is False:
        #file2.txtを新規書き込み状態で開き、passwordを追加する
        f2 = open("file2.txt","w")
        f2.write(password)
        f2.write("\n")
        f2.close
    #file2.txtが存在する場合
    else:
        #file2.txtを追記状態で開き、passwordを追加する
        f2 = open("file2.txt","a")
        f2.write(password)
        f2.write("\n")
        f2.close

    #先ほど入れた配列の中身があるかどうか調べる
    if userIDlist[0] is None:
        return 0
    else:
        return 1

    
#CustomerInformationSuvey(userID) 顧客情報調査(userID)
def CISu():
    """
    userIDの情報をC2 認証処理部にデータを送る
    戻り値　:　userIDlist
    """

    #list1 ---> userIDのlistを格納するためのlist
    #file1.txtが存在しない場合
    if os.path.exists('file1.txt') is False:
        #file1.txtを作り、その後読み込み状態にする
        f3 = open("file1.txt","w")
        f3.close()
        f4 = open("file1.txt","r")
        list1 = f4.readlines()    #f4をlist型にして、list1に渡す
        f4.close()
        return list1      
    #file1.txtが存在する場合
    else:
        #file1.txtを読み込み状態にする    
        f3 = open("file1.txt","r")
        list1 = f3.readlines()    #f3をlist型にして、list1に渡す
        f3.close() 
        return list1      #f3をlist型の状態で返す

#CustomerInformationSuvey(password) 顧客情報調査(password)
def CISp():
    """
    passwordの情報をC2 認証処理部にデータを送る
    戻り値: passwordlist
    """
    #list2 ---> passwordのlistを格納するためのlist    
    #最初からfile2を読み込み状態にする
    f5 = open("file2.txt","r")
    list2 = f5.readlines() #f5をlist型にして、list2に渡す
    f5.close()
    return list2          


