CREATE DATABASE IF NOT EXISTS `clean_database` /*!40100 DEFAULT CHARACTER SET utf8 */;

CREATE TABLE IF NOT EXISTS `clean_database`.`users` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `age` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
);
