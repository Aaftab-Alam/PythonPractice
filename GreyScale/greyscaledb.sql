-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 16, 2022 at 07:44 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `greyscaledb`
--

-- --------------------------------------------------------

--
-- Table structure for table `emails`
--

CREATE TABLE `emails` (
  `sno` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `emails`
--

INSERT INTO `emails` (`sno`, `email`, `date`) VALUES
(1, 'aadilkhan891316@gmail.com', '2022-02-01 21:45:46'),
(2, 'hehe@gmail.com', '2022-02-01 21:46:14'),
(3, '0201CSML185@niet.co.in', '2022-02-03 22:29:42'),
(4, 'aurbete@gmail.com', '2022-02-14 23:36:10'),
(5, 'chutiya@gmail.com', '2022-02-16 00:02:20');

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `sno` int(11) NOT NULL,
  `heading` text NOT NULL,
  `description` text NOT NULL,
  `img` varchar(100) DEFAULT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `uname` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`sno`, `heading`, `description`, `img`, `date`, `uname`) VALUES
(1, 'Shoreline', 'Grayscale is open source and MIT licensed. This means you can use it for any project - even commercial projects! Download it, customize it, and publish your website!', 'bg-masthead.jpg', '2022-02-04 19:31:14', 'aadilkhan891316@gmail.com'),
(2, 'Misty', 'An example of where you can put an image of a project, or anything else, along with a description.', 'demo-image-01.jpg', '2022-02-04 20:03:02', 'aadilkhan891316@gmail.com'),
(3, 'Mountains', 'Another example of a project with its respective description. These sections work well responsively as well, try this theme on a small screen!', 'demo-image-02.jpg', '2022-02-04 19:31:14', 'aadilkhan891316@gmail.com'),
(4, 'Aaftab', 'this is my second post', 'bg-masthead.jpg', '2022-02-04 19:54:15', 'aadilkhan891316@gmail.com'),
(5, 'not to be deleted 2', 'not to be deleted', 'about-bg.jpg', '2022-02-04 21:07:20', 'aadilkhan891316@gmail.com'),
(8, 'ye wala post dekhna hai bheedu', 'jaroor  bhaiiiii', 'Annotation_2022-01-02_005412.png', '2022-02-16 23:03:45', 'aadilkhan891316@gmail.com'),
(9, 'fir se dekhega', 'jalwa', 'Planet9_3840x2160.jpg', '2022-02-04 22:55:06', 'aadilkhan891316@gmail.com'),
(14, 'ek aur post', 'ye le bhai ek post', 'about-bg.jpg', '2022-02-14 23:28:08', 'aadilkhan891316@gmail.com'),
(17, 'Aditya ka posty ', 'hehhehehehhehhehehehhehehhehehheehhehehhehehhehehe', 'ipad.png', '2022-02-16 23:45:59', 'aditya@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `uname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`sno`, `name`, `uname`, `password`) VALUES
(1, 'Aaftab Alam', 'aadilkhan891316@gmail.com', 'aa'),
(2, 'Aadil Khan', '0201CSML185@niet.co.in', '1234'),
(3, 'aaa', 'aaa@gmail.com', '1234'),
(4, 'Aditya Garg', 'aditya@gmail.com', '12345'),
(5, 'Akash Srivastva', 'akash@gmail.com', 'akash');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `emails`
--
ALTER TABLE `emails`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `emails`
--
ALTER TABLE `emails`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
