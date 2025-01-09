#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
}

let helper = parseInt(process.argv[2]);
const helper1 = helper;
while (helper > 0) {
  console.log('X'.repeat(helper1));
  helper--;
}
