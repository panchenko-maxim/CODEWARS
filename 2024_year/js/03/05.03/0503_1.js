/**
An isogram is a word that has no repeating letters, consecutive 
or non-consecutive. Implement a function that determines whether a 
string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
 */


function isIsogram(str){
    let str_ = str.toLowerCase();
    let obj = {};
    for(let el of str_){
        if(!(el in obj)) obj[`${el}`] = 0;
        obj[`${el}`] += 1;
    }
    for (let el in obj){ 
        if (obj[el] != 1) return false;
    }
    return true;
  }


console.log(isIsogram("aba"))