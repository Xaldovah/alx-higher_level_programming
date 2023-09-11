#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (!isNaN(num) && num > 0) {
  for (let i = 0; i < num; i++) {
    console.log('c is fun');
  }
} else if (isNaN(num)) {
  console.log('Missing number of occurrences');
}
