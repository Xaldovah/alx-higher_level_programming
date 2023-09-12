#!/usr/bin/node

const arry = require('./100-data').list;

console.log(arry);
console.log(arry.map((x, idx) => x * idx));
