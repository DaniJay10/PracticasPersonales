CREATE TABLE auditoriaPersona (
 IDauditoria INT AUTO_INCREMENT PRIMARY KEY,
 fecha DATETIME NOT NULL,
 IDobjeto INT,
 Tabla VARCHAR(30),
 Usuario VARCHAR(100),
 Operacion CHAR(6) NOT NULL,
CHECK(Operacion = "INSERT" or Operacion="DELETE" or Operacion="UPDATE"));


CREATE TABLE auditoriaEmpleado (
 IDauditoria INT AUTO_INCREMENT PRIMARY KEY,
 fecha DATETIME NOT NULL,
 IDobjeto INT,
 Tabla VARCHAR(30),
 Usuario VARCHAR(100),
 Operacion CHAR(6) NOT NULL,
CHECK(Operacion = "INSERT" or Operacion="DELETE" or Operacion="UPDATE"));

CREATE TABLE auditoriaCliente (
 IDauditoria INT AUTO_INCREMENT PRIMARY KEY,
 fecha DATETIME NOT NULL,
 IDobjeto INT,
 Tabla VARCHAR(30),
 Usuario VARCHAR(100),
 Operacion CHAR(6) NOT NULL,
CHECK(Operacion = "INSERT" or Operacion="DELETE" or Operacion="UPDATE"));

CREATE TABLE auditoriaCompra(
 IDauditoria INT AUTO_INCREMENT PRIMARY KEY,
 fecha DATETIME NOT NULL,
 IDobjeto INT,
 Tabla VARCHAR(30),
 Usuario VARCHAR(100),
 Operacion CHAR(6) NOT NULL,
CHECK(Operacion = "INSERT" or Operacion="DELETE" or Operacion="UPDATE"));

CREATE TABLE auditoriaPuntoVenta (
 IDauditoria INT AUTO_INCREMENT PRIMARY KEY,
 fecha DATETIME NOT NULL,
 IDobjeto INT,
 Tabla VARCHAR(30),
 Usuario VARCHAR(100),
 Operacion CHAR(6) NOT NULL,
CHECK(Operacion = "INSERT" or Operacion="DELETE" or Operacion="UPDATE"));


CREATE TABLE auditoriaCamionCarga (
 IDauditoria INT AUTO_INCREMENT PRIMARY KEY,
 fecha DATETIME NOT NULL,
 IDobjeto INT,
 Tabla VARCHAR(30),
 Usuario VARCHAR(100),
 Operacion CHAR(6) NOT NULL,
CHECK(Operacion = "INSERT" or Operacion="DELETE" or Operacion="UPDATE"));

CREATE TABLE auditoriaLoteProduccion (
 IDauditoria INT AUTO_INCREMENT PRIMARY KEY,
 fecha DATETIME NOT NULL,
 IDobjeto INT,
 Tabla VARCHAR(30),
 Usuario VARCHAR(100),
 Operacion CHAR(6) NOT NULL,
CHECK(Operacion = "INSERT" or Operacion="DELETE" or Operacion="UPDATE"));


CREATE TABLE auditoriaFinca (
 IDauditoria INT AUTO_INCREMENT PRIMARY KEY,
 fecha DATETIME NOT NULL,
 IDobjeto INT,
 Tabla VARCHAR(30),
 Usuario VARCHAR(100),
 Operacion CHAR(6) NOT NULL,
CHECK(Operacion = "INSERT" or Operacion="DELETE" or Operacion="UPDATE"));

CREATE TABLE auditoriaAlimento (
 IDauditoria INT AUTO_INCREMENT PRIMARY KEY,
 fecha DATETIME NOT NULL,
 IDobjeto INT,
 Tabla VARCHAR(30),
 Usuario VARCHAR(100),
 Operacion CHAR(6) NOT NULL,
CHECK(Operacion = "INSERT" or Operacion="DELETE" or Operacion="UPDATE"));

CREATE TABLE auditoriaEstablo (
 IDauditoria INT AUTO_INCREMENT PRIMARY KEY,
 fecha DATETIME NOT NULL,
 IDobjeto INT,
 Tabla VARCHAR(30),
 Usuario VARCHAR(100),
 Operacion CHAR(6) NOT NULL,
CHECK(Operacion = "INSERT" or Operacion="DELETE" or Operacion="UPDATE"));


CREATE TABLE auditoriaAnimal  (
 IDauditoria INT AUTO_INCREMENT PRIMARY KEY,
 fecha DATETIME NOT NULL,
 IDobjeto INT,
 Tabla VARCHAR(30),
 Usuario VARCHAR(100),
 Operacion CHAR(6) NOT NULL,
CHECK(Operacion = "INSERT" or Operacion="DELETE" or Operacion="UPDATE"));