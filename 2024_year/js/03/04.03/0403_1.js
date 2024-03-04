/**
Complete the solution so that it returns true if the 
first argument(string) passed in ends with the 2nd 
argument (also a string).

Examples:

solution('abc', 'bc') // returns true
solution('abc', 'd') // returns false
 */


function solution(str, ending){
    let st = str.split('').reverse().join('');
    let end = ending.split('').reverse().join('');
    for(let i=0;i != end.length;i++){
        if (end[i] != st[i]){
            return false
        }
    }
    return true
}


console.log(solution('abc', 'bc') )
console.log(solution('abc', 'd') )