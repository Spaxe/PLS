var args = process.argv;
var express = require("express");

function getMySQLConnection() {
    var mysql      = require('mysql');
    var connection = mysql.createConnection({
      host     : 'localhost',
      user     : 'root',
      password :'',
      database : 'PLS',
      timezone: 'aest'
    });
    connection.connect();
    console.log("Running test query to check connectivity");
    connection.query('SELECT 1 + 1 AS solution', function(err, rows, fields) {
      if (err) throw err;
      console.log('The solution is: ', rows[0].solution);
    });
    console.log("Connected successfully. Creating REST API");
    return connection;
}


//////////////////////////// Create REST endpoint for MySQL ////////////////////////////////
var restPort = 2999;
var app = express();
var connection = getMySQLConnection();
var mysqltorest  = require('mysql-to-rest');
var api = mysqltorest(app,connection);
console.log("REST Server listening on on " + restPort);
app.listen(restPort);

