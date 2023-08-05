<?php
// Writed By Kanata Saito
function uuidmake(){
    $pattern = "xxxxxxxx_xxxx_4xxx_yxxx_xxxxxxxxxxxx";
    $character_array = str_split($pattern);
    $uuid = "";
    foreach($character_array as $character) {
        switch($character) {
            case "x":
                $uuid .= dechex(random_int(0, 15));
                break;
    
            case "y":
                $uuid .= dechex(random_int(8, 11));
                break;
    
            default:
                $uuid .= $character;
        }
    }
    return $uuid;
}
?>