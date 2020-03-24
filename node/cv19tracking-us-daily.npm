#!/usr/bin/node
/*
#   2020-03-23T22:55:26
#	Unlike typical "new" node.js programs, we unwind the functions ahead of time - oldSchool().
#
*/

const https = require('https');
//const http = require('http');

online_dataset = 'https://covidtracking.com/api/us/daily';

function process (resp) {
    let data = '';

    // A chunk of data has been recieved.
    resp.on('data', function (chunk) { data += chunk; });

    // The whole response has been received. Print out the result.
    resp.on('end', function () { 
        // The next line is not USEFUL
        // console.log(JSON.parse(data).explanation);
        // dump the entire JSON file
        console.log(data);
        // parse & assign JSON to an Object
        theData = JSON.parse(data);
        // validate we got it
        console.log(theData.length);
        // Iterate over an Array, if there is one
        for (var i = 0; i < theData.length; i++) {
            //
            //console.log(Object.keys(theData[i]));
            console.log("\n**",i, theData[i]['date'], "**\n");
            Object.keys(theData[i]).forEach(x => console.log(x, theData[i][x]));
        }

    });
}

https.get(online_dataset, process).on("error", function (err)  { cosole.log("Error: " + err.message); } );

