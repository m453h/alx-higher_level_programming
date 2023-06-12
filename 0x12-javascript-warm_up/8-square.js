#!/usr/bin/node
const x = parseInt(process.argv[2]);

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      process.stdout.write('X');
    }

    process.stdout.write('\n');
  }
} else {
  console.log('Missing size');
}
