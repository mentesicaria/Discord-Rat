<?php
$webhook = base64_encode($_POST['webhook']);
$desctruct = $_POST['desctruct'];
$gild = base64_encode($_POST['gild']);
$token = base64_encode($_POST['token']);
$pass = $_POST['password'];

$yourpassword = "a";




if($pass == $yourpassword){
    if($webhook != ""){
        $file = fopen("../private/webhook","w");
        fwrite($file,$webhook);
        fclose($file);
    }elseif($token != ""){
        $file = fopen("../private/token","w");
        fwrite($file,$token);
        fclose($file);
    }elseif($gild != ""){
        $file = fopen("../private/gild","w");
        fwrite($file,$gild);
        fclose($file);
    }elseif($desctruct != ""){
        $file = fopen("desctruct","w");
        fwrite($file,$desctruct);
        fclose($file);
    }
}




?>