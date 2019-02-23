<?php

$username = $_POST['username'];
$password = $_POST['password'];

if($username == "suma" && $password== "123456789") {
echo "Login Success !";
}else{
echo "Login Failed";
}

?>
