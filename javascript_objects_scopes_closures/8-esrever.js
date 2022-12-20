#!/usr/bin/node
// create function for reversed list
exports.esrever = function (list) {
  const revList = [];
  while (list.length) {
    revList.push(list.pop());
  }
  return revList;
};
