-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-09-2022 a las 16:57:48
-- Versión del servidor: 10.1.40-MariaDB
-- Versión de PHP: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `rh3`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto`
--

CREATE TABLE `puesto` (
  `idPuesto` int(11) NOT NULL,
  `codPuesto` varchar(15) NOT NULL,
  `idArea` int(11) NOT NULL,
  `nomPuesto` varchar(50) NOT NULL,
  `puestoJefeSup` varchar(50) NOT NULL,
  `jornada` varchar(70) NOT NULL,
  `remunMensual` int(11) NOT NULL,
  `prestaciones` varchar(70) NOT NULL,
  `descripcionGeneral` varchar(250) NOT NULL,
  `funciones` varchar(250) NOT NULL,
  `edad` varchar(50) NOT NULL,
  `sexo` varchar(15) NOT NULL,
  `idEstadoCivil` int(11) NOT NULL,
  `idEscolaridad` int(11) NOT NULL,
  `idGradoAvance` int(11) NOT NULL,
  `idCarrera` int(11) NOT NULL,
  `experiencia` varchar(70) NOT NULL,
  `conocimientos` varchar(70) NOT NULL,
  `manejoEquipo` varchar(70) NOT NULL,
  `reqFisicos` varchar(70) NOT NULL,
  `reqPsicologicos` varchar(70) NOT NULL,
  `responsabilidades` varchar(70) NOT NULL,
  `condicionesTrabajo` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `puesto`
--

INSERT INTO `puesto` (`idPuesto`, `codPuesto`, `idArea`, `nomPuesto`, `puestoJefeSup`, `jornada`, `remunMensual`, `prestaciones`, `descripcionGeneral`, `funciones`, `edad`, `sexo`, `idEstadoCivil`, `idEscolaridad`, `idGradoAvance`, `idCarrera`, `experiencia`, `conocimientos`, `manejoEquipo`, `reqFisicos`, `reqPsicologicos`, `responsabilidades`, `condicionesTrabajo`) VALUES
(1, 'V009', 5, 'SUPERVISOR DE TIENDA ', 'SUPERVISOR', 'LUNES A VIERNES', 5000, 'DE LEY', 'VENTAS AL PÚBLICO', 'VENDER', '18 A 45 AÑOS', 'Hombre', 1, 3, 2, 2, '2 AÑOS', 'VENTAS', 'DE COMPUTO', 'AGUDEZA VISUAL', 'MEMORIA A CORTO Y LARGO PLAZO', 'INVENTARIO', 'AGRADABLES'),
(3, 'v0008', 3, 'OBRERO', 'SUPERVISOR', 'LUNES A VIERNES', 5000, 'DE LEY', 'maquilar', 'trabajar', '18 A 45 AÑOS', 'Indistinto', 1, 2, 2, 1, '2 AÑOS', 'VENTAS', 'DE COMPUTO', 'AGUDEZA VISUAL', 'MEMORIA A CORTO Y LARGO PLAZO', 'INVENTARIO', 'AGRADABLES'),
(4, 'v010', 6, 'PROGRAMADOR', 'LIDER DE PROYECTO', 'LUNES A VIERNES 8:30am 4:30am SABADOS 9:00am  A 2:00am', 10000, 'DE LEY', 'ELABORACION DE SISTEMAS COMPUTACIONALES', 'PROGRAMAR, ANALISIS DE SISTEMAS', '18 a 70 años', 'Indistinto', 1, 3, 5, 14, '2 AÑOS', 'PROGRAMACION EN LENGUAJES JAVA, PYTHO, MANEJO DE BASES DE DATOS ', 'DE COMPUTO', 'NO NECESARIOS', 'NO NECESARIOS', 'NO ESPECIFICADAS', 'AGRADABLES'),
(5, 'p001', 5, 'JEFE DE MERCADOTECNIA', 'GERENTE', 'LUNES A VIERNES 8:30am 4:30am SABADOS 9:00am  A 2:00am', 6500, 'DE LEY', 'COORDINAR A PERSONAL DE MERCADOTECNIA', 'CORDINACIÓN', '25 A 50', 'Indistinto', 1, 3, 4, 13, '2 AÑOS', 'VENTAS', 'DE COMPUTO', 'NO NECESARIOS', 'MEMORIA A CORTO Y LARGO PLAZO', 'NO ESPECIFICADAS', 'AGRADABLES');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `puesto`
--
ALTER TABLE `puesto`
  ADD PRIMARY KEY (`idPuesto`),
  ADD KEY `idEscolaridad` (`idEscolaridad`),
  ADD KEY `idEstadoCivil` (`idEstadoCivil`),
  ADD KEY `idGradoAvance` (`idGradoAvance`),
  ADD KEY `idCarrera` (`idCarrera`),
  ADD KEY `area` (`idArea`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `puesto`
--
ALTER TABLE `puesto`
  MODIFY `idPuesto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
