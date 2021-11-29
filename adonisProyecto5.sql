-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 29-11-2021 a las 00:54:18
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `adonisProyecto5`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

CREATE TABLE `factura` (
  `id` int(11) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `placa` varchar(250) DEFAULT NULL,
  `precioPorHora` int(11) DEFAULT NULL,
  `espacio_ocupado` tinyint(1) DEFAULT NULL,
  `registro_id` varchar(190) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `info__parqueo`
--

CREATE TABLE `info__parqueo` (
  `id` int(11) NOT NULL,
  `nombreL` varchar(200) DEFAULT NULL,
  `ced_juridica` varchar(460) DEFAULT NULL,
  `duenio` varchar(200) DEFAULT NULL,
  `direccion` varchar(3500) DEFAULT NULL,
  `anio_creacion` varchar(80) DEFAULT NULL,
  `email` varchar(360) DEFAULT NULL,
  `telefono` varchar(230) DEFAULT NULL,
  `cumple_requisitos` tinyint(1) DEFAULT NULL,
  `parqueo_id` varchar(190) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `info__parqueo`
--

INSERT INTO `info__parqueo` (`id`, `nombreL`, `ced_juridica`, `duenio`, `direccion`, `anio_creacion`, `email`, `telefono`, `cumple_requisitos`, `parqueo_id`) VALUES
(1, 'Parqueo ALeman', '2551164151451415541161', 'isas aleman', '200 metros este del arbol de aguacate', '2017', 'asas@gmail.com', '56541541515515', 0, 'f8ee085b-d46a-4677-b6f2-eb52553ea95d'),
(2, 'Parqueo ALeman', '545454545485454151', 'dannd aleman', '200 metros este del arbol de aguacate', '2017', 'danda@gmail.com', '56541541515515', 0, '39d28273-5521-4675-8377-a1a745d538ad'),
(3, 'Parqueo ALeman', '515815151515', 'adonis aleman', '200 metros este del arbol de aguacate', '2017', 'adonis@gmail.com', '6235488522', 1, 'e0c70a15-4014-4886-b714-01d084157a7c'),
(4, 'Parqueo ALeman', '84551215152', 'pamela aleman', '200 metros este del arbol de aguacate', '2017', 'pamela@gmail.com', '65288155', 0, '6c3ee8b5-17d0-467f-b4ef-ebed46595011');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo__espacio`
--

CREATE TABLE `tipo__espacio` (
  `id` int(11) NOT NULL,
  `nombreC` varchar(200) DEFAULT NULL,
  `descripcion` varchar(250) DEFAULT NULL,
  `placa` varchar(90) DEFAULT NULL,
  `precioPorHora` int(11) DEFAULT NULL,
  `espacio_ocupado` tinyint(1) DEFAULT NULL,
  `registro_id` varchar(190) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `public_id` varchar(60) DEFAULT NULL,
  `name` varchar(60) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `admin` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `public_id`, `name`, `password`, `admin`) VALUES
(1, '229b8f64-d4f2-471e-8e67-166e71d27e13', 'laura', 'sha256$wXE970oixHYavXC1$afacdcfa65b5a0f6f35d669f087d417b9a20d90c717686aabcb87bb86f49d45a', 0),
(2, 'bac639f0-2efc-4a94-abc7-690393bce2fa', 'pedro', 'sha256$8INXjz3Bue0LCShN$7e060a0fcba2e7bada8a7838ac83608719ea053a3aad37452d83a5b6375b7537', 1),
(3, '1b4da7dd-579c-4ed6-8455-261040ca089c', 'camilo', 'sha256$spQMZpRxoNjSlclV$6f89ae9f646e1154d0deeaad633294cf0536ecddce7ecfd542672fe26885c281', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `factura`
--
ALTER TABLE `factura`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `registro_id` (`registro_id`);

--
-- Indices de la tabla `info__parqueo`
--
ALTER TABLE `info__parqueo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `parqueo_id` (`parqueo_id`);

--
-- Indices de la tabla `tipo__espacio`
--
ALTER TABLE `tipo__espacio`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `registro_id` (`registro_id`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `public_id` (`public_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `factura`
--
ALTER TABLE `factura`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `info__parqueo`
--
ALTER TABLE `info__parqueo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `tipo__espacio`
--
ALTER TABLE `tipo__espacio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
