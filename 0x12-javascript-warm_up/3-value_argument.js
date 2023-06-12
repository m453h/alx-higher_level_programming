#!/usr/bin/node
const argsLength = process.argv.length - 2;
const args = process.argv;

if (argsLength < 1 || typeof args[2] === 'undefined') {
  console.log('No argument');
} else {
  console.log(args[2]);
}
