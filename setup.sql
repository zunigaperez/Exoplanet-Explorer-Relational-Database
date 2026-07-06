--my code starts here

DROP DATABASE IF EXISTS Earth_Like_Exoplanets;

CREATE DATABASE Earth_Like_Exoplanets;

USE Earth_Like_Exoplanets;

Create Table Discoveries (
    Discovery_ID INTEGER PRIMARY KEY,
    Discovery_Facility TEXT,
    Discovery_Year Integer,
    Discovery_Method VARCHAR(100)
);

/* LOAD DATA*/
LOAD DATA INFILE '/home/coder/project/cleaned_discoveries_data.txt'
INTO TABLE Discoveries
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

/*
-- insert instance data

INSERT INTO Discoveries(Discovery_Year, Discovery_Facility, Discovery_Method)
VALUES ('Radial Velocity', 2004, 'McDonald Observatory');
-----

mysql -u root < setup.sql 

SELECT Discovery_Method
FROM Discoveries
WHERE Discovery_ID < 10;

SELECT Discovery_ID, Discovery_Method
FROM Discoveries
WHERE Discovery_ID < 10;

SELECT Discovery_ID, Discovery_Facility
FROM Discoveries
WHERE Discovery_ID < 10;

*/

Create TABLE Solar_System (
  System_ID INTEGER PRIMARY KEY,
  Host_Name TEXT,
  Number_of_Stars Integer,
  Number_of_Planets Integer,
  RA_deg FLOAT,
  Dec_deg FLOAT,
  Distance_pc FLOAT
);

LOAD DATA INFILE '/home/coder/project/cleaned_system_data.txt'
INTO TABLE Solar_System
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

/* 
SELECT * FROM Solar_System;
*/

CREATE TABLE Exoplanets (
  Planet_ID INTEGER Primary Key Auto_Increment,
  Planet_Name Text, 
  Planet_Letter Text,
  Number_of_Moons Integer,
  Orbital_Period_days FLOAT,
  Orbit_Semi_Major_Axis_au FLOAT,
  Angular_Separation_mas FLOAT, 
  Planet_Radius_Earth_Radius FLOAT,
  Planet_Mass_or_Earth_Mass FLOAT,
  Planet_Density_g_cm3 FLOAT,
  Eccentricity FLOAT,
  Insolation_Flux_Earth_Flux FLOAT,
  Equilibrium_Temperature_K FLOAT,
  Inclination_deg FLOAT,
  Transit_Midpoint_days FLOAT,
  Transit_Depth_percent FLOAT,
  Transit_Duration_hours FLOAT,
  Radial_Velocity_Amplitude_m_s FLOAT
);

LOAD DATA INFILE '/home/coder/project/cleaned_planet_data.txt'
INTO TABLE Exoplanets
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

/* 

SELECT * FROM Exoplanets;

SELECT Planet_ID, Planet_Name, Number_of_Moons, Planet_Mass_or_Earth_Mass 
FROM Exoplanets 
WHERE Planet_ID < 100;

*/

Create TABLE Stars (
  Star_ID Integer Primary Key Auto_Increment,
  System_ID Integer,
  Spectral_Type TEXT, 
  Stellar_Radius VARCHAR(50),
  Stellar_Mass_Solar_mass DOUBLE,
  Stellar_Metallicity_dex FLOAT,
  Stellar_Luminosity_log_Solar FLOAT,
  Stellar_Surface_Gravity_log10_cm_s2 FLOAT,
  Stellar_Age_Gyr FLOAT,
  Stellar_Density_g_cm3 FLOAT,
  Stellar_Rotational_Velocity_km_s FLOAT,
  Stellar_Rotational_Period_days FLOAT,
  Systemic_Radial_Velocity_km_s FLOAT,
  Foreign Key (System_ID) References Solar_System(System_ID)
);

LOAD DATA INFILE '/home/coder/project/cleaned_stars_data.txt'
INTO TABLE Stars
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

/* 
SELECT * FROM Stars;

SELECT Star_ID, System_ID, Spectral_Type, Stellar_Radius
FROM Stars 
WHERE Star_ID < 100;
*/


/*
junction  tables
SELECT * FROM Star_Exoplanet_Orbits;
*/

CREATE TABLE Star_Exoplanet_Orbits (
  Star_ID INTEGER,
  Planet_ID INTEGER, 
  PRIMARY KEY (Star_ID, Planet_ID),
  FOREIGN KEY (Star_ID) REFERENCES Stars(Star_ID),
  FOREIGN KEY (Planet_ID) REFERENCES Exoplanets(Planet_ID)
);

LOAD DATA INFILE '/home/coder/project/Star_Exoplanet_Orbits_cleaned.txt'
INTO TABLE Star_Exoplanet_Orbits
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

/*
SELECT * FROM Exoplanet_Discoveries;
*/

CREATE TABLE Exoplanet_Discoveries (
  Discovery_ID INTEGER,
  Planet_ID INTEGER,
  PRIMARY KEY (Discovery_ID, Planet_ID),
  FOREIGN KEY (Discovery_ID) REFERENCES Discoveries(Discovery_ID),
  FOREIGN KEY (Planet_ID) REFERENCES Exoplanets(Planet_ID)
);

LOAD DATA INFILE '/home/coder/project/Exoplanet_Discoveries_cleaned.txt'
INTO TABLE Exoplanet_Discoveries
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

/* 

use command below to reset and run setup.sql again:

$ mysql -u root < setup.sql 

go to mysql

$ mysql

mysql> USE Earth_Like_Exoplanets;

*/

--my code ends here 









