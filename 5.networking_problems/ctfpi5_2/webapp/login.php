<?php
$username = $_POST['username'];
$password = $_POST['password'];

file_put_contents('/tmp/creds.txt', "Username: $username, Password: $password\n", FILE_APPEND);

if ($username === "admin" && $password === "4am_SECRET_sandw3ch.1") {
    echo "<h1>Access Granted!</h1>";
    $flag = file_get_contents("/tmp/flag.txt");
    echo $flag;
} else {
    echo "<h1>Login failed</h1>";
}
?>
