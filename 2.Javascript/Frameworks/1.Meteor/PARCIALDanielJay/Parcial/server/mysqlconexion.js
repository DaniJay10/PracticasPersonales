import mysql from 'mysql2/promise';


const connection = await mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'spike10',
  database: 'parcial',
});

export default connection;
