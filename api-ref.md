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

## かえってくｒ

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
|キー|型|備考|
|-|-|-|
|result|String|結果です。突貫工事のため成功以外実装していません|
|resultcode|int|結果を表すコードです。resultと同様(ry|
|respcode|int|実行結果(信用できるVer)です。Linuxのコマンドラインの終了コードになってます。|
|DetecResult|Object|検出結果が保存されているやつです|
|DetecResult.Syakan|String|車間距離で煽られている確率を出します。なんでString？|
|DetecResult.is_Aorare|bool|煽られているかを判断して返してます。Syakanが80超えてたらtrueです。気分で決めました。|
