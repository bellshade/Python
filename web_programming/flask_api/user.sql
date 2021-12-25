SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

CREATE TABLE 'user' (
  'id' int(11) NOT NULL,
  'email' varchar(50) DEFAULT NULL,
  'password' varchar(50) DEFAULT NULL,
  'name' varchar(50) DEFAULT NULL,
  'created_at' datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  'updated_at' datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table 'user'
--

INSERT INTO 'user' ('id', 'email', 'password', 'name', 'created_at', 'updated_at') VALUES
(1, 'contoh1@gmail.com', 'contoh1', 'nama1', '2021-10-04 10:36:35', '2021-10-04 10:36:35'),
(2, 'contoh2@gmail.com', 'contoh2', 'nama2', '2021-10-04 10:37:04', '2021-10-04 10:37:04');

--
-- Indexes for dumped tables
--

--
-- Indexes for table 'user'
--
ALTER TABLE 'user'
  ADD PRIMARY KEY ('id');

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table 'user'
--
ALTER TABLE 'user'
  MODIFY 'id' int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
