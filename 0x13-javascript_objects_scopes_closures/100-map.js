#!/usr/bin/node
const list1 = require('./100-data').list;
console.log(list1);
const list2 = list1.map((value, index) => value * index);
console.log(list2);
