-- ----------------------------------------------------------------------------
-- MySQL Workbench Migration
-- Migrated Schemata: short
-- Source Schemata: short
-- Created: Thu Sep 08 10:35:05 2016
-- Workbench Version: 6.3.7
-- ----------------------------------------------------------------------------

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------------------------------------------------------
-- Schema short
-- ----------------------------------------------------------------------------
DROP SCHEMA IF EXISTS `short` ;
CREATE SCHEMA IF NOT EXISTS `short` ;

-- ----------------------------------------------------------------------------
-- Table short.REVIEWS
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `short`.`REVIEWS` (
  `movie_id` INT NULL DEFAULT NULL,
  `user_id` INT NULL DEFAULT NULL,
  `review` INT NULL DEFAULT NULL,
  `time` DOUBLE NULL DEFAULT NULL);
SET FOREIGN_KEY_CHECKS = 1;
