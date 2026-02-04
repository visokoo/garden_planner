/*
Data Manipulation Language (DML) statements for the CS340 Project
CS340 Garden Planner
Authors: Vivian Ta, Ameya Patel Patkar
GROUP 125
*/

-- select all from Plant
SELECT * FROM Plant;

-- insert new plant into Plant
INSERT INTO Plant (species, plant_category, water_requirements, sunlight, season, cycle, edible)
VALUES 
(
  :speciesInput,
  :plant_categoryInput,
  :water_requirements_from_dropdownInput,
  :sunlight_from_dropdownInput,
  :season_from_dropdownInput,
  :cycle_from_dropdownInput,
  :edible_from_radiobuttonInput
)

SELECT Garden.garden_id, Garden.name, Garden.location, CONCAT(User.first_name, ' ', User.last_name) AS Owner
FROM Garden JOIN User on Garden.user_id = User.user_id;

-- select all from Garden
SELECT * FROM Garden;

-- select all from user but combine columns first_name and last_name as owner
SELECT User.user_id, CONCAT(User.first_name, ' ', User.last_name) AS owner FROM USER;

-- delete a plant
DELETE FROM Plant WHERE plant_id = :plant_id_selected_from_plant_page

-- delete a garden
DELETE FROM Garden WHERE garden_id = :garden_id_selected_from_garden_page
