#!/usr/bin/node
const argsLength = process.argv.length - 2;

if (argsLength < 1 || typeof process.argv[2] === 'undefined') {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
