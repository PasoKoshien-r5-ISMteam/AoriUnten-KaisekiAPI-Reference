<?php
// Writed By Kanata Saito
header("Content-Type: application/json; charset=UTF-8");
usleep(1000);
$filepath_temp = $_FILES['file1']['tmp_name'];
$uuid = $_POST['uuid'];
$resultdata = [];
$getfile = file_get_contents("php://input");
$fileexecuts = preg_match("/...$/",$_FILES['file1']['name'],$match);

if(is_uploaded_file($filepath_temp)){
    $filepath_after = $uuid."/".date("Y-m-d-H-i-s").".".$match[0];
    if(move_uploaded_file($filepath_temp,$filepath_after)){
        chmod($filepath_after,0755);
    }
    else{
        $rs_Msg = "File Moving Error";
        $rs_Code = 500;
    }
}
else{
    $rs_Msg = "File Upload Error";
    $rs_Code = 500;
}

exec("python3.11 ./mvdetector.py $filepath_after $uuid 2>&1",$output,$exitcode);
//pyファイルから返却された各確率の代入

$resultdata['result'] = "解析に成功しました";
$resultdata['resultcode'] = 200;
$resultdata['respcode'] = $exitcode;
$resultdata['DetecResult']['Syakan'] = $output[count($output) -1];
if($output[count($output) -1] > 80){
    $resultdata['DetecResult']['is_Aorare'] = true;
}
else{
    $resultdata['DetecResult']['is_Aorare'] = false;
}

echo json_encode($resultdata, JSON_UNESCAPED_UNICODE);
?>