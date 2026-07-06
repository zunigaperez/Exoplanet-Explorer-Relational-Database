## Exoplanet Explorer Relational Database##

This project is a relational database and Node.js web application designed to analyze exoplanetary data from the NASA Exoplanet Archive. The goal is to provide a structured way to filter, locate, and learn about potential Earth-like planets using scientific data points.

###Project Overview###

This application demonstrates the complete database lifecycle:

Data Curation: Cleaning and normalizing raw exoplanetary data.

Relational Modeling: Implementing a schema in MySQL with junction tables to handle many-to-many relationships (Stars/Planets/Discoveries).

Web Interface: A dynamic Node.js web application for querying the database to answer specific habitability research questions.

###Features###

Earth-Like Filters: Search for exoplanets based on radius, equilibrium temperature, and mass.

Location Tracking: View host stars and their respective solar systems using SQL JOIN operations.

Discovery History: Track exoplanet discoveries by year, facility, and method.

Normalized Database: Schema adheres to 3NF, ensuring data integrity and efficiency.

###Getting Started###
Prerequisites

Node.js installed

MySQL Server installed

npm (Node Package Manager)

###Installation###

Clone the repository or download the project files.

Install the necessary dependencies: npm install mysql2 express ejs dotenv

Set up your .env file with your database credentials:npm install mysql2 express ejs dotenv

Set up your .env file with your database credentials: 
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=Earth_Like_Exoplanets


###Database Setup###

Open your MySQL terminal.

Run the provided setup script: mysql -u root -p < setup.sql

###Running the Application###

Start the server:node server.js

Open your browser and navigate to http://localhost:3000.

###Documentation###

Report: See Exoplanet Explorer Project.pdf for the full ER diagram, normalization analysis, and research reflection.

Data Source: NASA Exoplanet Archive


