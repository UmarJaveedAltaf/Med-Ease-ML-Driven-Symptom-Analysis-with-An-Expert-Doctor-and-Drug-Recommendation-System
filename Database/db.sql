/*
SQLyog Community Edition- MySQL GUI v6.07
Host - 5.5.30 : Database - disease_prediction
*********************************************************************
Server version : 5.5.30
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

create database if not exists `disease_prediction`;

USE `disease_prediction`;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

/*Table structure for table `bkappointments` */

DROP TABLE IF EXISTS `bkappointments`;

CREATE TABLE `bkappointments` (
  `sno` int(10) NOT NULL AUTO_INCREMENT,
  `patient_uid` varchar(500) DEFAULT NULL,
  `patient_name` varchar(500) DEFAULT NULL,
  `patient_age` varchar(500) DEFAULT NULL,
  `patient_gender` varchar(500) DEFAULT NULL,
  `symptoms` varchar(1000) DEFAULT NULL,
  `disease` varchar(500) DEFAULT NULL,
  `doctor_uid` varchar(500) DEFAULT NULL,
  `apdate` varchar(500) DEFAULT NULL,
  `aptime` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Table structure for table `doctor` */

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `name` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `specialties` varchar(100) DEFAULT NULL,
  `medication` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `workarea` varchar(100) DEFAULT NULL,
  `userid` varchar(100) DEFAULT NULL,
  `passwrd` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `picture` longblob,
  `rating` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `patient` */

DROP TABLE IF EXISTS `patient`;

CREATE TABLE `patient` (
  `name` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `userid` varchar(100) DEFAULT NULL,
  `passwrd` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `picture` longblob
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `ratings` */

DROP TABLE IF EXISTS `ratings`;

CREATE TABLE `ratings` (
  `doct_id` varchar(100) DEFAULT NULL,
  `one` int(10) DEFAULT NULL,
  `two` int(10) DEFAULT NULL,
  `three` int(10) DEFAULT NULL,
  `four` int(10) DEFAULT NULL,
  `five` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
