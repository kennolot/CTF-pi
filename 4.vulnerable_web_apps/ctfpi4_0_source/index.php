<?php
if (isset($_GET['source'])) {
    highlight_file(__FILE__);
    exit;
}

$flag = file_get_contents('/flag.txt');

$message = "Enter the password to retrieve the flag.";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['password']) && $_POST['password'] === 'admin123') {
        $message = "Flag: " . $flag;
    } else {
        $message = "Wrong password!";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>CTF-pi php app</title>
</head>
<body>
    <h2><?php echo $message; ?></h2>
    <form method="POST">
        <input type="text" name="password" placeholder="Enter password">
        <button type="submit">Submit</button>
    </form>
</body>
</html>

