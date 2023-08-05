# つかいかた

## makeconnection.php - ユーザ登録
### POST形式
```json
{
  "address":"addres",
  "pass":"passowrd"
}
```
### 各解説
|キー|型|備考|必須|
|-|-|-|-|
|address|String|メアド|〇|
|pass|String|パスワード(ほぼ使わない)|〇|

## かえってくるでーた
```json
{
    "result":"UserData Regist Successful","resultcode":200,
    "userdata":{
        "address":"ma@example.com",
        "pass":"tekisto",
        "uuid":"91c85cd6_a3f7_48bd_8735_65725772bb82"
        }
}
```

## 各解説
|キー|型|備考|
|-|-|-|
|result|String|結果です。英語だけど単語なので読めるはず|
|resultcode|int|200:成功 403:失敗
|userdata|Object|サーバに登録したユーザデータがオウム返しされます|
|userdata.address|String|メアド|
|userdata.pass|String|パスワード(ほぼ使わない)|
|userdata.uuid|String|今後超重要なIDです。なくしたらﾀﾋ|

-- --

## movieobs.php - 映像の解析API

### POST形式

```json
{
    "uuid":"uuid"
}
```

### 各解説
|キー|型|備考|必須|
|-|-|-|-|
|uuid|String|UUID　makeconnection.phpにかえってきたものを。|〇|

> **Note**  
> ファイル送信はpythonのrequestライブラリについてる、filesをつかって"file1"というキーで送信してください。  
> そうじゃないと動きません。やり方は調べてえｎ

## かえってくるでーた
```json
{
  "result":"解析に成功しました",
  "resultcode":200,
  "respcode":0,
  "DetecResult":
    {
      "Syakan":"95",
      "is_Aorare":true
    }
}
```
## 各解説
|キー|型|備考|
|-|-|-|
|result|String|結果です。突貫工事のため成功以外実装していません|
|resultcode|int|結果を表すコードです。resultと同様(ry|
|respcode|int|実行結果(信用できるVer)です。Linuxのコマンドラインの終了コードになってます。|
|DetecResult|Object|検出結果が保存されているやつです|
|DetecResult.Syakan|String|車間距離で煽られている確率を出します。なんでString？|
|DetecResult.is_Aorare|bool|煽られているかを判断して返してます。Syakanが80超えてたらtrueです。気分で決めました。|


## ソースコードについて
### 同一リポジトリ内、codesフォルダ内に多分全部入ってるので、煮るなり焼くなり好きにしてくだしあ。

-- --

## api-test.py - 番外編

## なにこれ？
APIを作るときに動作テストで使ったpyファイルです。

## 含まれる関数

### userregist
|引数|型|備考|必須|
|-|-|-|-|
|[0]|String|メアドです。|〇|
|[1]|String|ぱすわです。|〇|

返却物  

makeconnection.phpと同じ内容がそのまま帰ってきます。json.dumpsするなりして、使ってください。

----
 
### sendMovieData

ファイル内に呼び出しを放置しているので、それを参考にしてください。  
帰ってくるのは、movieobs.phpと同じ内容が帰ってきます。  
userregistと同様、json.dumpsするなりして使ってください。
