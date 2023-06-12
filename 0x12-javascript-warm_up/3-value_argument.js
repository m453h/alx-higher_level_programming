#!/usr/bin/node
const argsLength = process.argv.length - 2;
if (argsLength === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
