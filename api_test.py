import requests
import os

#ユーザ登録
def userregist(addres,passowrd):
    url = "http://procon.schnetworks.net/api/makeconnection.php"

    postitems = {
        'address':addres,
        'pass':passowrd
    }
    ps_result = requests.post(url,data=postitems)
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

sendMovieData("録画した20秒のファイル","makeconnectionで帰ってきたuuid")