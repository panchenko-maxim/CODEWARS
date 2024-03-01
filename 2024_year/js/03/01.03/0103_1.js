/**
Complete the solution so that it splits 
the string into pairs of two characters. 
If the string contains an odd number of characters then 
it should replace the missing second character of the final 
pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
 */


function solution(str){
   if (str.length % 2 != 0) str += '_'
   let lst = []
   for (let i = 0; i < str.length; i++){
    if (i != 0 && i % 2 == 0){
        lst.push(str[i-1,i])
    }
    
   }
   return lst
}


console.log(solution('abc'))
console.log(solution('abcdef'))
