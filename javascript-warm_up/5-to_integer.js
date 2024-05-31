#!/usr/bin/node

const arg = process.argv[2]; // Get the first argument
const number = parseInt(arg, 10); // Try to convert it to an integer

if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}

