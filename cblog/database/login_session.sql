--
-- Table structure for table `login_session`
--

DROP TABLE IF EXISTS `login_session`;
CREATE TABLE `login_session` (
  `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `use_id` int(11) NOT NULL,
  `sso_id` varchar(64) NOT NULL,
  `is_valid` tinyint(4) DEFAULT 1,
  `last_active` timestamp,
  `created_ip` varchar(16) default '',
  `last_login` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
