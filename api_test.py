import requests
import os
import json

#APIとの通信に使うUUIDを保存&読み込みする関数
def LoSaUUID(or_ls,uuid=""):
    if(or_ls == "Load"):
        with open("settings.json",'r') as f:
            js_l = json.loads(f.read())
            return js_l['uuid']
    elif(or_ls == "Save"):
        with open("settings.json",'w') as f:
            data = {"uuid":uuid}
            f.write(json.dumps(data))

#ユーザ登録
def userregist(addres,passowrd):
    url = "http://procon.schnetworks.net/api/makeconnection.php"

    postitems = {
        'address':addres,
        'pass':passowrd
    }
    ps_result = requests.post(url,data=postitems)
    LoSaUUID("Save",json.loads(ps_result.text)['userdata']['uuid'])
    return ps_result.text

#動画ファイルの送信(20秒,mp4 MPEG-4フォーマットのみ対応)
def sendMovieData(filepath,uuid):
    url = "http://procon.schnetworks.net/api/movieobs.php"
    file = {
        'file1':open(filepath,"rb")
    }

    postitems = {
        'uuid':uuid
    }
    ps_result = requests.post(url,data=postitems,files=file)
    return ps_result.text

print(LoSaUUID("Load"))
#print(sendMovieData("D:/UserData/Siraisi/Videos/aoriunntenn_test.mp4","a25e898f_32bc_4756_b674_08c5a8f37d33"))
