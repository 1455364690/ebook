-- MySQL dump 10.13  Distrib 5.1.73, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: ebook
-- ------------------------------------------------------
-- Server version	5.1.73-log

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
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `src` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `img` varchar(70) COLLATE utf8_unicode_ci DEFAULT NULL,
  `brief` text COLLATE utf8_unicode_ci,
  `date` int(40) DEFAULT NULL,
  `uploader` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `bigpic` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'唱游--30期','static/www/20150418203104/vol30/online.htm','static/src/cover/72f1567bb5a2e4470ba9.jpg','远比远方的远，不过是氤氲在江南小镇的匆匆一瞥。——《远比远方的远》 不知',1429360265,'1','static/src/bigpic/2910439fc82aa3643b43.jpg'),(2,'唱游--32期','static/www/20150418203419/vol32/online.htm','static/src/cover/95b9f6d468501e6e7015.jpg','人世间不可长久的美，往往依托见证者一个瞬间的美好记忆。——《突然的美感》',1429360460,'1','static/src/bigpic/77d51c8875fbb64445d5.jpg'),(3,'唱游-34期 2014迎新特刊','static/www/20150418203620/vol34/online.htm','static/src/cover/b9b23fa867a7de7c146a.jpg','岁月流转，四季有时，无论昨天现在亦是未来，且歌且行，当惜韶华。——《昨天的你的现在的未来》 饶卓群',1429360580,'1','static/src/bigpic/34aedeb744ec4d1310bf.jpg'),(4,'唱游--35期','static/www/20150418203913/vol35/online.htm','static/src/cover/1a35f2eab063ff38432f.jpg','漫长的历史将伊卡鲁斯塑造成了一个遥不可及的神话悲歌，但他毕生难以企及的愿望，却终于在千百年后得以成全。伴随着文明的前进，我们从广袤的森林平原飞向了寥廓的天空，飞向了邈远无边的银河。——《天空的心》 张楷时',1429360753,'1','static/src/bigpic/27c8fbcf48dd5c3d2d5b.jpg'),(5,'唱游--36期','static/www/20150418204055/vol36/online.htm','static/src/cover/f5bd87f4f24070fb177b.jpg','也有那么一群疯子，他们在文字中发出人性中的另一种深刻的、被压抑太久的东西。边缘身份，边缘情感，边缘意识，这些涌动着的暗流，与主流相比较是那样的特别和与众不同，这种暂时性的边缘，便是永恒。——《诉者缘深》 丁里',1429360855,'1','static/src/bigpic/7daf640f1ad79236a10d.jpg'),(6,'唱游--37期','static/www/20150418204333/vol37/online.htm','static/src/cover/d7ac30ddd752fc35462f.jpg','地平线未曾靠近，有璀璨的金色从深处浮现，有金龙在慢慢苏醒。它们看见了，夜的褪去，日的降临。它们开始疯狂地后退，每条经脉重新回到它们的生根处，心愿在红线里沉默地落在枝桠上，梧桐的枝干还是一样枯瘦。它们退回的道路上卷起风沙，道路隐成指向明确的线，从他指向将起的霞光。——《夜的线》 饶卓群',1429361013,'1','static/src/bigpic/04692ef527b88b5abbf3.jpg'),(7,'唱游-38期  2015樱花特刊','static/www/20150418204526/vol38/online.htm','static/src/cover/aaebcc09a5ae5642d532.jpg','拾味中国，无论是食中之味，乐中之韵，还是书中之义，对我们而言，都是一场味觉的盛宴，需要用心去细细咀嚼。品味人生，我们用舌尖去触碰世界的美。',1429361126,'1','static/src/bigpic/291fa496feaff2121857.jpg'),(8,'唱游-39期','static/www/20150419015248/vol39/online.htm','static/src/cover/a00ca88e573603d0a18f.jpg','我宁愿至少把地球走遍，我宁愿只学自己喜欢的，不求甚解。可是的确不想醒来的时候也必须醒来，深深感觉到艰难的时候，也必须去面对而不能去逃避，不愿意，但是必须去做。——《一条缝隙》 袁杏然',1429379568,'ebooker','static/src/bigpic/118a131584f724db4414.jpg'),(11,'唱游-2015-五四特刊','static/www/20150504154416/extra5.4/online.htm','static/src/cover/9a8ec7e1950eda5e4ec8.jpg','学生，青年的含义我想是从历史的那一天得到真正的衡量。青年，冲动浪漫与沉着冷静兼顾，冰与火交融而生的乐章。不会忘记冲动，那是破冰的利器；无法丢弃理智，那是理想的锁匙。——《冰与火》袁杏然',1430725457,'ebooker','static/src/bigpic/68133680aef130fb7ce4.jpg');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(32) DEFAULT NULL,
  `lastpost` int(40) DEFAULT NULL,
  `state` int(11) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `realname` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'1','6da31d319d40440f6fd820adac3fc115',1444233598,4,'1299298676@qq.com','杨波'),(2,'lee3164','380ed0ef26f80b5f0b43aa509ce9dc82',1428841599,2,'',''),(3,'yingying','202cb962ac59075b964b07152d234b70',1419337430,3,'',''),(4,'ebooker','4684cddc2fdd1f00234aca819c872304',1433341342,3,'',''),(12,'孤城','facff280c0500e883fe552bc89797590',1431923146,1,'1579670185@qq.com','刘泽彬'),(21,'秉烛游','24ab83939e7460be2334ba165f2e7a07',1431923146,3,'1031211520@qq.com','岳瑾雯'),(22,'lianglee30','7202ae8c7c598c7d8984324bc6c907ac',NULL,1,'124366992@qq.com','124366992@qq.com'),(23,'xiaoyongsun','4e96a96b5f8da9ed0007aa2cc4891dcd',NULL,1,'309392685@qq.com','孙小勇'),(24,'leonhardt002','a7e6d9523a9e730e8bac1f87fb4a59fe',NULL,1,'1030522025@qq.com','李耀铮'),(25,'mavis','3e4716d9c9d033d52c299cfab13f840c',NULL,1,'390106329@qq.com','梅妍'),(26,'lsq','b08f2a26eabdfd11ffb0035373d9fed7',NULL,1,'2065079425@qq.com ','lei '),(27,'2014302010006','5cab6c2653707ea2b0730dc3f7c235a6',NULL,1,'1039074010@qq.com','覃维'),(28,'毛科稀','fab5c86dd8796ba8e47191a3cd387e02',NULL,1,'1215757073@qq.com','毛科稀'),(29,'我爱呼吸','5012b076a1d8919372b7f81e944ba3c4',NULL,1,'454173222@qq.com','贺夏雨'),(30,'凤宇','7d9d1244a255470ecdebd5edb2a566b2',NULL,1,'993878831@qq.com','张凤宇');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-10-11  9:24:19
