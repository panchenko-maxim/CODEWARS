/**
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
 */


function findAverage(array) {
    if (array.length == 0) return 0
    return array.reduce((count, val)=> count + val, 0) / array.length
  }