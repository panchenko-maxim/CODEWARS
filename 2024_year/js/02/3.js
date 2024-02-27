/*
Given an array of integers your solution should find the smallest integer.
For example:
Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, 
that the supplied array will not be empty.
*/


class SmallestIntegerFinder {
    findSmallestInt(args) {
      let min_num = args[0]
      for (let el of args) {
        if (el < min_num) min_num=el;
      }
      return min_num;
    }
  }


let obj = new SmallestIntegerFinder()
console.log(obj.findSmallestInt([34, 15, 88, 2]))
console.log(obj.findSmallestInt([34, -345, -1, 100]))