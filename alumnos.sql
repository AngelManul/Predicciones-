-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-07-2024 a las 19:37:38
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `alumnos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `Nombre` varchar(50) DEFAULT NULL,
  `Matricula` varchar(10) DEFAULT NULL,
  `Turno` varchar(10) DEFAULT NULL,
  `Plantel` varchar(20) DEFAULT NULL,
  `Edad` int(11) DEFAULT NULL,
  `Genero` varchar(10) DEFAULT NULL,
  `Promedio_General` decimal(3,2) DEFAULT NULL,
  `Porcentaje_de_asistencia` decimal(5,2) DEFAULT NULL,
  `Numero_de_materias_reprobadas` int(11) DEFAULT NULL,
  `Horas_de_estudio_semanal` int(11) DEFAULT NULL,
  `Cuatrimestres_cursados` int(11) DEFAULT NULL,
  `Tiene_beca` varchar(2) DEFAULT NULL,
  `Participa_en_actividades_extra` varchar(2) DEFAULT NULL,
  `Nivel_de_estres` varchar(10) DEFAULT NULL,
  `Satisfaccion_con_la_carrera` varchar(20) DEFAULT NULL,
  `Tiempo_para_llegar` int(11) DEFAULT NULL,
  `Es_puntual` varchar(2) DEFAULT NULL,
  `Area_de_mejora` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`Nombre`, `Matricula`, `Turno`, `Plantel`, `Edad`, `Genero`, `Promedio_General`, `Porcentaje_de_asistencia`, `Numero_de_materias_reprobadas`, `Horas_de_estudio_semanal`, `Cuatrimestres_cursados`, `Tiene_beca`, `Participa_en_actividades_extra`, `Nivel_de_estres`, `Satisfaccion_con_la_carrera`, `Tiempo_para_llegar`, `Es_puntual`, `Area_de_mejora`) VALUES
('Sergio Romero Muñoz', '220064165', 'Turno 2', 'Zona Rosa', 20, 'Hombre', 8.00, 100.00, 2, 4, 8, 'si', 'no', 'Alto', 'Muy satisfactorio', 30, 'si', NULL),
('Ana García López', '220064166', 'Turno 1', 'Londres', 21, 'Mujer', 9.20, 98.50, 0, 6, 7, 'si', 'si', 'Medio', 'Satisfactorio', 25, 'si', NULL),
('Carlos Martínez Pérez', '220064167', 'Turno 3', 'HIR', 22, 'Hombre', 7.50, 90.00, 1, 5, 6, 'no', 'si', 'Bajo', 'Satisfactorio', 40, 'no', NULL),
('María Rodríguez Sánchez', '220064168', 'Turno 2', 'Zona Rosa', 23, 'Mujer', 8.50, 95.00, 2, 3, 8, 'no', 'no', 'Alto', 'Muy satisfactorio', 20, 'si', NULL),
('José Luis Hernández', '220064169', 'Turno 1', 'Londres', 24, 'Hombre', 8.00, 100.00, 3, 7, 5, 'si', 'si', 'Medio', 'Satisfactorio', 35, 'si', NULL),
('Laura Gómez Ruiz', '220064170', 'Turno 3', 'HIR', 20, 'Mujer', 9.00, 97.00, 0, 6, 7, 'no', 'si', 'Bajo', 'Muy satisfactorio', 50, 'no', NULL),
('Miguel Fernández Ortiz', '220064171', 'Turno 2', 'Zona Rosa', 21, 'Hombre', 7.80, 92.00, 2, 4, 6, 'no', 'no', 'Alto', 'Satisfactorio', 30, 'no', NULL),
('Elena Jiménez Castro', '220064172', 'Turno 1', 'Londres', 22, 'Mujer', 8.90, 99.00, 1, 5, 8, 'si', 'si', 'Medio', 'Muy satisfactorio', 25, 'si', NULL),
('Ricardo Morales Vega', '220064173', 'Turno 3', 'HIR', 23, 'Hombre', 7.40, 89.00, 3, 7, 5, 'no', 'no', 'Bajo', 'Satisfactorio', 40, 'no', NULL),
('Patricia Torres Núñez', '220064174', 'Turno 2', 'Zona Rosa', 24, 'Mujer', 8.70, 96.00, 0, 6, 7, 'si', 'si', 'Alto', 'Muy satisfactorio', 30, 'si', NULL),
('Alejandro Vázquez Ríos', '220064175', 'Turno 1', 'Londres', 20, 'Hombre', 9.10, 98.00, 1, 5, 8, 'no', 'no', 'Medio', 'Satisfactorio', 20, 'si', NULL),
('Jesus Ivan Tercero', '220064424', 'Turno 1', 'Zona Rosa', 21, 'Hombre', 8.90, 98.00, 1, 9, 9, 'Si', 'No', 'Alto', 'Satisfecho', 30, 'Si', 'Mantener rendimiento'),
('Diego Ortiz Cervantes', '220049593', 'Turno 2', 'HIR', 21, 'Hombre', 9.00, 97.00, 0, 6, 9, 'Si', 'No', 'Alto', 'Satisfecho', 50, 'Si', 'Mantener rendimiento');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
