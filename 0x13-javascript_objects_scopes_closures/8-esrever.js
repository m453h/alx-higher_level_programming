#!/usr/bin/node
exports.esrever = function (list) {
  let reversedList = [];
  for (let i = list.length - 1; i > -1; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
