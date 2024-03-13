/**
 The main idea is to count all the occurring characters in a string. 
 If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
 */


function count(string) {
    let dct = {};
    if (string.length == 0) return dct;
    else {
        for (let el of string){
            if (el in dct) {
                dct[el] += 1;
            } 
            else dct[el] = 1;
        }
        return dct;
    }
  }