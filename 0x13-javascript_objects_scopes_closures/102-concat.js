#!/usr/bin/node

const fs = require('fs');

const fileOne = process.argv[2];
const fileTwo = process.argv[3];
const fileDest = process.argv[4];

const fileOneData = fs.readFileSync(fileOne, 'utf8');
const fileTwoData = fs.readFileSync(fileTwo, 'utf8');

const fileData = fileOneData + fileTwoData;
fs.writeFileSync(fileDest, fileData, 'utf8');
