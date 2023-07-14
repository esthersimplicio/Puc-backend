-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 05, 2021 at 02:58 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.4.25

-- Or Mysql

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- CREATE THE DATABASE: `mvp`
--

-- --------------------------------------------------------

--
-- Table structure for table `animais`
--

CREATE TABLE `animais` (
  `id` int(11) NOT NULL,
  `nome_tutor` varchar(255) NOT NULL,
  `contato` varchar(255) NOT NULL,
  `nome_animal` varchar(255) NOT NULL,
  `especie` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- If you want insert data on the table `animais`
--

INSERT INTO `animais` (`id`, `nome_tutor`, `contato`, `nome_animal`, `especie`) VALUES
(23, 'motech noel', '+255752541568','teste', 'teste' ),
(24, 'Thiago Moses', '0712541669', 'teste', 'teste'),
(25, 'Saratex Marie', '0712541669', 'teste', 'teste'),
(26, 'Kamonyo Kiiza', '+255752541568', 'teste', 'teste');

--
--

--
-- Indexes for table `animais`
--
ALTER TABLE `animais`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `animais`
--
ALTER TABLE `animais`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=01;


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
