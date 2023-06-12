#!/usr/bin/node
const argsLength = process.argv.length - 2;
if (argsLength === 0 || argsLength === 1) {
  console.log(0);
} else {
  let largest = parseInt(process.argv[2]);
  let secondLargest = parseInt(process.argv[3]);
  for (let i = 1; i < argsLength; i++) {
    const currentValue = parseInt(process.argv[i + 2]);
    if (largest < currentValue) {
      secondLargest = largest;
      largest = currentValue;
    } else if (currentValue > secondLargest &&
      currentValue !== largest) {
      secondLargest = currentValue;
    }
  }
  console.log(secondLargest);
}
