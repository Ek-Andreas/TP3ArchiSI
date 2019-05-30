-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.3.15-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             9.5.0.5196
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for tp3
CREATE DATABASE IF NOT EXISTS `tp3` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin */;
USE `tp3`;

-- Dumping structure for table tp3.articles
CREATE TABLE IF NOT EXISTS `articles` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `author` varchar(50) NOT NULL,
  `section` varchar(50) NOT NULL,
  `title` varchar(250) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `summary` mediumtext DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table tp3.articles: ~2 rows (approximately)
/*!40000 ALTER TABLE `articles` DISABLE KEYS */;
INSERT INTO `articles` (`ID`, `author`, `section`, `title`, `date`, `status`, `summary`) VALUES
	(6, 'Anthony Zurcher', 'politics', 'Robert Mueller statement: What special counsel really meant', '2019-05-04', 'published', 'For the first time in his more than two years as special counsel, Mueller has spoken publicly about his investigation.\r\n\r\nIn addition to his announcement that his office is officially shutting down and he is returning to private life, Mr Mueller essentially gave a bullet-point guide to the results of his investigation.\r\n\r\nHere are some key takeaways from his eight minutes in front of the nation.'),
	(7, 'David Allan', 'cinema', 'First look: Living, breathing, eating Star Wars in Disney\'s new theme park land', '2018-05-04', 'in edition', 'That line, from "Star Wars: The Force Awakens" is what walking into Disneyland\'s new Star Wars land, opening Friday, embodies.');
/*!40000 ALTER TABLE `articles` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
