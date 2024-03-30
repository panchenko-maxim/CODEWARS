/*
Task Overview
Given a non-negative integer n, write a function to_binary/ToBinary which returns that number in a binary format.
*/



function toBinary(n) {
    let binaryString = "";
    let quotient = n;
  
    while (quotient > 0) {
      const remainder = quotient % 2;
      quotient = Math.floor(quotient / 2);
      binaryString = remainder + binaryString;
    }
  
    return Number(binaryString);
  }