-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-08-2021 a las 08:09:01
-- Versión del servidor: 10.4.13-MariaDB
-- Versión de PHP: 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `_db_uthealt2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial`
--

CREATE TABLE `historial` (
  `id_historial` int(10) NOT NULL,
  `id_signos_vitales` int(10) NOT NULL,
  `fecha_actual` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona`
--

CREATE TABLE `persona` (
  `id_persona` int(10) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `apellido_paterno` varchar(30) NOT NULL,
  `apellido_materno` varchar(30) NOT NULL,
  `genero` enum('M','F') NOT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `altura` float(4,3) NOT NULL,
  `peso` float(6,2) NOT NULL,
  `ciudad` varchar(50) NOT NULL,
  `codigo_postal` int(20) NOT NULL,
  `colonia` varchar(20) NOT NULL,
  `estado` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona_medico`
--

CREATE TABLE `persona_medico` (
  `id_persona_medico` int(10) NOT NULL,
  `cedula_medica` varchar(50) NOT NULL,
  `id_persona` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `signos_vitales`
--

CREATE TABLE `signos_vitales` (
  `id_signos_vitales` int(10) NOT NULL,
  `id_persona` int(10) NOT NULL,
  `oxigeno` float(6,2) NOT NULL,
  `temperatura` float(6,2) NOT NULL,
  `calorias_quemadas` float(6,2) NOT NULL,
  `peso_diario` float(6,2) NOT NULL,
  `distancia_recorrida` float(6,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `historial`
--
ALTER TABLE `historial`
  ADD PRIMARY KEY (`id_historial`),
  ADD KEY `id_signos_vitales` (`id_signos_vitales`);

--
-- Indices de la tabla `persona`
--
ALTER TABLE `persona`
  ADD PRIMARY KEY (`id_persona`);

--
-- Indices de la tabla `persona_medico`
--
ALTER TABLE `persona_medico`
  ADD PRIMARY KEY (`id_persona_medico`),
  ADD KEY `id_persona` (`id_persona`);

--
-- Indices de la tabla `signos_vitales`
--
ALTER TABLE `signos_vitales`
  ADD PRIMARY KEY (`id_signos_vitales`),
  ADD KEY `id_persona` (`id_persona`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `historial`
--
ALTER TABLE `historial`
  MODIFY `id_historial` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `persona`
--
ALTER TABLE `persona`
  MODIFY `id_persona` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `persona_medico`
--
ALTER TABLE `persona_medico`
  MODIFY `id_persona_medico` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `signos_vitales`
--
ALTER TABLE `signos_vitales`
  MODIFY `id_signos_vitales` int(10) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `historial`
--
ALTER TABLE `historial`
  ADD CONSTRAINT `historial_ibfk_1` FOREIGN KEY (`id_signos_vitales`) REFERENCES `signos_vitales` (`id_signos_vitales`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `persona_medico`
--
ALTER TABLE `persona_medico`
  ADD CONSTRAINT `persona_medico_ibfk_1` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `signos_vitales`
--
ALTER TABLE `signos_vitales`
  ADD CONSTRAINT `signos_vitales_ibfk_1` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
