<?php
include_once 'global.php';

if ($_SERVER["REQUEST_METHOD"] == "GET") {
    if(isset($_GET['username'])){
        $username = $_GET["username"];
        if($username == 'guest'){
            header("Location: index.php?message=User guest can't unregister.");
        }else{
            $stmt = $conn->prepare("DELETE FROM users WHERE username = ? AND id = ?");
            $stmt->bind_param("si", $username, $_SESSION['user_id']);
            
            if ($stmt->execute()) {
                session_destroy();
                header("Location: login.php?message=Unregister successful.");
            } else {
                header("Location: login.php?message=Something went wrong.");
            }
        }
    }else{
        header("Location: index.php");
    }
}
?>