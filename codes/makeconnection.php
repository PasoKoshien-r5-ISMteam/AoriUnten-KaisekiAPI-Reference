<?php
// Writed By Kanata Saito

//ユーザ登録(コネクションID生成)
require_once 'makeuuid.php';
$address = $_POST["address"];
$pass = password_hash($_POST["pass"],PASSWORD_DEFAULT);
$uuid = uuidmake();
$resultdata = [];
$rs_Msg = "";
$rs_Code = 200;

$dsn = "mysql:host=localhost; dbname=toshocsrs; charset=utf8";
$username = "＊＊＊＊＊";
$password = "＊＊＊＊＊";

try {
    $dbh = new PDO($dsn, $username, $password);
} catch (PDOException $e) {
    $rs_Msg = $e->getMessage();
}

if($address != null && $pass != null){
    $sql = "SELECT * FROM userdata WHERE address = :address";
    $stmt = $dbh->prepare($sql);
    $stmt->bindValue(':address', $address);
    $stmt->execute();
    $member = $stmt->fetch();
    if($member['address'] === $address){
        $rs_Msg = "UserData Regist Failture";
        $rs_Code = 403;
    }
    else{
        $sql = "INSERT INTO userdata (address, pass, uuid) VALUES(:addres, :pass, :uuid)";
        $stmt = $dbh->prepare($sql);
        $stmt->bindValue(':addres', $address);
        $stmt->bindValue(':pass', $pass);
        $stmt->bindValue(':uuid', $uuid);
        $stmt->execute();
        $rs_Msg = "UserData Regist Successful";
        $rs_Code = 200;
        mkdir($uuid,0755,true);
        mkdir("$uuid/detec_temp",0755,true);
    }
}
else {
    $rs_Msg = "UserData Regist Failture";
    $rs_Code = 403;
}

header("Content-Type: application/json; charset=UTF-8");
$resultdata['result'] = $rs_Msg;
$resultdata['resultcode'] = $rs_Code;
$resultdata['userdata']['address'] = $address;
$resultdata['userdata']['pass'] = $_POST['pass'];
$resultdata['userdata']['uuid'] = $uuid;
echo json_encode($resultdata, JSON_UNESCAPED_UNICODE);
?>