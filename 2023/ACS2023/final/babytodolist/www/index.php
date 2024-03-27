<?php
$preview = false;
include_once 'global.php';
if (!isset($_SESSION["user_id"])) {
    header("Location: login.php");
    exit();
}

$todos_fetch = mysqli_query($conn, "SELECT * FROM todos WHERE user_id = " . $_SESSION["user_id"]);
$todos_row = @mysqli_fetch_all($todos_fetch, MYSQLI_ASSOC);

$users_fetch = mysqli_query($conn, "SELECT * FROM users WHERE id = " . $_SESSION["user_id"]);
$user = @mysqli_fetch_array($users_fetch);

include_once 'theme.header.php';
include_once "./themes/".($preview?$theme['fname']:$user["theme"]);
include_once 'theme.footer.php';
?>

