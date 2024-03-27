<?php
include_once 'global.php';
if (!isset($_SESSION["user_id"])) {
    header("Location: login.php");
    exit();
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST["mode"])) {
        switch($_POST["mode"]){
            case "done":
                if (is_numeric($_POST["task"])) {
                    $tid = $_POST["task"];
                    $sql = "UPDATE todos SET done = CASE WHEN done = 1 THEN 0 ELSE 1 END WHERE id = $tid AND user_id = " . $_SESSION['user_id'];
            
                    if (!mysqli_query($conn, $sql)) {
                        echo "Error <br>" . mysqli_error($conn);
                    }
                }
                break;
            case "add":
                if (isset($_POST["task"])) {
                    $task = trim(htmlspecialchars($_POST["task"], ENT_QUOTES));
                    $sql = "INSERT INTO todos (user_id, task) VALUES (".$_SESSION['user_id'].", '$task')";
            
                    if (!mysqli_query($conn, $sql)) {
                        echo "Error <br>" . mysqli_error($conn);
                    }
                }
                break;
            case "remove":
                if (is_numeric($_POST["task"])) {
                    $tid = $_POST["task"];
                    $sql = "DELETE FROM todos WHERE id = $tid AND user_id = " . $_SESSION['user_id'];
            
                    if (!mysqli_query($conn, $sql)) {
                        echo "Error <br>" . mysqli_error($conn);
                    }
                }
                break;
            case "changeTheme":
                if (isset($_POST["theme"])) {
                    $theme = $_POST["theme"];
                    switch($theme){
                        case "blue":
                            $theme = "blue.php";
                            break;
                        case "green":
                            $theme = "green.php";
                            break;
                        default:
                            $theme = "red.php";
                            break;
                    }
                    $sql = "UPDATE users SET theme = '$theme' WHERE id = " . $_SESSION['user_id'];
            
                    if (!mysqli_query($conn, $sql)) {
                        echo "Error <br>" . mysqli_error($conn);
                    }
                }
                break;
        }
    }
}
?>
