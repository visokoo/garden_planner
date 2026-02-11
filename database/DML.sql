/*
Data Manipulation Language (DML) statements for the CS340 Project
CS340 Garden Planner
Authors: Vivian Ta, Ameya Patil Patkar
GROUP 125
*/

/* -------------- [ Plant - SELECT, INSERT, DELETE ] -------------- */

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

-- delete a plant
DELETE FROM Plant WHERE plant_id = :plant_id_selected_from_plant_page

/* -------------- [ Garden - SELECT, INSERT, DELETE ] -------------- */

SELECT Garden.garden_id, Garden.name, Garden.location, CONCAT(User.first_name, ' ', User.last_name) AS Owner
FROM Garden JOIN User on Garden.user_id = User.user_id;

-- select all from Garden
SELECT * FROM Garden;

-- select all from user but combine columns first_name and last_name as owner
SELECT User.user_id, CONCAT(User.first_name, ' ', User.last_name) AS owner FROM USER;

-- delete a garden
DELETE FROM Garden WHERE garden_id = :garden_id_selected_from_garden_page

/* -------------- [ Bed - SELECT, INSERT ] -------------- */

-- get all identifying information to populate the "View All Beds" table
SELECT * FROM Bed;

-- add a new bed
INSERT INTO Bed (label, length, width, Garden_garden_id) 
VALUES(:label_input, :length_input, :width_input, :garden_id_from_dropdown_input);

-- get all garden_id and name to populate the Garden dropdown
SELECT garden_id, name FROM Garden ORDER BY name;

/* -------------- [ USER - SELECT, INSERT, UPDATE, DELETE ] -------------- */

-- get all identifying information to populate the "View All Users" table
SELECT * FROM User;

-- add a new user
INSERT INTO User (first_name, last_name) 
VALUES(:first_name_input, :last_name_input);

-- update a user
UPDATE User 
SET first_name = :first_name_input, last_name = :last_name_input;
WHERE id = :user_id_selected_from_all_users_page;

-- delete a new user
DELETE FROM User
WHERE id = :user_id_selected_from_all_users_page;

/* -------------- [ Plant_In_Bed - SELECT, INSERT, UPDATE, DELETE ] -------------- */

-- get all identifying information to populate the "View All Of My Plants" table
SELECT Plant.species, Plant.plant_category, Plant_In_Bed.id, Plant_In_Bed.date_planted, Plant_In_Bed.plant_quantity, Bed.bed_id, Bed.label
FROM Plant_In_Bed
INNER JOIN Plant ON Plant_In_Bed.Plant_plant_id = Plant.plant_id
INNER JOIN Bed ON Plant_In_Bed.Bed_bed_id = Bed.bed_id
ORDER BY Plant_In_Bed.date_planted DESC;

-- add a new plant in bed
INSERT INTO Plant_In_Bed (Plant_plant_id, Bed_bed_id, date_planted, plant_quantity) 
VALUES(:plant_id_from_dropdown_input, :bed_id_from_dropdown_input, :date_input, :plant_quantity_input);

-- get all bed_id and label to populate the Bed dropdown
SELECT bed_id, label FROM Bed ORDER BY label;

-- get all plant_id and species to populate the Plant dropdown
SELECT plant_id, species FROM Plant ORDER BY species;

-- update a plant in bed
UPDATE Plant_In_Bed
SET Plant_plant_id = :plant_id_from_dropdown_input, 
	Bed_bed_id = :bed_id_from_dropdown_input,
    date_planted = :date_input,
    plant_quantity = :plant_quantity_input
WHERE id = :plant_in_bed_id_selected_from_all_of_my_plants_page;


-- populate target plant's current data into Update Plant Form 
SELECT Plant_plant_id, Bed_bed_id, date_planted, plant_quantity
FROM Plant_In_Bed
WHERE id = :plant_in_bed_id_selected_from_all__of_my_plants_page;

-- dis-associate a plant from a bed (M-to-M relationship deletion)
DELETE FROM Plant_In_Bed 
WHERE id = :plant_in_bed_id_selected_from_all__of_my_plants_page;
-- delete a plant
DELETE FROM Plant WHERE plant_id = :plant_id_selected_from_plant_page

-- delete a garden
DELETE FROM Garden WHERE garden_id = :garden_id_selected_from_garden_page
