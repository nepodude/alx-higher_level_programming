#!/usr/bin/node
const fs = require('fs');

const args = process.argv.slice(2);
const [file1, file2, destination] = args;

// if (!file1 || !file2 || !destination) {
//   console.error('Usage: ./concat.js <file1> <file2> <destination>');
//   process.exit(1);
// }

const content1 = fs.readFileSync(file1, 'utf8');

const content2 = fs.readFileSync(file2, 'utf8');

fs.writeFileSync(destination, content1 + content2);
