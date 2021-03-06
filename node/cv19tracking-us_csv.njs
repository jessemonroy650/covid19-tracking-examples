#!/usr/bin/node
/*
#   2020-03-23T22:55:26
#	Unlike typical "new" node.js programs, we unwind the functions ahead of time - oldSchool().
#
#   The program is a merger of these two documents
    https://www.npmjs.com/package/csv-parser
    https://stackoverflow.com/questions/37899263/pipe-function-in-node-and-http-get/40480854

    NOTE: 
#
*/

const https = require('https');
//const http = require('http');

// if required 'npm install csv-parser'
// https://www.npmjs.com/package/csv-parser
const csv      = require('csv-parser');
var results    = [];

online_dataset = 'https://covidtracking.com/api/us.csv';

function process (response) {
    // connect .pipe() to the response
    response.pipe(csv())
    .on('data', (data) => results.push(data) )
    .on('end', () => {
        // show the entire array
        console.log(results);
        // show the first row in the CSV table (after the labels) as a JSON key-value pair
        console.log(results[0]);
        // from the first row in the table, show the item in the 'positive' column
        console.log('positive ', results[0].positive);
        // [
        //   { NAME: 'Daffy Duck', AGE: '24' },
        //   { NAME: 'Bugs Bunny', AGE: '22' }
        // ]
    });

}

https.get(online_dataset, process).on("error", function (err)  { cosole.log("Error: " + err.message); } );

