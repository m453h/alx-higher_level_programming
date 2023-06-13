#!/usr/bin/node
const { dict } = require('./101-data.js');
const newDict = {};
for (const userId in dict) {
  const occurrence = dict[userId];

  if (!newDict[occurrence]) {
    newDict[occurrence] = [userId];
  } else {
    newDict[occurrence].push(userId);
  }
}
console.log(newDict);
