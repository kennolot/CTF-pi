<?php
$flag = file_get_contents('/flag.txt');
if ($_POST['password'] === 'admin123') {
    echo "Flag: " . htmlspecialchars($flag);
} else {
    echo "Wrong password!";
}
?>

