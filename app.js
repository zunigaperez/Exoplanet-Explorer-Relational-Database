

/* not my code starts here */

const express = require('express');
const pool = require('./database'); // Ensure this matches your file name
const app = express();

require('dotenv').config();

// --- REQUIRED BOILERPLATE ---
app.set('view engine', 'ejs'); 

// --- ROUTE: Home/Search ---
app.get('/', async (req, res) => {
    try {
        const { planet_name, min_mass,
            min_planet_radius_earth_radius,
            min_equilibrium_temperature_k } = req.query;
        let query = 'SELECT * FROM Exoplanets';
        let conditions = [];
        let params = [];

        // Build conditions dynamically
        if (planet_name) {
            conditions.push('Planet_Name LIKE ?');
            params.push(`%${planet_name}%`);
        }
        if (min_mass && !isNaN(min_mass)) {
            conditions.push('Planet_Mass_or_Earth_Mass >= ?');
            params.push(parseFloat(min_mass));
        }

        //my code starts here

        if (min_planet_radius_earth_radius && !isNaN(min_planet_radius_earth_radius)) {
            conditions.push('Planet_Radius_Earth_Radius >= ?');
            params.push(parseFloat(min_planet_radius_earth_radius));
        }

          if (min_equilibrium_temperature_k && !isNaN(min_equilibrium_temperature_k)) {
            conditions.push('Equilibrium_Temperature_K >= ?');
            params.push(parseFloat(min_equilibrium_temperature_k));
        }

        //my code ends here

        // Apply filters if they exist
        if (conditions.length > 0) {
            query += ' WHERE ' + conditions.join(' AND ');
        }

     

        const [rows] = await pool.query(query, params);
        
        res.render('index', { 
            title: 'Exoplanet Explorer', 
            data: rows,
            planet_name: planet_name || '',
              //my code starts here
            min_mass: min_mass || '',
            min_planet_radius_earth_radius: min_planet_radius_earth_radius || '', 
            min_equilibrium_temperature_k: min_equilibrium_temperature_k || ''
              //my code starts here
        });
        
    } catch (err) {
        console.error(err);
        res.status(500).send('Error retrieving data from the database');
    }
});

// --- ROUTE: Habitability Analysis ---
app.get('/analyze', async (req, res) => {
    try {

          //my code starts here
        const query = `
            SELECT Planet_Name, Planet_Radius_Earth_Radius, Equilibrium_Temperature_K 
            FROM Exoplanets
            WHERE Planet_Radius_Earth_Radius BETWEEN 0.5 AND 2.5
            AND Equilibrium_Temperature_K BETWEEN 150 AND 500
        `;

          //my code ends here
        
        const [rows] = await pool.query(query);
        
        res.render('index', { 
            title: 'Earth-Like Candidates Analysis', 
            data: rows 
        });
    } catch (err) {
        console.error(err);
        res.status(500).send('Error performing analysis');
    }
});

//my code starts here
app.get('/locate', async (req, res) => {
    try {

    
        const query = `
            SELECT 
                e.Planet_Name, 
                ss.Host_Name,
                s.Star_ID,
                s.Spectral_Type
                FROM Exoplanets e
                JOIN Star_Exoplanet_Orbits seo ON e.Planet_ID = seo.Planet_ID
                JOIN Stars s ON seo.Star_ID = s.Star_ID
                JOIN Solar_System ss ON s.System_ID = ss.System_ID
        `;
        
        const [rows] = await pool.query(query);
        
        res.render('index', { 
            title: 'Locate Exoplanets', 
            data: rows 
        });
    } catch (err) {
        console.error(err);
        res.status(500).send('Error loading location data');
    }
});

app.get('/discover', async (req, res) => {
    try {

    
        const query = `
            SELECT 
                e.Planet_Name, 
                d.Discovery_Year,
                d.Discovery_Facility,
                d.Discovery_Method
                FROM Exoplanets e
                JOIN Exoplanet_Discoveries ed ON e.Planet_ID = ed.Planet_ID
                JOIN Discoveries d ON ed.Discovery_ID = d.Discovery_ID
        `;
        
        const [rows] = await pool.query(query);
        
        res.render('index', { 
            title: 'Exoplanet Discoveries', 
            data: rows 
        });
    } catch (err) {
        console.error(err);
        res.status(500).send('Error loading discovery data');
    }
});

//things to add
//add a link to Star_ID and all the entries in that row

//my code ends here

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});



/* not my code ends here           

*/