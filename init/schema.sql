-- Criação do Banco de Dados
CREATE DATABASE IF NOT EXISTS `clean_database`
  /*!40100 DEFAULT CHARACTER SET utf8 */
  /*!80016 DEFAULT ENCRYPTION='N' */;

USE `clean_database`;

-- Tabela de Clientes
CREATE TABLE IF NOT EXISTS `customers` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `customer_birthday` DATE,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Tabela de Carrinhos de Compras
CREATE TABLE IF NOT EXISTS `shopping_carts` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `customer_id` INT(11) NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `shopping_carts_customer_id_foreign` (`customer_id`),
  CONSTRAINT `shopping_carts_customer_id_foreign` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



-- Tabela de Preferências de Compra
CREATE TABLE IF NOT EXISTS `purchase_preferences` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `customer_id` INT(11) NOT NULL,
  `mode_color` VARCHAR(255) NOT NULL,
  `standard_deviation_color` VARCHAR(255) NOT NULL,
  `mode_item_cluster` VARCHAR(255) NOT NULL,
  `standard_deviation_item_cluster` DECIMAL(10, 2) NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `purchase_preferences_customer_id_foreign` (`customer_id`),
  CONSTRAINT `purchase_preferences_customer_id_foreign` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Tabela de Padrões de Compra
CREATE TABLE IF NOT EXISTS `purchase_standards` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `customer_id` INT(11) NOT NULL,
  `average_purchase_item` DECIMAL(10, 2) NOT NULL,
  `mode_payment_method` VARCHAR(255) NOT NULL,
  `average_purchase_gap` DECIMAL(10, 2) NOT NULL,
  `standard_deviation_purchase_gap` DECIMAL(10, 2) NOT NULL,
  `average_purchase_value` DECIMAL(10, 2) NOT NULL,
  `mode_weekly_purchase` VARCHAR(255) NOT NULL,
  `standard_deviation_weekly_purchase` VARCHAR(255) NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `purchase_standards_customer_id_foreign` (`customer_id`),
  CONSTRAINT `purchase_standards_customer_id_foreign` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Tabela de Produtos
CREATE TABLE IF NOT EXISTS `products` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `price` DECIMAL(10, 2) NOT NULL,
  `color` VARCHAR(255) NOT NULL,
  `size` VARCHAR(255) NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Tabela de Itens do Carrinho
CREATE TABLE IF NOT EXISTS `shopping_cart_items` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `shopping_cart_id` INT(11) NOT NULL,
  `product_id` INT(11) NOT NULL,
  `quantity` INT(11) NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `shopping_cart_items_shopping_cart_id_foreign` (`shopping_cart_id`),
  KEY `shopping_cart_items_product_id_foreign` (`product_id`),
  CONSTRAINT `shopping_cart_items_product_id_foreign` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `shopping_cart_items_shopping_cart_id_foreign` FOREIGN KEY (`shopping_cart_id`) REFERENCES `shopping_carts` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;