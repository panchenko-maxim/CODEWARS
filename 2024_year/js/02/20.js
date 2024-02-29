/**
 Complete the solution so that the function will break up camel casing, 
 using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
 */

function solution(string) {
    result = "";
    for (let el of string){
        if (el === el.toUpperCase()) result += ` ${el}`;
        else result += el;
    }
    return result;
  }


console.log(solution(''))