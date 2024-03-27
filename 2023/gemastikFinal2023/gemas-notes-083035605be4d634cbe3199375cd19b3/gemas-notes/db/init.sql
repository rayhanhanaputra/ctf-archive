USE `gemasnotes`;

DROP TABLE IF EXISTS `User`;
CREATE TABLE `User` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(150) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `Notes`;
CREATE TABLE `Notes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `content` longtext,
  `author` int(11) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `tags` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user` (`author`),
  CONSTRAINT `fk_user` FOREIGN KEY (`author`) REFERENCES `User` (`id`)
);