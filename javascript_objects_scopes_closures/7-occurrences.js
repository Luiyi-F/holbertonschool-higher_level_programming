#!/usr/bin/node
// write a count ocurrence in a list
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const index of list) {
    if (searchElement == index) {
      counter++;
    }
  }
  return counter;
};
