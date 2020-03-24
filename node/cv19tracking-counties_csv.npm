#!/usr/bin/node
/*
#   2020-03-23T22:55:26
#	Unlike typical "new" node.js programs, we unwind the functions ahead of time - oldSchool().
#
*/

const https = require('https');
//const http = require('http');

// if required 'npm install csv-parser'
// https://www.npmjs.com/package/csv-parser
const csv      = require('csv-parser');
var results    = [];

online_dataset = 'https://covidtracking.com/api/counties.csv';

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
        console.log('state ', results[0].state);
        // [
        //   { NAME: 'Daffy Duck', AGE: '24' },
        //   { NAME: 'Bugs Bunny', AGE: '22' }
        // ]
    });

}


https.get(online_dataset, process).on("error", function (err)  { cosole.log("Error: " + err.message); } );

