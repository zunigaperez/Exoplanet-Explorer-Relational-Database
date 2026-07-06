


/* not my code starts here */

/* this imports the mysql12 library, and requests the promise based version of the client */
const mysql = require('mysql2/promise');

/* loads environment variables from file names .env in the project root directory into process.env */
require('dotenv').config();

const pool = mysql.createPool({
  host: process.env.DB_HOST || 'localhost',
  user: process.env.DB_USER || 'root',
  password: process.env.DB_PASSWORD || '', // If empty in .env, it defaults to empty string
  database: process.env.DB_NAME || 'Earth_Like_Exoplanets',
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0
});

module.exports = pool;


/* not my code ends here */