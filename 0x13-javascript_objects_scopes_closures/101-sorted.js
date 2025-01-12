#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

const values = [...new Set(Object.values(dict))];
values.forEach((value) => {
  newDict[value] = [];
});
for (const [key, value] of Object.entries(dict)) {
  if (newDict[value]) {
    newDict[value].push(key);
  }
}
console.log(newDict);
