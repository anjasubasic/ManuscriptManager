-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
-- ------------------------------------------------------
-- Server version	5.7.20-log

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
-- Table structure for table `acceptedmanuscript`
--

CREATE DATABASE mydb;
USE mydb;

DROP TABLE IF EXISTS `acceptedmanuscript`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `acceptedmanuscript` (
  `pageCount` int(11) NOT NULL,
  `orderNumberInIssue` int(11) NOT NULL,
  `startPageInIssue` int(11) NOT NULL,
  `dateAcceptedToIssue` datetime NOT NULL,
  `Manuscript_idManuscript` int(11) NOT NULL,
  `Issue_idIssue` int(11) NOT NULL,
  PRIMARY KEY (`Manuscript_idManuscript`),
  KEY `fk_AcceptedManuscript_Manuscript1_idx` (`Manuscript_idManuscript`),
  KEY `fk_AcceptedManuscript_Issue1_idx` (`Issue_idIssue`),
  CONSTRAINT `fk_AcceptedManuscript_Issue1` FOREIGN KEY (`Issue_idIssue`) REFERENCES `issue` (`idIssue`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_AcceptedManuscript_Manuscript1` FOREIGN KEY (`Manuscript_idManuscript`) REFERENCES `manuscript` (`idManuscript`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acceptedmanuscript`
--

LOCK TABLES `acceptedmanuscript` WRITE;
/*!40000 ALTER TABLE `acceptedmanuscript` DISABLE KEYS */;
INSERT INTO `acceptedmanuscript` VALUES (15,3,47,'2003-01-01 00:00:00',5,1),(10,2,94,'2004-01-01 00:00:00',6,1),(10000,0,0,'2017-10-27 00:00:00',50,0);
/*!40000 ALTER TABLE `acceptedmanuscript` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `anyauthormanuscripts`
--

DROP TABLE IF EXISTS `anyauthormanuscripts`;
/*!50001 DROP VIEW IF EXISTS `anyauthormanuscripts`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `anyauthormanuscripts` AS SELECT 
 1 AS `lastName`,
 1 AS `idAuthor`,
 1 AS `idManuscript`,
 1 AS `status`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `author`
--

DROP TABLE IF EXISTS `author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `author` (
  `idAuthor` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) NOT NULL,
  `emailAddress` varchar(45) NOT NULL,
  `mailingAddress` varchar(45) NOT NULL,
  `currentAffiliation` varchar(45) NOT NULL,
  `middleInitial` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) NOT NULL,
  PRIMARY KEY (`idAuthor`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `author`
--

LOCK TABLES `author` WRITE;
/*!40000 ALTER TABLE `author` DISABLE KEYS */;
INSERT INTO `author` VALUES (1,'Anja','anja.subasic@blah.com','1 Wheelock Street, Hanover NH 03755','Dartmouth College','','Subasic'),(2,'Casey','casey.baer@blah.com','1 Wheelock Street, Hanover NH 03755','Dartmouth College','F','Baer'),(3,'Sergey','sergey.bratus@blah.com','1 Wheelock Street, Hanover NH 03755','Dartmouth College','C','Bratus'),(4,'VS','vs.subrahmanian@blah.com','1 Wheelock Street, Hanover NH 03755','University of Maryland','S','Subrahmanian'),(5,'Chiara','chiara.pulice@blah.com','1 Wheelock Street, Hanover NH 03755','University of Maryland','','Pulice'),(6,'Marissa','marissa@email.com','1 Wheelock Street, Hanovere NH 03755','Dartmouth','C','Le Coz'),(9,'Jenny','jenny@email.com','1 Wheelock Street, Hanover NH 03755','Dartmouth College','','Mathews'),(10,'Jane','jane@email.com','1 Wheelock Street, Hanover NH 03755','Dartmouth College','','Maine'),(11,'F','E','A','A','M','L'),(12,'Anja','anja@gmail.scom','sdfkjsdlfk dffdf','dartmouth','','Subasic');
/*!40000 ALTER TABLE `author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editor`
--

DROP TABLE IF EXISTS `editor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `editor` (
  `idEditor` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) NOT NULL,
  `middleInitial` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) NOT NULL,
  PRIMARY KEY (`idEditor`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editor`
--

LOCK TABLES `editor` WRITE;
/*!40000 ALTER TABLE `editor` DISABLE KEYS */;
INSERT INTO `editor` VALUES (1,'Marissa','C','Le Coz'),(2,'Anja','','Subasic'),(3,'Charles','C','Palmer'),(4,'Steve','','Jobs'),(6,'Stan','','Mathews'),(7,'Stanley','','Jones'),(8,'Jenny','','Jones'),(9,'Test1','','Test2'),(16,'Steve','',' Jobs'),(17,'Steve','',' Jobs'),(18,'Anja','',' Subasic');
/*!40000 ALTER TABLE `editor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback` (
  `Manuscript_idManuscript` int(11) NOT NULL,
  `Reviewer_idReviewer` int(11) NOT NULL,
  `dateSentToReviewer` datetime NOT NULL,
  `appropriateRating` int(11) NOT NULL,
  `clarityRating` int(11) NOT NULL,
  `methodologyRating` int(11) NOT NULL,
  `contributionRating` int(11) NOT NULL,
  `dateFeedbackReceived` datetime DEFAULT NULL,
  `recommendation` varchar(45) NOT NULL,
  PRIMARY KEY (`Manuscript_idManuscript`,`Reviewer_idReviewer`),
  KEY `fk_Feedback_Manuscript1_idx` (`Manuscript_idManuscript`),
  KEY `fk_Feedback_Reviewer1_idx` (`Reviewer_idReviewer`),
  CONSTRAINT `fk_Feedback_Manuscript1` FOREIGN KEY (`Manuscript_idManuscript`) REFERENCES `manuscript` (`idManuscript`) ON DELETE CASCADE,
  CONSTRAINT `fk_Feedback_Reviewer1` FOREIGN KEY (`Reviewer_idReviewer`) REFERENCES `reviewer` (`idReviewer`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (5,10,'2017-10-26 00:00:00',10,10,10,10,NULL,'accept'),(6,8,'2017-10-26 00:00:00',10,10,10,10,NULL,'accept'),(6,10,'2017-10-26 00:00:00',1,2,3,4,'2017-10-26 00:00:00','accept');
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `interest`
--

DROP TABLE IF EXISTS `interest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `interest` (
  `Reviewer_idReviewer` int(11) NOT NULL,
  `RICode_idRICode` int(11) NOT NULL,
  PRIMARY KEY (`Reviewer_idReviewer`,`RICode_idRICode`),
  KEY `fk_Interest_Reviewer1_idx` (`Reviewer_idReviewer`),
  KEY `fk_Interest_RICode1_idx` (`RICode_idRICode`),
  CONSTRAINT `fk_Interest_RICode1` FOREIGN KEY (`RICode_idRICode`) REFERENCES `ricode` (`idRICode`),
  CONSTRAINT `fk_Interest_Reviewer1` FOREIGN KEY (`Reviewer_idReviewer`) REFERENCES `reviewer` (`idReviewer`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interest`
--

LOCK TABLES `interest` WRITE;
/*!40000 ALTER TABLE `interest` DISABLE KEYS */;
INSERT INTO `interest` VALUES (3,103),(8,103),(10,106),(143,101),(143,105),(143,109),(144,105),(145,105),(146,101),(146,105),(146,109),(147,101),(147,105),(147,109),(148,107),(149,105),(149,107);
/*!40000 ALTER TABLE `interest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issue`
--

DROP TABLE IF EXISTS `issue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `issue` (
  `idIssue` int(11) NOT NULL,
  `publicationYear` datetime NOT NULL,
  `periodNumber` int(11) NOT NULL,
  `printDate` datetime NOT NULL,
  PRIMARY KEY (`idIssue`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issue`
--

LOCK TABLES `issue` WRITE;
/*!40000 ALTER TABLE `issue` DISABLE KEYS */;
INSERT INTO `issue` VALUES (0,'1900-01-01 00:00:00',0,'1900-01-01 00:00:00'),(1,'2014-01-01 00:00:00',1,'2014-01-01 00:00:00'),(2,'2014-01-01 00:00:00',2,'2014-03-01 00:00:00'),(3,'2014-01-01 00:00:00',3,'2014-06-01 00:00:00'),(4,'2014-01-01 00:00:00',4,'2014-09-01 00:00:00'),(5,'2015-01-01 00:00:00',1,'2017-10-27 00:00:00'),(6,'2015-01-01 00:00:00',2,'2015-03-01 00:00:00'),(7,'2015-01-01 00:00:00',3,'2015-06-01 00:00:00'),(8,'2015-01-01 00:00:00',4,'2015-09-01 00:00:00'),(9,'2016-01-01 00:00:00',1,'2016-01-01 00:00:00'),(10,'2016-01-01 00:00:00',2,'2016-03-01 00:00:00'),(11,'2016-01-01 00:00:00',3,'2016-06-01 00:00:00'),(12,'2016-01-01 00:00:00',4,'2016-09-01 00:00:00'),(13,'2017-01-01 00:00:00',1,'2017-01-01 00:00:00'),(14,'2017-01-01 00:00:00',2,'2017-03-01 00:00:00'),(15,'2017-01-01 00:00:00',3,'2017-06-01 00:00:00'),(16,'2017-01-01 00:00:00',4,'2017-09-01 00:00:00');
/*!40000 ALTER TABLE `issue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `leadauthormanuscripts`
--

DROP TABLE IF EXISTS `leadauthormanuscripts`;
/*!50001 DROP VIEW IF EXISTS `leadauthormanuscripts`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `leadauthormanuscripts` AS SELECT 
 1 AS `lastName`,
 1 AS `idAuthor`,
 1 AS `idManuscript`,
 1 AS `status`,
 1 AS `statusModifiedDateTime`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `manuscript`
--

DROP TABLE IF EXISTS `manuscript`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manuscript` (
  `idManuscript` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `dateReceived` datetime NOT NULL,
  `status` varchar(45) NOT NULL,
  `Editor_idEditor` int(11) NOT NULL,
  `statusModifiedDateTime` datetime NOT NULL,
  `RICode_idRICode` int(11) NOT NULL,
  `document` blob,
  PRIMARY KEY (`idManuscript`),
  KEY `fk_Manuscript_Editor1_idx` (`Editor_idEditor`),
  KEY `fk_Manuscript_RICode1` (`RICode_idRICode`),
  CONSTRAINT `fk_Manuscript_Editor1` FOREIGN KEY (`Editor_idEditor`) REFERENCES `editor` (`idEditor`),
  CONSTRAINT `fk_Manuscript_RICode1` FOREIGN KEY (`RICode_idRICode`) REFERENCES `ricode` (`idRICode`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manuscript`
--

LOCK TABLES `manuscript` WRITE;
/*!40000 ALTER TABLE `manuscript` DISABLE KEYS */;
INSERT INTO `manuscript` VALUES (5,'New Manuscript','2002-02-02 00:00:00','published',6,'2017-10-26 00:00:00',101,NULL),(6,'title','2017-10-26 00:00:00','reviewing',7,'2017-10-27 00:00:00',101,NULL),(12,'title','2017-10-26 00:00:00','in typesetting',7,'2017-10-27 00:00:00',101,NULL),(15,'title','2017-10-26 00:00:00','accepted',7,'2017-10-26 00:00:00',101,NULL),(50,'Trigger Test Manuscript','2003-03-03 00:00:00','in typesetting',7,'2017-10-27 00:00:00',103,NULL),(58,'paperTitle','2017-10-26 00:00:00','in typesetting',7,'2017-10-26 00:00:00',105,NULL),(59,'title ','2017-10-27 00:00:00','submitted',7,'2017-10-27 00:00:00',105,NULL);
/*!40000 ALTER TABLE `manuscript` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_VALUE_ON_ZERO' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER no_reviewer_available
BEFORE INSERT ON manuscript
FOR EACH ROW 

BEGIN

	# n = number of reviewers with this RICode
	DECLARE n INT DEFAULT 0;
    DECLARE signal_message VARCHAR(128);
	SELECT COUNT(*) FROM interest WHERE RICode_idRICode = new.RICode_idRICode INTO n; # wasn't sure how to work DISTINCT into this syntax
	#SELECT COUNT(*) INTO n FROM (SELECT idRICode FROM interest WHERE idRICode = new.RICode) as T;

    
    IF (n = 0) THEN
        SET signal_message = CONCAT('UserException: No manuscript reviewers are qualified to review papers with the RICode you have specified: ', CAST(new.RICode_idRICode AS CHAR));
        SIGNAL SQLSTATE '45000' SET message_text = signal_message;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER updateStatusModifiedDateTime 
BEFORE UPDATE ON manuscript 
FOR EACH ROW
     BEGIN
         IF NEW.status != OLD.status THEN
             SET NEW.statusModifiedDateTime = curdate();
         END IF;
     END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 trigger add_to_acceptedmanuscript after update on manuscript
for each row
begin
  IF (NEW.status = 'accepted') THEN
	IF((SELECT COUNT(Manuscript_idManuscript) FROM acceptedmanuscript WHERE Manuscript_idManuscript = NEW.idManuscript) = 0) THEN
        insert into acceptedmanuscript values (0, 0, 0, curdate(), new.idManuscript, 0);
	END IF;
  END IF;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary view structure for view `publishedissues`
--

DROP TABLE IF EXISTS `publishedissues`;
/*!50001 DROP VIEW IF EXISTS `publishedissues`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `publishedissues` AS SELECT 
 1 AS `publicationYear`,
 1 AS `periodNumber`,
 1 AS `title`,
 1 AS `startPageInIssue`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `reviewer`
--

DROP TABLE IF EXISTS `reviewer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reviewer` (
  `idReviewer` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) NOT NULL,
  `emailAddress` varchar(45) NOT NULL,
  `currentAffiliation` varchar(45) NOT NULL,
  `middleInitial` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) NOT NULL,
  PRIMARY KEY (`idReviewer`)
) ENGINE=InnoDB AUTO_INCREMENT=150 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviewer`
--

LOCK TABLES `reviewer` WRITE;
/*!40000 ALTER TABLE `reviewer` DISABLE KEYS */;
INSERT INTO `reviewer` VALUES (3,'Chiara','chiara@email.com','Dartmouth College','K','Pulice'),(8,'Sean','sean@email.com','Dartmouth College','K','Smith'),(10,'Anja','asubasic@cs.dartmouth.edu','Dartmouth',NULL,'Subasic'),(100,'sdf','sdf','sdf','sdf','sdf'),(101,'Charles','jane@email.com','Dartmouth College','','Palmer'),(124,'TestFirst','TestEmail','TestAff','TestMiddle','TestLast'),(143,'df','dfd','df','df','df'),(144,'df','df','df','df','df'),(145,'fd','df','df','df','df'),(146,'df','df','df','df','df'),(147,'Anja','anja@gmail.com','Dartmouth','f','Subasic'),(148,'F','E','A','M','L'),(149,'F','E','A','I','L');
/*!40000 ALTER TABLE `reviewer` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_VALUE_ON_ZERO' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER reviewer_withdrew
BEFORE DELETE ON reviewer
FOR EACH ROW 

BEGIN

    DECLARE n INT DEFAULT 0; # number of feedback entries for this reviewer
    DECLARE i INT DEFAULT 0; # index
    DECLARE currentManuscriptId INT DEFAULT 0;
    DECLARE currentRICode INT DEFAULT 0;
        DECLARE signal_message VARCHAR(128);

    # n = number of feedback entries for this reviewer
    SELECT COUNT(*) FROM feedback WHERE Reviewer_idReviewer = old.idReviewer INTO n;

    WHILE i < n DO
           
        # each iteration of the loop will deal with a different manuscript that the reviewer was reviewing
        SET currentManuscriptId = (SELECT Manuscript_idManuscript FROM feedback WHERE Reviewer_idReviewer = old.idReviewer LIMIT 1 OFFSET i);

        # if the manuscript is currently under review AND this manuscript has no other reviewers
        IF (((SELECT status from manuscript WHERE idManuscript = currentManuscriptId) = "under review") AND ((SELECT COUNT(*) FROM feedback WHERE Manuscript_idManuscript = currentManuscriptId) = 1)) THEN
       
            # get RICode for this current manuscript
            SET currentRICode = (SELECT RICode_idRICode FROM manuscript WHERE idManuscript = currentManuscriptId);
           
            # if there's another reviewer in the system with that RICode who isn't this reviewee...
            IF ((SELECT COUNT(*) FROM interest WHERE RICode_idRICode = currentRICode AND Reviewer_idReviewer != old.idReviewer) > 0) THEN
                # set manuscript's status to submitted
                UPDATE manuscript SET status = "submitted" WHERE idManuscript = currentManuscriptId;
            
            # else, that reviewer was the only one with that RICode
            ELSE
                # update status to rejected
                UPDATE manuscript SET status = "rejected" WHERE idManuscript = currentManuscriptId;
            END IF;
           
        END IF;
        SET i = i + 1;
    END WHILE;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary view structure for view `reviewqueue`
--

DROP TABLE IF EXISTS `reviewqueue`;
/*!50001 DROP VIEW IF EXISTS `reviewqueue`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `reviewqueue` AS SELECT 
 1 AS `PrimaryAuthor`,
 1 AS `idAuthor`,
 1 AS `idManuscript`,
 1 AS `Reviewers`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `reviewstatus`
--

DROP TABLE IF EXISTS `reviewstatus`;
/*!50001 DROP VIEW IF EXISTS `reviewstatus`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `reviewstatus` AS SELECT 
 1 AS `idManuscript`,
 1 AS `dateSentToReviewer`,
 1 AS `title`,
 1 AS `appropriateRating`,
 1 AS `clarityRating`,
 1 AS `methodologyRating`,
 1 AS `contributionRating`,
 1 AS `recommendation`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `ricode`
--

DROP TABLE IF EXISTS `ricode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ricode` (
  `idRICode` int(11) NOT NULL AUTO_INCREMENT,
  `RIValue` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idRICode`)
) ENGINE=InnoDB AUTO_INCREMENT=225 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ricode`
--

LOCK TABLES `ricode` WRITE;
/*!40000 ALTER TABLE `ricode` DISABLE KEYS */;
INSERT INTO `ricode` VALUES (101,'Agricultural engineering'),(102,'Biochemical engineering'),(103,'Biomechanical engineering'),(104,'Ergonomics'),(105,'Food engineering'),(106,'Bioprocess engineering'),(107,'Genetic engineering'),(108,'Human genetic engineering'),(109,'Metabolic engineering'),(110,'Molecular engineering'),(111,'Neural engineering'),(112,'Protein engineering'),(113,'Rehabilitation engineering'),(114,'Tissue engineering'),(115,'Aquatic and environmental engineering'),(116,'Architectural engineering'),(117,'Civionic engineering'),(118,'Construction engineering'),(119,'Earthquake engineering'),(120,'Earth systems engineering and management'),(121,'Ecological engineering'),(122,'Environmental engineering'),(123,'Geomatics engineering'),(124,'Geotechnical engineering'),(125,'Highway engineering'),(126,'Hydraulic engineering'),(127,'Landscape engineering'),(128,'Land development engineering'),(129,'Pavement engineering'),(130,'Railway systems engineering'),(131,'River engineering'),(132,'Sanitary engineering'),(133,'Sewage engineering'),(134,'Structural engineering'),(135,'Surveying'),(136,'Traffic engineering'),(137,'Transportation engineering'),(138,'Urban engineering'),(139,'Irrigation and agriculture engineering'),(140,'Explosives engineering'),(141,'Biomolecular engineering'),(142,'Ceramics engineering'),(143,'Broadcast engineering'),(144,'Building engineering'),(145,'Signal Processing'),(146,'Computer engineering'),(147,'Power systems engineering'),(148,'Control engineering'),(149,'Telecommunications engineering'),(150,'Electronic engineering'),(151,'Instrumentation engineering'),(152,'Network engineering'),(153,'Neuromorphic engineering'),(154,'Engineering Technology'),(155,'Integrated engineering'),(156,'Value engineering'),(157,'Cost engineering'),(158,'Fire protection engineering'),(159,'Domain engineering'),(160,'Engineering economics'),(161,'Engineering management'),(162,'Engineering psychology'),(163,'Ergonomics'),(164,'Facilities Engineering'),(165,'Logistic engineering'),(166,'Model-driven engineering'),(167,'Performance engineering'),(168,'Process engineering'),(169,'Product Family Engineering'),(170,'Quality engineering'),(171,'Reliability engineering'),(172,'Safety engineering'),(173,'Security engineering'),(174,'Support engineering'),(175,'Systems engineering'),(176,'Metallurgical Engineering'),(177,'Surface Engineering'),(178,'Biomaterials Engineering'),(179,'Crystal Engineering'),(180,'Amorphous Metals'),(181,'Metal Forming'),(182,'Ceramic Engineering'),(183,'Plastics Engineering'),(184,'Forensic Materials Engineering'),(185,'Composite Materials'),(186,'Casting'),(187,'Electronic Materials'),(188,'Nano materials'),(189,'Corrosion Engineering'),(190,'Vitreous Materials'),(191,'Welding'),(192,'Acoustical engineering'),(193,'Aerospace engineering'),(194,'Audio engineering'),(195,'Automotive engineering'),(196,'Building services engineering'),(197,'Earthquake engineering'),(198,'Forensic engineering'),(199,'Marine engineering'),(200,'Mechatronics'),(201,'Nanoengineering'),(202,'Naval architecture'),(203,'Sports engineering'),(204,'Structural engineering'),(205,'Vacuum engineering'),(206,'Military engineering'),(207,'Combat engineering'),(208,'Offshore engineering'),(209,'Optical engineering'),(210,'Geophysical engineering'),(211,'Mineral engineering'),(212,'Mining engineering'),(213,'Reservoir engineering'),(214,'Climate engineering'),(215,'Computer-aided engineering'),(216,'Cryptographic engineering'),(217,'Information engineering'),(218,'Knowledge engineering'),(219,'Language engineering'),(220,'Release engineering'),(221,'Teletraffic engineering'),(222,'Usability engineering'),(223,'Web engineering'),(224,'Systems engineering');
/*!40000 ALTER TABLE `ricode` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `submit`
--

DROP TABLE IF EXISTS `submit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `submit` (
  `Author_idAuthor` int(11) NOT NULL,
  `Manuscript_idManuscript` int(11) NOT NULL,
  `authorOrderNumber` int(11) NOT NULL,
  `affiliationAtTimeOfManuscript` varchar(45) NOT NULL,
  PRIMARY KEY (`Author_idAuthor`,`Manuscript_idManuscript`),
  KEY `fk_Submit_Author_idx` (`Author_idAuthor`),
  KEY `fk_Submit_Manuscript1_idx` (`Manuscript_idManuscript`),
  CONSTRAINT `fk_Submit_Author` FOREIGN KEY (`Author_idAuthor`) REFERENCES `author` (`idAuthor`),
  CONSTRAINT `fk_Submit_Manuscript1` FOREIGN KEY (`Manuscript_idManuscript`) REFERENCES `manuscript` (`idManuscript`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `submit`
--

LOCK TABLES `submit` WRITE;
/*!40000 ALTER TABLE `submit` DISABLE KEYS */;
INSERT INTO `submit` VALUES (1,6,1,'Dartmouth College'),(1,58,1,'Dartmouth'),(1,59,1,'dartmouth '),(2,6,2,''),(3,6,3,''),(9,50,1,'Dartmouth College');
/*!40000 ALTER TABLE `submit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `whatsleft`
--

DROP TABLE IF EXISTS `whatsleft`;
/*!50001 DROP VIEW IF EXISTS `whatsleft`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `whatsleft` AS SELECT 
 1 AS `idManuscript`,
 1 AS `status`,
 1 AS `statusModifiedDateTime`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping routines for database 'mydb'
--
/*!50003 DROP FUNCTION IF EXISTS `getReviewerId` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_VALUE_ON_ZERO' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `getReviewerId`() RETURNS int(11)
    NO SQL
    DETERMINISTIC
RETURN @reviewerid ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `anyauthormanuscripts`
--

/*!50001 DROP VIEW IF EXISTS `anyauthormanuscripts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `anyauthormanuscripts` AS select `a`.`lastName` AS `lastName`,`a`.`idAuthor` AS `idAuthor`,`m`.`idManuscript` AS `idManuscript`,`m`.`status` AS `status` from ((`author` `a` join `submit` `s` on((`s`.`Author_idAuthor` = `a`.`idAuthor`))) join `manuscript` `m` on((`m`.`idManuscript` = `s`.`Manuscript_idManuscript`))) order by `a`.`lastName`,`m`.`statusModifiedDateTime` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `leadauthormanuscripts`
--

/*!50001 DROP VIEW IF EXISTS `leadauthormanuscripts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `leadauthormanuscripts` AS select `a`.`lastName` AS `lastName`,`a`.`idAuthor` AS `idAuthor`,`m`.`idManuscript` AS `idManuscript`,`m`.`status` AS `status`,`m`.`statusModifiedDateTime` AS `statusModifiedDateTime` from ((`author` `a` join `submit` `s` on((`s`.`Author_idAuthor` = `a`.`idAuthor`))) join `manuscript` `m` on((`m`.`idManuscript` = `s`.`Manuscript_idManuscript`))) where (`s`.`authorOrderNumber` = 1) order by `a`.`lastName`,`a`.`idAuthor`,`m`.`statusModifiedDateTime` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `publishedissues`
--

/*!50001 DROP VIEW IF EXISTS `publishedissues`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `publishedissues` AS select year(`i`.`publicationYear`) AS `publicationYear`,`i`.`periodNumber` AS `periodNumber`,`m`.`title` AS `title`,`am`.`startPageInIssue` AS `startPageInIssue` from ((`issue` `i` join `acceptedmanuscript` `am` on((`am`.`Issue_idIssue` = `i`.`idIssue`))) join `manuscript` `m` on((`m`.`idManuscript` = `am`.`Manuscript_idManuscript`))) where ((`i`.`printDate` <= curdate()) and (`m`.`status` = 'Published')) order by year(`i`.`publicationYear`),`i`.`periodNumber`,`am`.`startPageInIssue` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `reviewqueue`
--

/*!50001 DROP VIEW IF EXISTS `reviewqueue`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `reviewqueue` AS select concat(`a`.`firstName`,' ',`a`.`lastName`) AS `PrimaryAuthor`,`a`.`idAuthor` AS `idAuthor`,`m`.`idManuscript` AS `idManuscript`,concat(`r`.`firstName`,' ',`r`.`lastName`) AS `Reviewers` from ((((`manuscript` `m` join `submit` `s` on((`s`.`Manuscript_idManuscript` = `m`.`idManuscript`))) join `author` `a` on((`a`.`idAuthor` = `s`.`Author_idAuthor`))) join `feedback` `f` on((`f`.`Manuscript_idManuscript` = `m`.`idManuscript`))) join `reviewer` `r` on((`r`.`idReviewer` = `f`.`Reviewer_idReviewer`))) where ((`m`.`status` = 'under review') and (`s`.`authorOrderNumber` = 1)) order by `m`.`statusModifiedDateTime` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `reviewstatus`
--

/*!50001 DROP VIEW IF EXISTS `reviewstatus`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `reviewstatus` AS select `m`.`idManuscript` AS `idManuscript`,`f`.`dateSentToReviewer` AS `dateSentToReviewer`,`m`.`title` AS `title`,`f`.`appropriateRating` AS `appropriateRating`,`f`.`clarityRating` AS `clarityRating`,`f`.`methodologyRating` AS `methodologyRating`,`f`.`contributionRating` AS `contributionRating`,`f`.`recommendation` AS `recommendation` from (`feedback` `f` join `manuscript` `m` on((`m`.`idManuscript` = `f`.`Manuscript_idManuscript`))) where (`f`.`Reviewer_idReviewer` = `getReviewerId`()) order by `f`.`dateFeedbackReceived` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `whatsleft`
--

/*!50001 DROP VIEW IF EXISTS `whatsleft`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `whatsleft` AS select `m`.`idManuscript` AS `idManuscript`,`m`.`status` AS `status`,`m`.`statusModifiedDateTime` AS `statusModifiedDateTime` from `manuscript` `m` */;
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

-- Dump completed on 2017-10-27 18:23:44
