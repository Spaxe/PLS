-- MySQL dump 10.16  Distrib 10.1.17-MariaDB, for osx10.10 (x86_64)
--
-- Host: localhost    Database: PLS
-- ------------------------------------------------------
-- Server version	10.1.17-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `congestion_pricing`
--

DROP TABLE IF EXISTS `congestion_pricing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `congestion_pricing` (
  `priority` int(11) NOT NULL,
  `non_priority` int(11) NOT NULL,
  `dynamic_price` double NOT NULL,
  `static_price` double DEFAULT NULL,
  PRIMARY KEY (`priority`,`dynamic_price`,`non_priority`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `congestion_pricing`
--

LOCK TABLES `congestion_pricing` WRITE;
/*!40000 ALTER TABLE `congestion_pricing` DISABLE KEYS */;
INSERT INTO `congestion_pricing` VALUES (70,30,20,40),(75,35,35,50),(75,80,47,33),(80,20,30,45),(80,80,55,44);
/*!40000 ALTER TABLE `congestion_pricing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `current_non_priority_congestion`
--

DROP TABLE IF EXISTS `current_non_priority_congestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `current_non_priority_congestion` (
  `congestion` double NOT NULL,
  `timestamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `current_non_priority_congestion`
--

LOCK TABLES `current_non_priority_congestion` WRITE;
/*!40000 ALTER TABLE `current_non_priority_congestion` DISABLE KEYS */;
INSERT INTO `current_non_priority_congestion` VALUES (33,'2016-10-09 01:27:35'),(15.7,'2016-10-09 01:29:59'),(3,'2016-10-09 02:14:10'),(3,'2016-10-09 02:19:11'),(3,'2016-10-09 02:26:58'),(3,'2016-10-09 02:27:14'),(3,'2016-10-09 02:27:24'),(3,'2016-10-09 02:28:18'),(3,'2016-10-09 02:29:18'),(3,'2016-10-09 02:30:18'),(3,'2016-10-09 02:31:20'),(3,'2016-10-09 02:32:19'),(3,'2016-10-09 02:33:18'),(3,'2016-10-09 02:34:18'),(3,'2016-10-09 02:35:18'),(3,'2016-10-09 02:36:18'),(3,'2016-10-09 02:37:19'),(3,'2016-10-09 02:38:19'),(3,'2016-10-09 02:39:26'),(3,'2016-10-09 02:40:22'),(3,'2016-10-09 02:41:18'),(3,'2016-10-09 02:42:19'),(3,'2016-10-09 02:43:20'),(3,'2016-10-09 02:44:18'),(3,'2016-10-09 02:45:19'),(3,'2016-10-09 02:46:19'),(3,'2016-10-09 02:47:20'),(3,'2016-10-09 02:48:18'),(3,'2016-10-09 02:49:21'),(3,'2016-10-09 02:50:19'),(3,'2016-10-09 02:51:22'),(3,'2016-10-09 02:52:31'),(3,'2016-10-09 02:53:28'),(3,'2016-10-09 02:54:21'),(3,'2016-10-09 02:55:30'),(3,'2016-10-09 02:56:29'),(3,'2016-10-09 02:57:19'),(3,'2016-10-09 02:58:34'),(3,'2016-10-09 02:59:29'),(3,'2016-10-09 03:00:22'),(3,'2016-10-09 03:01:24'),(3,'2016-10-09 07:16:17'),(3,'2016-10-09 07:17:14'),(3,'2016-10-09 07:18:18'),(3,'2016-10-09 07:19:27'),(3,'2016-10-09 07:20:15'),(3,'2016-10-09 07:21:18'),(3,'2016-10-09 07:22:19'),(3,'2016-10-09 07:23:15'),(3,'2016-10-09 07:24:15'),(3,'2016-10-09 07:25:23'),(3,'2016-10-09 07:26:15'),(3,'2016-10-09 07:27:13'),(3,'2016-10-09 07:28:13'),(3,'2016-10-09 07:29:14'),(3,'2016-10-09 07:30:21'),(3,'2016-10-09 07:31:20'),(3,'2016-10-09 07:32:23'),(3,'2016-10-09 07:33:16'),(3,'2016-10-09 07:34:14'),(3,'2016-10-09 07:35:14'),(3,'2016-10-09 07:36:19'),(3,'2016-10-09 07:37:27'),(3,'2016-10-09 07:38:23'),(3,'2016-10-09 07:40:18'),(3,'2016-10-09 07:40:43'),(3,'2016-10-09 07:41:42'),(3,'2016-10-09 07:42:45'),(3,'2016-10-09 07:43:44'),(3,'2016-10-09 07:44:51'),(3,'2016-10-09 07:45:52'),(3,'2016-10-09 07:46:47'),(3,'2016-10-09 07:47:18'),(3,'2016-10-09 07:48:19'),(3,'2016-10-09 07:49:18'),(3,'2016-10-09 07:50:26'),(3,'2016-10-09 07:51:20'),(3,'2016-10-09 07:52:20'),(3,'2016-10-09 07:53:27'),(3,'2016-10-09 07:54:21'),(3,'2016-10-09 07:55:18'),(3,'2016-10-09 07:56:19'),(3,'2016-10-09 07:57:23'),(3,'2016-10-09 07:58:18'),(3,'2016-10-09 07:59:27'),(3,'2016-10-09 08:00:18'),(3,'2016-10-09 08:01:18'),(3,'2016-10-09 08:02:20'),(3,'2016-10-09 08:03:20'),(3,'2016-10-09 08:04:19'),(3,'2016-10-09 08:05:19'),(3,'2016-10-09 08:06:20'),(3,'2016-10-09 08:07:17'),(3,'2016-10-09 08:08:17'),(3,'2016-10-09 08:09:18'),(3,'2016-10-09 08:10:17'),(3,'2016-10-09 08:11:19'),(3,'2016-10-09 08:12:20'),(3,'2016-10-09 08:13:19'),(3,'2016-10-09 08:14:19'),(3,'2016-10-09 08:15:17'),(3,'2016-10-09 08:16:25'),(3,'2016-10-09 08:17:18'),(3,'2016-10-09 08:18:21'),(3,'2016-10-09 08:19:20'),(3,'2016-10-09 08:20:26'),(3,'2016-10-09 08:21:21'),(3,'2016-10-09 08:22:18'),(3,'2016-10-09 08:23:25'),(3,'2016-10-09 08:24:18'),(3,'2016-10-09 08:25:23'),(3,'2016-10-09 08:26:21'),(3,'2016-10-09 08:27:20'),(3,'2016-10-09 08:28:16'),(3,'2016-10-09 08:29:32'),(3,'2016-10-09 08:30:18'),(3,'2016-10-09 08:31:19'),(3,'2016-10-09 08:32:25'),(3,'2016-10-09 08:33:25'),(3,'2016-10-09 08:34:20'),(3,'2016-10-09 08:34:46'),(3,'2016-10-09 08:36:46'),(3,'2016-10-09 08:36:49'),(3,'2016-10-09 08:37:50'),(3,'2016-10-09 08:38:48'),(3,'2016-10-09 08:39:50'),(3,'2016-10-09 08:40:49'),(3,'2016-10-09 08:41:49'),(3,'2016-10-09 08:42:49'),(3,'2016-10-09 08:43:47'),(3,'2016-10-09 08:44:49'),(3,'2016-10-09 08:45:51');
/*!40000 ALTER TABLE `current_non_priority_congestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `current_price`
--

DROP TABLE IF EXISTS `current_price`;
/*!50001 DROP VIEW IF EXISTS `current_price`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `current_price` (
  `dynamic_price` tinyint NOT NULL,
  `static_price` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `current_priority_congestion`
--

DROP TABLE IF EXISTS `current_priority_congestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `current_priority_congestion` (
  `congestion` double NOT NULL,
  `timestamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `current_priority_congestion`
--

LOCK TABLES `current_priority_congestion` WRITE;
/*!40000 ALTER TABLE `current_priority_congestion` DISABLE KEYS */;
INSERT INTO `current_priority_congestion` VALUES (5,'2016-10-09 00:59:35'),(15,'2016-10-09 01:11:05'),(20,'2016-10-08 22:11:32'),(73,'2016-10-08 22:11:32'),(75,'2016-10-08 23:14:55'),(77,'2016-10-08 23:11:03'),(11.11,'2016-10-09 01:30:27'),(5,'2016-10-09 07:37:17'),(5,'2016-10-09 07:37:17');
/*!40000 ALTER TABLE `current_priority_congestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `journey`
--

DROP TABLE IF EXISTS `journey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `journey` (
  `distance_travelled` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `journey`
--

LOCK TABLES `journey` WRITE;
/*!40000 ALTER TABLE `journey` DISABLE KEYS */;
INSERT INTO `journey` VALUES (15),(16),(0),(0),(15),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(10),(10),(10),(10),(10),(10),(10),(10),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(1),(1),(1),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(1),(1),(1),(10),(0),(0),(1),(5),(5),(5),(5),(5),(0.1);
/*!40000 ALTER TABLE `journey` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `PLS`.`journey_AFTER_INSERT` AFTER INSERT ON `journey` FOR EACH ROW

BEGIN
IF NEW.distance_travelled = 0 THEN
	SELECT static_price *(5/60) INTO @journey_cost FROM current_price;
ELSE
	SELECT dynamic_price * NEW.distance_travelled INTO @journey_cost FROM current_price;
END IF;
UPDATE user SET current_journey_distance = current_journey_distance + NEW.distance_travelled;
UPDATE user SET current_journey_cost=current_journey_cost + @journey_cost;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `registration_number` int(11) NOT NULL,
  `in_priority_lane` blob,
  `mastercard_token` double DEFAULT NULL,
  `account_balance` double DEFAULT NULL,
  `current_journey_cost` double DEFAULT NULL,
  `current_journey_distance` double DEFAULT NULL,
  PRIMARY KEY (`registration_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1234,NULL,34835,30,1801.8333329000004,143.1);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `current_price`
--

/*!50001 DROP TABLE IF EXISTS `current_price`*/;
/*!50001 DROP VIEW IF EXISTS `current_price`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `pls`.`current_price` AS select `pls`.`congestion_pricing`.`dynamic_price` AS `dynamic_price`,`pls`.`congestion_pricing`.`static_price` AS `static_price` from ((`pls`.`congestion_pricing` join `pls`.`current_priority_congestion` on(((round(((`pls`.`current_priority_congestion`.`congestion` / 5) + 0.5),0) * 5) = `pls`.`congestion_pricing`.`priority`))) join `pls`.`current_non_priority_congestion` on(((round(((`pls`.`current_non_priority_congestion`.`congestion` / 5) + 0.5),0) * 5) = `pls`.`congestion_pricing`.`non_priority`))) limit 1 */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-10-09  9:31:57
