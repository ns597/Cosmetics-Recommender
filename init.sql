-- MySQL dump 10.13  Distrib 8.0.32, for macos13.0 (arm64)
--
-- Host: localhost    Database: cosmetics
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `cosmetics`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `cosmetics` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `cosmetics`;

--
-- Table structure for table `products`
--

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('Cleanser','Cerave','Facial Foaming Cleanser',17,'4.8','Glycerin, Water, Citric Acid, Coumarin, Fragrance',_binary '\0',_binary '\0',_binary '\0',_binary '',_binary '\0'),('Moisturizer','GLAMGLOW','Glam Purifying Moisturizer',30,'4.5','Water, Alcohol, Citric Acid, Fragrance, Glycerin',_binary '\0',_binary '',_binary '\0',_binary '\0',_binary '\0'),('Cleanser','Cetaphil','Hydrating Cleanser',40,'3.8','Water, Alcohol, Sorbic Acid, Glycerin',_binary '\0',_binary '',_binary '\0',_binary '\0',_binary '\0'),('Treatment','CLARINS','Lotus face Treatment',36,'3.6','Water,  Niacinamide, Retinol, Glycolic Acid ',_binary '',_binary '',_binary '\0',_binary '\0',_binary '\0'),('Moisturizer','CLINIQUE','Retinol 24 Hour Moisturizer',65,'3.7','Water, Retinol, Hazelnut, Citric Acid, Glycerin',_binary '\0',_binary '\0',_binary '\0',_binary '',_binary '\0'),('Treatment','FRESH','Seaberry Skin Nutrition Booster',36,'3.6','Water,  Niacinamide, Glycerin, Sorbic Acid ',_binary '',_binary '\0',_binary '',_binary '\0',_binary '\0'),('Sun protect','SHISEIDO','Ultimate Sun Protection Cream Broad Spectrum SPF 50+',36,'3.6','Water,  Glycerin, Retinol, Sorbic Acid',_binary '\0',_binary '',_binary '',_binary '',_binary '\0');
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

-- Dump completed on 2023-03-27 21:17:18
