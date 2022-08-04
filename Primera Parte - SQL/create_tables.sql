CREATE DATABASE Ecommerce CHARACTER SET utf8mb4;
USE Ecommerce;

CREATE TABLE Customer (
  idCustomer INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(30) NOT NULL,
  nombre VARCHAR(20),
  apellido VARCHAR(20),
  sexo VARCHAR(10),
  direccion VARCHAR(45),
  fechaNacimiento DATE,
  telefono VARCHAR(13)
);

CREATE TABLE Category (
  idCategory INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(30),
  descripcion VARCHAR(50),
  ruta VARCHAR(30)
);

CREATE TABLE Item (
  idItem INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  producto VARCHAR(30),
  idCategory INT unsigned NOT NULL,
  FOREIGN KEY (idCategory) REFERENCES Category(idCategory)
);

CREATE TABLE Orden (
  idOrder INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  precio DECIMAL,
  fechaVenta DATE,
  idVendedor INT,
  idCustomer INT unsigned NOT NULL,
  idItem INT unsigned NOT NULL,
  FOREIGN KEY (idCustomer) REFERENCES Customer(idCustomer),
  FOREIGN KEY (idItem) REFERENCES Item(idItem)
);







