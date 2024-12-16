#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
    console.log("Missing number of occurrences");
}

let helper = parseInt(process.argv[2]);
let helper1 = helper;
while (helper > 0) {
    console.log("X".repeat(helper1));
    helper --;
}
