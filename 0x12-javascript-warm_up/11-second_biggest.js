#!/usr/bin/node

function findSecondBiggest (numbers) {
  if (numbers.length < 2) {
    return 0;
  }

  let largest = numbers[0];
  let secondLargest = -Infinity;

  for (const num of numbers) {
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }
  return secondLargest;
}

const args = process.argv.slice(2).map(Number);

console.log(findSecondBiggest(args));
