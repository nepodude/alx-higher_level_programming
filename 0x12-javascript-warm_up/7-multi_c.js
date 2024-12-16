#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
    console.log("Missing number of occurrences");
}

let helper = parseInt(process.argv[2]);
while (helper > 0) {
    console.log("C is fun");
    helper --;
}
