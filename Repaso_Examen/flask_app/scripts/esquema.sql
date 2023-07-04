-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema concesionario
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema concesionario
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `concesionario` DEFAULT CHARACTER SET utf8 ;
USE `concesionario` ;

-- -----------------------------------------------------
-- Table `concesionario`.`paises`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concesionario`.`paises` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `concesionario`.`fabricantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concesionario`.`fabricantes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `pais_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_fabricantes_paises1_idx` (`pais_id` ASC) VISIBLE,
  CONSTRAINT `fk_fabricantes_paises1`
    FOREIGN KEY (`pais_id`)
    REFERENCES `concesionario`.`paises` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `concesionario`.`carros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concesionario`.`carros` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `modelo` VARCHAR(45) NOT NULL,
  `año` DATE NOT NULL,
  `color` VARCHAR(45) NOT NULL,
  `precio` DOUBLE NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `fabricante_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_carros_fabricantes_idx` (`fabricante_id` ASC) VISIBLE,
  CONSTRAINT `fk_carros_fabricantes`
    FOREIGN KEY (`fabricante_id`)
    REFERENCES `concesionario`.`fabricantes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `concesionario`.`vendedores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concesionario`.`vendedores` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuario` VARCHAR(45) NOT NULL,
  `contraseña` VARCHAR(255) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `cargo` VARCHAR(45) NOT NULL,
  `porcentaje` INT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `concesionario`.`ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `concesionario`.`ventas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comprador` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `vendedor_id` INT NOT NULL,
  `carro_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ventas_vendedores1_idx` (`vendedor_id` ASC) VISIBLE,
  INDEX `fk_ventas_carros1_idx` (`carro_id` ASC) VISIBLE,
  CONSTRAINT `fk_ventas_vendedores1`
    FOREIGN KEY (`vendedor_id`)
    REFERENCES `concesionario`.`vendedores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ventas_carros1`
    FOREIGN KEY (`carro_id`)
    REFERENCES `concesionario`.`carros` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
