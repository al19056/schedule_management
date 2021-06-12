##################################################
###***Designer:池之上
###***Date:2021.6.12
###***Purpose:C7コンポーネント
##################################################

#CustomerInformationRegistration 顧客情報登録
def CIR(userID,password):
    import sys
    import math
    import argparse
    import logging
    """
        C2 認証処理部から送られてきたデータを登録する。
        引数:
            userID (str):W1ログイン画面からPOSTされたemailフィールド
            password (str):W1ログイン画面からPOSTされたpasswordフィールド


    """        
    count = 0
    userIDlist = []
    passwordlist = []
    # userIDlist: userIDの配列 
    # passwordlist: passwordの配列
    userIDlist.append("userID")
    passwordlist.append("password")
    count+=1
    if userIDlist[count] is None:
        return 0
    else:
        return 1

    
#CustomerInformationSuvey(userID) 顧客情報調査(userID)
    def CISu():
        """
        userIDの情報をC2 認証処理部にデータを送る
        戻り値　:　userIDlist
        """
        return userIDlist

    #CustomerInformationSuvey(password) 顧客情報調査(password)
    def CISp():
        """
        passwordの情報をC2 認証処理部にデータを送る
        戻り値: passwordlist
        """
        return passwordlist
