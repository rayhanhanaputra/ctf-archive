CREATE DATABASE IF NOT EXISTS CTF;
USE `CTF`;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    theme VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    task VARCHAR(255) NOT NULL,
    done TINYINT(1) DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS themes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tname VARCHAR(50) NOT NULL,
    fname VARCHAR(255) NOT NULL,
    last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO themes (tname, fname, last_modified) VALUES ("red", "red.php", NOW());
INSERT INTO themes (tname, fname, last_modified) VALUES ("blue", "blue.php", NOW());
INSERT INTO themes (tname, fname, last_modified) VALUES ("green", "green.php", NOW());
INSERT INTO users (username, password, theme) VALUES ("guest", "$2y$10$umvHLKrgRd7Qv.8/G37meeF0g1HYgj1s/8K/XuSFIOpW4t0o8zRdu", "red.php");
INSERT INTO todos (user_id, task) VALUES (1, "This is a sample todo 1!");
INSERT INTO todos (user_id, task) VALUES (1, "This is a sample todo 2!");