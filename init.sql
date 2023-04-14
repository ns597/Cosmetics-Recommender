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
INSERT INTO `products` VALUES ('Moisturizer', 'SK-II', 'Facial Treatment Essence', 179, 4.1, 'Galactomyces Ferment Filtrate (Pitera), Butylene Glycol, Pentylene Glycol, Water, Sodium Benzoate, Methylparaben, Sorbic Acid.', 1, 1, 1, 1, 1);
INSERT INTO `products` VALUES ('Moisturizer', 'DRUNK ELEPHANT', 'Protini Polypeptide Cream', 68, 4.4, 'Water, Dicaprylyl Carbonate, Glycerin, Cetearyl Alcohol, Cetearyl Olivate, Sorbitan Olivate, Sclerocarya Birrea Seed Oil, Bacillus/Soybean/ Folic Acid Ferment Extract, Nymphaea Alba Root Extract', 1, 1, 1, 1, 0);
INSERT INTO `products` VALUES ('Moisturizer','DRUNK E22LEPHANT','ProtiniΓäó Polypeptide Cream 2',68,4.4,'Water, Dicaprylyl Carbonate, Glycerin, Cetearyl Alcohol, Cetearyl Olivate, Sorbitan Olivate, Sclerocarya Birrea Seed Oil, Bacillus/Soybean/ Folic Acid Ferment Extract, Nymphaea Alba Root Extract, sh-Oligopeptide-1, sh-Oligopeptide-2, sh-Polypeptide-1, sh-Polypeptide-9, sh-Polypeptide-11, Copper Palmitoyl Heptapeptide-14, Heptapeptide-15 Palmitate, Palmitoyl Tetrapeptide-7, Palmitoyl Tripeptide-1, Alanine, Arginine, Glycine, Histidine, Isoleucine, Phenylalanine, Proline, Serine, Threonine, Valine, Acetyl Glutamine, Coconut Alkanes , Coco-Caprylate/Caprate, Sodium Hyaluronate, Aspartic Acid, Linoleic Acid, Linolenic Acid, Lecithin, Butylene Glycol, Polyvinyl Alcohol, Sodium Lactate, Sodium PCA, PCA, Sorbitan Isostearate, Carbomer, Polysorbate 20, Polysorbate 60, Lactic Acid/Glycolic Acid Copolymer, Hydroxyethyl Acrylate/Sodium Acryloyldimethyl Taurate Copolymer, Xanthan Gum, Isomalt, 1,2-Hexanediol, Caprylyl Glycol, Chlorphenesin, Phenoxyethanol, Tocopherol, Sodium Benzoate, Phenylpropanol, Glyceryl Caprylate, Symphytum Officinale Callus Culture Extract.',1,1,1,1,0);
INSERT INTO `products` VALUES ('Moisturizer','LA MER','Creme de la Mer',175,4.1,'Algae (Seaweed) Extract, Mineral Oil, Petrolatum, Glycerin, Isohexadecane, Microcrystalline Wax, Lanolin Alcohol, Citrus Aurantifolia (Lime) Extract, Sesamum Indicum (Sesame) Seed Oil, Eucalyptus Globulus (Eucalyptus) Leaf Oil, Sesamum Indicum (Sesame) Seed Powder, Medicago Sativa (Alfalfa) Seed Powder, Helianthus Annuus (Sunflower) Seedcake, Prunus Amygdalus Dulcis (Sweet Almond) Seed Meal, Sodium Gluconate, Copper Gluconate, Calcium Gluconate, Magnesium Gluconate, Zinc Gluconate, Magnesium Sulfate, Paraffin, Tocopheryl Succinate, Niacin, Water, Beta-Carotene, Decyl Oleate, Aluminum Distearate, Octyldodecanol, Citric Acid, Cyanocobalamin, Magnesium Stearate, Panthenol, Limonene, Geraniol, Linalool, Hydroxycitronellal, Citronellol, Benzyl Salicylate, Citral, Sodium Benzoate, Alcohol Denat., Fragrance.',1,1,1,1,1);


INSERT INTO `products` VALUES ('Moisturizer','LA MER','The Moisturizing Soft Cream',175,3.8,'Algae (Seaweed) Extract, Cyclopentasiloxane, Petrolatum, Glyceryl Distearate, Phenyl Trimethicone, Butylene Glycol, Hydrogenated Vegetable Oil, Cholesterol, Butyrospermum Parkii (Shea Butter), Steareth-10, Dimethicone, Glyceryl Stearate Se, Polysilicone-11, Sesamum Indicum (Sesame) Seed Oil, Medicago Sativa (Alfalfa) Seed Powder, Helianthus Annuus (Sunflower) Seedcake, Prunus Amygdalus Dulcis (Sweet Almond) Seed Meal, Eucalyptus Globulus (Eucalyptus) Leaf Oil, Sodium Gluconate, Copper Gluconate, Calcium Gluconate, Magnesium Gluconate, Zinc Gluconate, Tocopheryl Succinate, Niacin, Sesamum Indicum (Sesame) Seed Powder, Water, Citrus Aurantifolia (Lime) Peel Extract, Laminaria Digitata Extract, Crithmum Maritimum Extract, Salicornia Herbacea Extract, Plankton Extract, Chlorella Vulgaris Extract, Glycine Soja (Soybean) Seed Extract, Glycerin, Caffeine, Sea Salt/Maris Sal/Sel Marin, Micrococcus Lysate, Diethylhexyl Succinate, Adenosine Phosphate, Creatine, Hydrolyzed Algin, Isocetyl Stearoyl Stearate, Cetyl Alcohol, Sucrose, Acetyl Hexapeptide-8, Glucose Oxidase, Polyacrylamide, Acetyl Carnitine Hcl, Glucose, Caprylic/Capric Triglyceride, C13-14 Isoparaffin, Tocopheryl Acetate, Tetrahexyldecyl Ascorbate, Sodium Pca, Glycosaminoglycans, Urea, Distearyldimonium Chloride, Dipalmitoyl Hydroxyproline, Sodium Hyaluronate, Laureth-7, Lecithin, Trehalose, Polyquaternium-51, Lactoperoxidase, Hydroxypropyl Cyclodextrin, Cyanocobalamin, Pentylene Glycol, Fragrance, Disodium Edta, Bht, Citronellol, Hydroxycitronellal, Geraniol, Linalool, Limonene, Potassium Sorbate, Phenoxyethanol',1,1,1,1,1),('Moisturizer','IT COSMETICS','Your Skin But BetterΓäó CC+Γäó Cream with SPF 50+',38,4.1,'Water, Snail Secretion Filtrate, Phenyl Trimethicone, Dimethicone, Butylene Glycol, Butylene Glycol Dicaprylate/Dicaprate, Orbignya Oleifera Seed Oil, Butyloctyl Salicylate, Cetyl Peg/Ppg-10/1 Dimethicone, Cyclopentasiloxane, Cyclohexasiloxane, Magnesium Sulfate, Polyglyceryl-4 Isostearate, Dimethicone/Vinyl Dimethicone Crosspolymer, Aluminum Hydroxide, Hexyl Laurate, Stearic Acid, Calcium Stearate, Caprylyl Glycol, Triethoxycaprylylsilane, Ethylhexylglycerin, Citrus Medica Limonum (Lemon) Peel Oil, Tocopheryl Acetate, Sorbitan Isostearate, Phenoxyethanol, Citrus Aurantium Bergamia (Bergamot) Fruit Oil, 1,2-Hexanediol, Disodium Edta, Citrus Aurantium Dulcis (Orange) Peel Oil, Citrus Aurantifolia (Lime) Oil, Vitis Vinifera (Grape) Seed Oil, Punica Granatum Seed Oil, Pinus Sylvestris Leaf Oil, Persea Gratissima (Avocado) Oil, Niacinamide, Citrus Grandis (Grapefruit) Peel Oil, Cholesterol, Anthemis Nobilis Flower Water, Lactobacillus/Honeysuckle Flower/Licorice Root/Morus Alba Root/Pueraria Lobata Root/Schizandra Chinensis Fruit/Scutellaria Baicalensis Root/Sophora Japonica Flower Extract Ferment Filtrate, Perfluorohexane, Olea Europaea (Olive) Leaf Extract, Glycerin, Eucalyptus Globulus Leaf Oil, Camellia Sinensis Leaf Extract, Chrysanthemum Indicum Flower Extract, Pueraria Lobata Root Extract, Perfluorodecalin, Morus Alba Fruit Extract, Magnolia Kobus Bark Extract, Glycine Soja (Soybean) Sprout Extract, Diospyros Kaki Leaf Extract, Cinnamomum Cassia Bark Extract, Artemisia Princeps Leaf Extract, Pentafluoropropane, Curcuma Longa (Turmeric) Root Extract, Steareth-20, Hydrolyzed Hyaluronic Acid, Colloidal Oatmeal, Hydrolyzed Silk, Citric Acid, Sodium Benzoate, Potassium Sorbate, Aloe Barbadensis Leaf Extract, N-Hydroxysuccinimide, Hydrolyzed Collagen, Caprylhydroxamic Acid, Tocopherol, Thiamine Hcl, Riboflavin, Retinyl Palmitate, Pantothenic Acid, Palmitoyl Oligopeptide, Niacin, Folic Acid, Chrysin, Carnitine Hcl, Biotin, Ascorbic Acid, Palmitoyl Tetrapeptide-7, Chlorhexidine Digluconate. May Contain: Iron Oxides (Ci 77492, Ci 77491, Ci 77499).',1,1,1,1,1),('Moisturizer','TATCHA','The Water Cream',68,4.2,'Water, Saccharomyces/Camellia Sinensis Leaf/Cladosiphon Okamuranus/Rice Ferment Filtrate*, Dimethicone, Propanediol, Glycerin, Diglycerin, Diphenylsiloxy Phenyl Trimethicone, Gold, Belamcanda Chinensis Root Extract, Rosa Multiflora Fruit Extract, Houttuynia Cordata Extract, Sophora Angustifolia Root Extract, Sodium Hyaluronate, Lecithin, Pistacia Lentiscus (Mastic) Gum, Sodium Chloride, Sodium Citrate, Mica, Peg-9 Polydimethylsiloxyethyl Dimethicone, Dimethicone/Peg-10/15 Crosspolymer, Dimethicone/Phenyl Vinyl Dimethicone Crosspolymer, Disodium Edta, Tin Oxide, Titanium Dioxide, Butylene Glycol, Ethylhexylglycerin, Parfum/Fragrance, Alcohol, Phenoxyethanol. *Hadasei-3.',1,0,1,1,1),('Moisturizer','DRUNK ELEPHANT','Lala RetroΓäó Whipped Cream',60,4.2,'Water, Glycerin, Caprylic/ Capric Triglyceride, Isopropyl Isostearate, Pseudozyma Epicola/Camellia Sinensis Seed Oil/Glucose/Glycine Soja Meal/Malt Extract/Yeast Extract Ferment Filtrate (Pseudozyma Epicola/Camellia Sinensis Seed Oil/Glucose/Yeast Extract Ferment Filtrate), Stearic Acid, Glyceryl Stearate SE, Cetearyl Alcohol, Pentylene Glycol, Plantago Lanceolata Leaf Extract, Adansonia Digitata Seed Oil, Citrullus Lanatus (Watermelon) Seed Oil, Passiflora Edulis Seed Oil, Schinziophyton Rautanenii Kernel Oil, Sclerocarya Birrea Seed Oil, Polyglyceryl-6 Ximenia Americana Seedate, Sodium Hyaluronate Crosspolymer, Ceteareth-20, Trisodium Ethylenediamine Disuccinate, Sodium Hydroxide, Citric Acid, Carbomer, Xanthan Gum, Caprylyl Glycol, Chlorphenesin, Phenoxyethanol, Ethylhexylglycerin.',1,1,1,1,0),('Moisturizer','DRUNK ELEPHANT','Virgin Marula Luxury Facial Oil',72,4.4,'100% Unrefined Sclerocraya Birrea (Marula) Kernel Oil.',1,1,1,1,0),('Moisturizer','KIEHLS SINCE 1851','Ultra Facial Cream',29,4.4,'Water, Glycerin, Cyclohexasiloxane, Squalane, Bis-Peg-18 Methyl Ether Dimethyl Silane, Sucrose Stearate, Stearyl Alcohol, Peg-8 Stearate, Urea, Myristyl Myristate, Pentaerythrityl Tetraethylhexanoate, Prunus Armeniaca Kernel Oil, Phenoxyethanol, Persea Gratissima Oil, Olea Europaea Oil, Oryza Sativa Bran Oil, Cetyl Alcohol, Glyceryl Stearate, Imperata Cylindrica Root Extract, Stearic Acid, Methylparaben, Chlorphenesin, Palmitic Acid, Disodium Edta, Acrylates/C10-30 Alkyl Acrylate Crosspolymer, Propylparaben, Carbomer, Triethanolamine, Prunus Amygdalus Dulcis Oil, Xanthan Gum, Sodium Hydroxide, Tocopherol, Pseudoalteromonas Ferment Extract, Hydroxypalmitoyl Sphinganine, Caprylyl Glycol.',1,1,1,1,1),('Moisturizer','LA MER','Little Miss Miracle Limited-Edition Cr├¿me de la Mer',325,5.0,'Algae (Seaweed) Extract, Mineral Oil, Petrolatum, Glycerin, Isohexadecane, Microcrystalline Wax, Lanolin Alcohol, Citrus Aurantifolia (Lime) Extract, Sesamum Indicum (Sesame) Seed Oil, Eucalyptus Globulus (Eucalyptus) Leaf Oil, Sesamum Indicum (Sesame) Seed Powder, Medicago Sativa (Alfalfa) Seed Powder, Helianthus Annuus (Sunflower) Seedcake, Prunus Amygdalus Dulcis (Sweet Almond) Seed Meal, Sodium Gluconate, Copper Gluconate, Calcium Gluconate, Magnesium Gluconate, Zinc Gluconate, Magnesium Sulfate, Paraffin, Tocopheryl Succinate, Niacin, Water, Beta-Carotene, Decyl Oleate, Aluminum Distearate, Octyldodecanol, Citric Acid, Cyanocobalamin, Magnesium Stearate, Panthenol, Limonene, Geraniol, Linalool, Hydroxycitronellal, Citronellol, Benzyl Salicylate, Citral, Sodium Benzoate, Alcohol Denat., Fragrance.',0,0,0,0,0),('Moisturizer','FRESH','Lotus Youth Preserve Moisturizer',45,4.3,'Water, Glycerin, Propylene Glycol Dicaprylate/Dicaprate, Pentylene Glycol, Cetearyl Alcohol, Caprylic/Capric Triglyceride, Cetearyl Isononanoate, Betaine, Polymethyl Methacrylate, Steareth-21, Ficus Carica (Fig) Fruit Extract, Lepidium Meyenii Root Extract, Citrus Limon (Lemon) Peel Oil, Cucumis Sativus (Cucumber) Fruit Extract, Algae Extract, Nelumbo Nucifera Flower Extract, Hibiscus Esculentus Fruit Extract, Sodium Hyaluronate, Tocopheryl Acetate, Ascorbyl Tetraisopalmitate, Tocopherol, Behenyl Alcohol, Cetearyl Glucoside, Sorbitol, Dimethicone, Sodium PCA, Caprylyl Glycol, Carbomer, Tromethamine, Cetyl Alcohol, Stearyl Alcohol, Butylene Glycol, Xanthan Gum, Caramel, Citric Acid, Potassium Sorbate, Sorbic Acid, Phenoxyethanol, Limonene, Citral.',0,0,0,0,0);






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
