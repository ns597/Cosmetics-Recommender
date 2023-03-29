-- MySQL dump 10.13  Distrib 8.0.32, for macos13.0 (arm64)
--
-- Host: localhost    Database: cosmetics
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `products`
--
CREATE DATABASE IF NOT EXISTS cosmetics;
USE cosmetics;

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `Label` varchar(11) NOT NULL,
  `Brand` varchar(29) NOT NULL,
  `Name` varchar(117) NOT NULL,
  `Price` int NOT NULL,
  `Rank` varchar(3) NOT NULL,
  `Ingredients` varchar(5491) NOT NULL,
  `Combination` bit(1) NOT NULL,
  `Dry` bit(1) NOT NULL,
  `Normal` bit(1) NOT NULL,
  `Oily` bit(1) NOT NULL,
  `Sensitive` bit(1) NOT NULL,
  PRIMARY KEY (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('Moisturizer', 'GLAMGLOW', 'Glam Purifying Moisturizer', 30, '4.5', 'Water, Alcohol, Citric Acid, Fragrance, Glycerin', 0, 1, 0, 0, 0), ('Moisturizer', 'CLINIQUE', 'Retinol 24 Hour Moisturizer', 65, '3.7', 'Water, Retinol, Hazelnut, Citric Acid, Glycerin', 0, 0, 0, 1, 0), ('Cleanser', 'Cetaphil', 'Hydrating Cleanser', 40, '3.8', 'Water, Alcohol, Sorbic Acid, Glycerin', 0, 1, 0, 0, 0), ('Cleanser', 'Cerave', 'Facial Foaming Cleanser', 17, '4.8', 'Glycerin, Water, Citric Acid, Coumarin, Fragrance', 0, 0, 0, 1, 0);
INSERT INTO `products` VALUES ('Sun protect', 'DRUNK ELEPHANT', 'Umbra Tinte Physical Daily Defense Broad Spectrum Sunscreen SPF 30', 36, 3.6, 'Water,  Almond, Agua, Glycerin', 1,1,1,1,0 );
INSERT INTO `products` VALUES ('Sun protect', 'SHISEIDO', 'Ultimate Sun Protection Cream Broad Spectrum SPF 50+', 36, 3.6, 'Water,  Glycerin, Retinol, Sorbic Acid', 0,1,1,1,0 );
INSERT INTO `products` VALUES ('Treatment', 'FRESH', 'Seaberry Skin Nutrition Booster', 36, 3.6, 'Water,  Niacinamide, Glycerin, Sorbic Acid ', 1,0,1,0,0 );
INSERT INTO `products` VALUES ('Treatment', 'CLARINS', 'Lotus Face Treatment', 36, 3.6, 'Water,  Niacinamide, Retinol, Glycolic Acid ', 1,1,0,0,0 );
INSERT INTO `products` VALUES ('Treatment', 'CLINIQUE', 'Pore Retinol 24 Hour Treatment', 45, 4.6, 'Water, Alcohol, Sorbic Acid, Retinol, Glycolic Acid ', 1,1,0,0,0 );


/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-27 17:46:37
