<?php
include_once 'global.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    $default_theme = "red.php";
	
    $stmt = $conn->prepare("INSERT INTO users (username, password, theme) VALUES (?, ?, ?)");
	$stmt->bind_param("sss", $username, $hashedPassword, $default_theme);
	
    if ($stmt->execute()) {
        $last_user_id = $conn->insert_id;

        $sample_todo = "This is a sample todo 1!";
        $stmt_todo = $conn->prepare("INSERT INTO todos (user_id, task) VALUES (?, ?)");
        $stmt_todo->bind_param("is", $last_user_id, $sample_todo);
        $stmt_todo->execute();

        $sample_todo = "This is a sample todo 2!";
        $stmt_todo = $conn->prepare("INSERT INTO todos (user_id, task) VALUES (?, ?)");
        $stmt_todo->bind_param("is", $last_user_id, $sample_todo);
        $stmt_todo->execute();

        header("Location: login.php?message=Registration successful. Please login.");
    } else {
        header("Location: register.php?error=Username is already taken or an error occurred.");
    }
}
?>
