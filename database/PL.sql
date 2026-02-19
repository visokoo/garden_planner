-- OSU CS340
-- Garden Planner Stored Procedures
 
DROP PROCEDURE  IF EXISTS sp_load_garden_planner_db;
DELIMITER //
  CREATE PROCEDURE sp_load_garden_planner_db()
  BEGIN
      -- Create database and use it
      -- un comment these if NOT using the CS340 database
      -- CREATE DATABASE IF NOT EXISTS `movie`;
      -- USE `movie`;
  
    SET FOREIGN_KEY_CHECKS=0;
    SET AUTOCOMMIT = 0;

    /* Drop table if exists */
    DROP TABLE IF EXISTS Plant;
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Garden;
    DROP TABLE IF EXISTS Bed;
    DROP TABLE IF EXISTS Plant_in_Bed;

    /* Create Plant table
    For storing all plant species that the user will be using in their garden
    with relevant attributes
    */
    CREATE TABLE Plant (
      plant_id INT NOT NULL AUTO_INCREMENT,
      species VARCHAR(150) NOT NULL,
      plant_category VARCHAR(50) NOT NULL,
      water_requirements ENUM('Low', 'Moderate', 'High') NOT NULL,
      sunlight ENUM('Shade', 'Partial', 'Full') NOT NULL,
      season ENUM('Spring', 'Summer', 'Autumn', 'Winter', 'Year-Round') NOT NULL,
      cycle ENUM('Annual', 'Perennial', 'Biennial') NOT NULL,
      edible TINYINT NOT NULL DEFAULT 0,
      PRIMARY KEY (plant_id)
    );

    /* Create User table 
    For storing all users in the household so we can link them back to the
    gardens they own
    */
    CREATE TABLE User (
      user_id INT NOT NULL AUTO_INCREMENT,
      first_name VARCHAR(50) NOT NULL,
      last_name VARCHAR(50) NOT NULL,
      PRIMARY KEY (user_id)
    );

    /* Create Garden table
    For storing all gardens in the household where beds and users are tied to
    */
    CREATE TABLE Garden (
      garden_id INT NOT NULL AUTO_INCREMENT,
      description VARCHAR(100),
      location VARCHAR(50) NOT NULL,
      user_id INT NOT NULL,
      PRIMARY KEY (garden_id),
      UNIQUE (location), 
      FOREIGN KEY (user_id) REFERENCES User(user_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
    );

    /* Create Bed table
    For storing all beds that plants belong in with the associated garden that
    the beds belong in
    */
    CREATE TABLE Bed (
      bed_id INT NOT NULL AUTO_INCREMENT,
      label VARCHAR(50) NOT NULL,
      length INT NOT NULL,
      width INT NOT NULL,
      garden_id INT NOT NULL,
      PRIMARY KEY (bed_id),
      FOREIGN KEY (garden_id) REFERENCES Garden(garden_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
    );

    /* Create Plant_in_Bed table
    For tracking when and what plant was planted in a particular bed
    */
    CREATE TABLE Plant_in_Bed (
      id INT NOT NULL AUTO_INCREMENT,
      plant_id INT NOT NULL,
      bed_id INT NOT NULL,
      date_planted DATE NOT NULL,
      plant_quantity INT NOT NULL,
      PRIMARY KEY (id),
      FOREIGN KEY (plant_id) REFERENCES Plant(plant_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
      FOREIGN KEY (bed_id) REFERENCES Bed(bed_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
    );

    /* Insert data into Plant table */
    INSERT INTO Plant (species, plant_category, water_requirements, sunlight, season, cycle, edible)
    VALUES
    ('Tomato', 'Vegetable', 'Moderate', 'Full', 'Summer', 'Perennial', 1 ),
    ('Sunflower', 'Flower', 'Low', 'Full', 'Summer', 'Annual', 1),
    ('Camellia', 'Flower', 'Moderate', 'Shade', 'Autumn', 'Perennial', 1),
    ('Orchid', 'Flower', 'High', 'Partial', 'Autumn', 'Perennial', 0);

    /* Insert data into User table */
    INSERT INTO User (first_name, last_name)
    VALUES
    ('Ned', 'Stark'),
    ('Catelyn', 'Stark'),
    ('Sansa', 'Stark'),
    ('Arya', 'Stark');

    /* Insert data into Garden table */
    INSERT INTO Garden (description, location, user_id)
    VALUES
    ('Succulent garden', 'Backyard', (SELECT User.user_id FROM User WHERE User.first_name = 'Ned' AND User.last_name = 'Stark')),
    ('Native plant garden', 'Front yard', (SELECT User.user_id FROM User WHERE User.first_name = 'Ned' AND User.last_name = 'Stark')),
    ('Vegetable garden', 'Greenhouse', (SELECT User.user_id FROM User WHERE User.first_name = 'Catelyn' AND User.last_name = 'Stark')),
    ('Wildflower garden', 'Field', (SELECT User.user_id FROM User WHERE User.first_name = 'Sansa' AND User.last_name = 'Stark'));

    /* Insert data into Bed table */
    INSERT INTO Bed (label, length, width, garden_id)
    VALUES
    ('Wildflowers', 20, 5, (SELECT Garden.garden_id FROM Garden WHERE Garden.location = 'Greenhouse')),
    ('Vegetables', 20, 5, (SELECT Garden.garden_id FROM Garden WHERE Garden.location = 'Front yard')),
    ('Pollinator plants', 6, 3, (SELECT Garden.garden_id FROM Garden WHERE Garden.location = 'Backyard')),
    ('Herbs', 10, 4, (SELECT Garden.garden_id FROM Garden WHERE Garden.location = 'Front yard'));

    /* Insert data into Plant_in_Bed table */
    INSERT INTO Plant_in_Bed (plant_id, bed_id, date_planted, plant_quantity)
    VALUES
    ((SELECT Plant.plant_id FROM Plant WHERE Plant.species = 'Camellia'), (SELECT Bed.bed_id FROM Bed WHERE Bed.label = 'Wildflowers'), '2026-03-05', 5),
    ((SELECT Plant.plant_id FROM Plant WHERE Plant.species = 'Sunflower'), (SELECT Bed.bed_id FROM Bed WHERE Bed.label = 'Pollinator plants'), '2026-06-19', 3),
    ((SELECT Plant.plant_id FROM Plant WHERE Plant.species = 'Orchid'), (SELECT Bed.bed_id FROM Bed WHERE Bed.label = 'Wildflowers'), '2026-08-23', 4),
    ((SELECT Plant.plant_id FROM Plant WHERE Plant.species = 'Tomato'), (SELECT Bed.bed_id FROM Bed WHERE Bed.label = 'Vegetables'), '2026-10-03', 6);

    /* Turn back on foreign key checks */
    SET FOREIGN_KEY_CHECKS=1;
    COMMIT;
  END //
DELIMITER ;

/* Inserts a new plant into Plant */
DROP PROCEDURE  IF EXISTS sp_insert_into_plant;
DELIMITER //
  CREATE PROCEDURE sp_insert_into_plant(
    IN species VARCHAR(150),
    IN plant_category VARCHAR(50),
    IN water_requirements ENUM('Low', 'Moderate', 'High'),
    IN sunlight ENUM('Shade', 'Partial', 'Full'),
    IN season ENUM('Spring', 'Summer', 'Autumn', 'Winter', 'Year-Round'),
    IN cycle ENUM('Annual', 'Perennial', 'Biennial'),
    IN edible BOOLEAN,
    OUT new_plant_id INT
  )
  COMMENT 'Insert new plant and return new plant ID'
  BEGIN
    INSERT INTO `Plant` (species, plant_category, water_requirements, sunlight, season, cycle, edible)
    VALUES
    (species, plant_category, water_requirements, sunlight, season, cycle, edible);

    SET new_plant_id = LAST_INSERT_ID();
  END //
DELIMITER ;

/* Inserts a new plant into Plant */
DROP PROCEDURE  IF EXISTS sp_insert_into_plant_in_bed;
DELIMITER //
  CREATE PROCEDURE sp_insert_into_plant_in_bed(
    IN plant_id INT,
    IN bed_id INT,
    IN date_planted DATE, 
    IN plant_quantity INT,
    OUT new_plant_in_bed_id INT
  )
  COMMENT 'Insert new plant in bed and return new plant in bed ID'
  BEGIN
    INSERT INTO `Plant_in_Bed` (plant_id, bed_id, date_planted, plant_quantity)
    VALUES
    (plant_id, bed_id, date_planted, plant_quantity);

    SET new_plant_in_bed_id = LAST_INSERT_ID();
  END //
DELIMITER ;

/* Inserts a new user into User */
DROP PROCEDURE  IF EXISTS sp_insert_into_user;
DELIMITER //
  CREATE PROCEDURE sp_insert_into_user(
    IN first_name VARCHAR(50),
    IN last_name VARCHAR(50),
    OUT new_user_id INT
  )
  COMMENT 'Insert new user and return new user ID'
  BEGIN
    INSERT INTO `User` (first_name, last_name)
    VALUES
    (first_name, last_name);

    SET new_user_id = LAST_INSERT_ID();
  END //
DELIMITER ;

/* Inserts a new garden into Garden */
DROP PROCEDURE  IF EXISTS sp_insert_into_garden;
DELIMITER //
  CREATE PROCEDURE sp_insert_into_garden(
    IN description VARCHAR(100),
    IN location VARCHAR(50),
    IN user_id INT,
    OUT new_garden_id INT
  )
  COMMENT 'Insert new garden and return new garden ID'
  BEGIN
    INSERT INTO `Garden` (description, location, user_id)
    VALUES
    (description, location, user_id);

    SET new_garden_id = LAST_INSERT_ID();
  END //
DELIMITER ;

/* Inserts a new bed into Bed */
DROP PROCEDURE  IF EXISTS sp_insert_into_bed;
DELIMITER //
  CREATE PROCEDURE sp_insert_into_bed(
    IN label VARCHAR(50),
    IN length INT,
    IN width INT,
    IN garden_id INT,
    OUT new_bed_id INT
  )
  COMMENT 'Insert new bed and return new bed ID'
  BEGIN
    INSERT INTO `Bed` (label, length, width, garden_id)
    VALUES
    (label, length, width, garden_id);

    SET new_bed_id = LAST_INSERT_ID();
  END //
DELIMITER ;
