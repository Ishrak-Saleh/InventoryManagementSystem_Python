CREATE DATABASE  IF NOT EXISTS `mydata` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mydata`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mydata
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `pharma`
--

DROP TABLE IF EXISTS `pharma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pharma` (
  `REF` int NOT NULL,
  `MEDI_NAME` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`REF`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pharma`
--

LOCK TABLES `pharma` WRITE;
/*!40000 ALTER TABLE `pharma` DISABLE KEYS */;
INSERT INTO `pharma` VALUES (111024559,'Escitalopram'),(247198222,'Amoxicillin'),(341844389,'Pembrolizumab'),(374819247,'Bupropion'),(836483213,'Amlodipine'),(867453219,'Rosuvastatin'),(962003009,'Metformin'),(1716505078,'Atorvastatin');
/*!40000 ALTER TABLE `pharma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pharmacy`
--

DROP TABLE IF EXISTS `pharmacy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pharmacy` (
  `REF` int NOT NULL,
  `COMPANY` varchar(45) DEFAULT NULL,
  `MEDI_TYPE` varchar(45) DEFAULT NULL,
  `MEDI_NAME` varchar(45) DEFAULT NULL,
  `LOT_NUMBER` varchar(45) DEFAULT NULL,
  `ISSUED` varchar(45) DEFAULT NULL,
  `EXPIRES` varchar(45) DEFAULT NULL,
  `USES` varchar(45) DEFAULT NULL,
  `SIDE_EFFECT` varchar(45) DEFAULT NULL,
  `WARNING` varchar(45) DEFAULT NULL,
  `DOSAGE` varchar(45) DEFAULT NULL,
  `PRICE` varchar(45) DEFAULT NULL,
  `QUANTITY` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`REF`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pharmacy`
--

LOCK TABLES `pharmacy` WRITE;
/*!40000 ALTER TABLE `pharmacy` DISABLE KEYS */;
INSERT INTO `pharmacy` VALUES (111024559,'AstraZeneca','TABLET','Escitalopram','312841234','16/12/2021','16/12/2024','Sinusitis','Cervical Spindolysis','Dr. Mehta','2','Tk 3400','6'),(247198222,'Novartis','TOPICAL MEDICINES','Amoxicillin','138223849','09/11/2021','09/11/2027','Chronic Arthritis','Low Blood Pressure','Dr. Kumar','1','Tk 5625','3'),(374819247,'Novartis','DROPS','Bupropion','391234310','09/11/2022','09/11/2024','Blood Cancer','Nausea, Mild Allergies','Dr. Jefferson','3','Tk 1200','45'),(836483213,'Bayer','INHALERS','Amlodipine','228312823','16/02/2023','16/02/2025','Asthma','Nausea','Dr. Chowdhury','2','Tk 650','11'),(867453219,'Bayer','INJECTION','Rosuvastatin','231444345','05/07/2023','05/07/2028','Typhoid','Dry Lips, Loss of Appetite','Dr. Miguel','4','Tk 1200','8'),(962003009,'GSK','LIQUID','Metformin','343444321','05/07/2022','05/07/2024','Dry Cough','N/A','Dr. Hasan','2','Tk 1350','5'),(1716505078,'GSK','DROPS','Atorvastatin','111223098','04/03/2021','04/03/2025','Pain Killer','Numbness, Loss of Appetite','Dr. Jamal','1','Tk 340','25');
/*!40000 ALTER TABLE `pharmacy` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-20 21:14:31
