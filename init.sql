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
CREATE TABLE products (
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
INSERT INTO `products` VALUES ('Moisturizer', 'GLAMGLOW', '(Glam Purifying Moisturizer', 30, '4.5', 'Water(Alcohol), Citric Acid, Mineral Oil, Fragrance, Glycerin', 0, 1, 1, 0, 1);
INSERT INTO `products` VALUES ('Moisturizer', 'CLINIQUE', 'Retinol 24 Hour Moisturizer', 65, '3.7', 'Water, Retinol, Hazelnut, Citric Acid, Glycerin', 1, 0, 0, 1, 0);
-- INSERT INTO `products` VALUES ('Moisturizer', 'LA MER', 'Creme de la Mer', 175, 4.1, "Algae (Seaweed) Extract, Mineral Oil, Petrolatum, Glycerin, Sodium Gluconate, Niacin, Water, Octyldodecanol, Citric Acid, Fragrance",1,1,1,1,1);
INSERT INTO `products` VALUES ('Cleanser', 'Cetaphil', 'Hydrating Cleanser', 40, '3.8', 'Water, Alcohol, Sorbic Acid, Glycerin', 1, 1, 0, 0, 1);
INSERT INTO `products` VALUES ('Cleanser', 'Cerave', 'Facial Foaming Cleanser', 17, '4.8', 'Glycerin, Water, Citric Acid, Coumarin, Fragrance', 0, 0, 1, 1, 0);
INSERT INTO `products` VALUES ('Sun protect', 'DRUNK ELEPHANT', 'Umbra Tinte Physical Daily Defense Broad Spectrum Sunscreen SPF 30', 36, 3.6, 'Water,  Almond, Agua, Glycerin', 1,1,1,1,0 );
INSERT INTO `products` VALUES ('Sun protect', 'SHISEIDO', 'Ultimate Sun Protection Cream Broad Spectrum SPF 50+', 36, 3.6, 'Water,  Glycerin, Retinol, Sorbic Acid', 0,1,1,0,1 );
INSERT INTO `products` VALUES ('Treatment', 'FRESH', 'Seaberry Skin Nutrition Booster', 36, 3.6, 'Water, Niacinamide, Glycerin, Sorbic Acid, Mineral Oil, Fragrance', 1,0,0,1,0 );
INSERT INTO `products` VALUES ('Treatment', 'CLARINS', 'Lotus Face Treatment', 36, 3.6, 'Water,  Niacinamide, Retinol, Glycolic Acid ', 1,0,0,0,1 );
INSERT INTO `products` VALUES ('Treatment', 'CLINIQUE', 'Pore Retinol 24 Hour Treatment', 45, 4.6, 'Water, Alcohol, Sorbic Acid, Retinol, Glycolic Acid ', 0,1,1,0,0 );
INSERT INTO `products` VALUES ('Moisturizer', 'SK-II', 'Facial Treatment Essence', 179, 4.1, 'Galactomyces Ferment Filtrate (Pitera), Butylene Glycol, Pentylene Glycol, Water, Sodium Benzoate, Methylparaben, Sorbic Acid.', 1, 1, 1, 1, 1)
INSERT INTO `products` VALUES ('Moisturizer', 'DRUNK ELEPHANT', 'Protini Polypeptide Cream', 68, 4.4, 'Water, Dicaprylyl Carbonate, Glycerin, Cetearyl Alcohol, Cetearyl Olivate, Sorbitan Olivate, Sclerocarya Birrea Seed Oil, Bacillus/Soybean/ Folic Acid Ferment Extract, Nymphaea Alba Root Extract', 1, 1, 1, 1, 0)
INSERT INTO `products` VALUES ('Moisturizer','DRUNK E22LEPHANT','ProtiniΓäó Polypeptide Cream 2',68,4.4,'Water, Dicaprylyl Carbonate, Glycerin, Cetearyl Alcohol, Cetearyl Olivate, Sorbitan Olivate, Sclerocarya Birrea Seed Oil, Bacillus/Soybean/ Folic Acid Ferment Extract, Nymphaea Alba Root Extract, sh-Oligopeptide-1, sh-Oligopeptide-2, sh-Polypeptide-1, sh-Polypeptide-9, sh-Polypeptide-11, Copper Palmitoyl Heptapeptide-14, Heptapeptide-15 Palmitate, Palmitoyl Tetrapeptide-7, Palmitoyl Tripeptide-1, Alanine, Arginine, Glycine, Histidine, Isoleucine, Phenylalanine, Proline, Serine, Threonine, Valine, Acetyl Glutamine, Coconut Alkanes , Coco-Caprylate/Caprate, Sodium Hyaluronate, Aspartic Acid, Linoleic Acid, Linolenic Acid, Lecithin, Butylene Glycol, Polyvinyl Alcohol, Sodium Lactate, Sodium PCA, PCA, Sorbitan Isostearate, Carbomer, Polysorbate 20, Polysorbate 60, Lactic Acid/Glycolic Acid Copolymer, Hydroxyethyl Acrylate/Sodium Acryloyldimethyl Taurate Copolymer, Xanthan Gum, Isomalt, 1,2-Hexanediol, Caprylyl Glycol, Chlorphenesin, Phenoxyethanol, Tocopherol, Sodium Benzoate, Phenylpropanol, Glyceryl Caprylate, Symphytum Officinale Callus Culture Extract.',1,1,1,1,0)
INSERT INTO `products` VALUES ('Moisturizer','LA MER','Creme de la Mer',175,4.1,'Algae (Seaweed) Extract, Mineral Oil, Petrolatum, Glycerin, Isohexadecane, Microcrystalline Wax, Lanolin Alcohol, Citrus Aurantifolia (Lime) Extract, Sesamum Indicum (Sesame) Seed Oil, Eucalyptus Globulus (Eucalyptus) Leaf Oil, Sesamum Indicum (Sesame) Seed Powder, Medicago Sativa (Alfalfa) Seed Powder, Helianthus Annuus (Sunflower) Seedcake, Prunus Amygdalus Dulcis (Sweet Almond) Seed Meal, Sodium Gluconate, Copper Gluconate, Calcium Gluconate, Magnesium Gluconate, Zinc Gluconate, Magnesium Sulfate, Paraffin, Tocopheryl Succinate, Niacin, Water, Beta-Carotene, Decyl Oleate, Aluminum Distearate, Octyldodecanol, Citric Acid, Cyanocobalamin, Magnesium Stearate, Panthenol, Limonene, Geraniol, Linalool, Hydroxycitronellal, Citronellol, Benzyl Salicylate, Citral, Sodium Benzoate, Alcohol Denat., Fragrance.',1,1,1,1,1)









-- LOAD DATA INFILE './csv/cosmetics_clean.csv' 
-- INTO TABLE `products` 
-- FIELDS TERMINATED BY ',' 
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS;

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
