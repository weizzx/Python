-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: endora-db-11.stable.cz:3306
-- Generation Time: Jun 13, 2025 at 12:36 AM
-- Server version: 10.3.35-MariaDB
-- PHP Version: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `weizzx`
--
CREATE DATABASE IF NOT EXISTS `weizzx` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `weizzx`;

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `id` int(11) NOT NULL,
  `question_text` varchar(255) DEFAULT NULL,
  `option_a` varchar(255) DEFAULT NULL,
  `option_b` varchar(255) DEFAULT NULL,
  `option_c` varchar(255) DEFAULT NULL,
  `option_d` varchar(255) DEFAULT NULL,
  `correct_option` char(1) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`id`, `question_text`, `option_a`, `option_b`, `option_c`, `option_d`, `correct_option`) VALUES
(1, 'Co znamená zkratka CPU?', 'Central Processing Unit', 'Computer Personal Unit', 'Central Programming Utility', 'Control Processing Unit', 'A'),
(2, 'Který jazyk je nejčastěji používán pro webové stránky?', 'Python', 'C++', 'HTML', 'Java', 'C'),
(3, 'Kolik bitů má 1 bajt?', '4', '8', '16', '32', 'B'),
(4, 'Jaký port používá HTTP protokol?', '80', '21', '443', '110', 'A'),
(5, 'Jaký je výstup příkazu 2 + 2 v Pythonu?', '22', '4', '2+2', 'Chyba', 'B'),
(6, 'Jaký hardware ukládá trvale data?', 'RAM', 'CPU', 'SSD', 'GPU', 'C'),
(7, 'Jaký je účel operačního systému?', 'Zobrazit web', 'Spustit BIOS', 'Spravovat hardware a software', 'Zabezpečit síť', 'C'),
(8, 'Co je IP adresa?', 'Typ počítače', 'Internetový poskytovatel', 'Jedinečný identifikátor v síti', 'Značka routeru', 'C'),
(9, 'Který jazyk se používá pro stylování webu?', 'HTML', 'JavaScript', 'CSS', 'SQL', 'C'),
(10, 'Co znamená zkratka URL?', 'Universal Resource Locator', 'Uniform Resource Locator', 'Unified Random Location', 'Universal Routing Layer', 'B'),
(11, 'K čemu slouží příkaz SELECT v SQL?', 'Vkládání dat', 'Smazání dat', 'Úprava dat', 'Výběr dat', 'D'),
(12, 'Jaký datový typ se v Pythonu používá pro celá čísla?', 'float', 'int', 'char', 'bool', 'B'),
(13, 'Jaký je správný způsob komentáře v Pythonu?', '// komentář', '# komentář', '/* komentář */', '<!-- komentář -->', 'B'),
(14, 'Který protokol se používá pro bezpečné webové připojení?', 'HTTP', 'FTP', 'HTTPS', 'SMTP', 'C'),
(15, 'Kolik znaků má binární číslo 1011?', '2', '3', '4', '5', 'C'),
(16, 'Jaký příkaz vypíše text v Pythonu?', 'echo', 'printf', 'write', 'print', 'D'),
(17, 'Jaký hardware se stará o zobrazení grafiky?', 'CPU', 'SSD', 'GPU', 'RAM', 'C'),
(18, 'Co je to cloud computing?', 'Fyzický server doma', 'Záloha na disku', 'Služba pro ukládání a práci s daty online', 'Typ počítače', 'C'),
(19, 'Jaká z možností je relační databáze?', 'MongoDB', 'Firebase', 'MySQL', 'Redis', 'C'),
(20, 'Který soubor má typicky příponu .exe?', 'Obrázek', 'Spustitelný program', 'Textový dokument', 'Tabulka', 'B');

-- --------------------------------------------------------

--
-- Table structure for table `scoreboard`
--

CREATE TABLE `scoreboard` (
  `id` int(11) NOT NULL,
  `username` varchar(16) DEFAULT NULL,
  `score` int(16) DEFAULT NULL,
  `isPassed` tinyint(1) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `scoreboard`
--

INSERT INTO `scoreboard` (`id`, `username`, `score`, `isPassed`) VALUES
(15, 'weizzx', 4, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `scoreboard`
--
ALTER TABLE `scoreboard`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `scoreboard`
--
ALTER TABLE `scoreboard`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
