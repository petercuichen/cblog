--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
CREATE TABLE `post` (
  `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `author_id` int(11) NOT NULL,
  `title` varchar(128),
  `category_id` int(11),
  `pv` int(11) DEFAULT 0,
  `status` tinyint(4) NOT NULL,
  `area` text DEFAULT '',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  INDEX `category_id` (`category_id`),
  INDEX `author_id` (`author_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;


--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `is_admin` tinyint(4) DEFAULT 0,
  `email` varchar(128),
  `last_login` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;


--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(128) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;


--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag` (
  `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `post_id` int(11) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
