/* 
Given a string of digits, you should replace any 
digit below 5 with '0' and any digit 5 and above with '1'. 
Return the resulting string.

Note: input will never be an empty string
*/

function fakeBin(x){
    let str_num = ""
    for (let el of x) {
        if (Number(el) <= 4)
            {str_num += "0";}
        else
            {str_num += "1";}
    }
    return str_num

}

console.log(fakeBin("45385593107843568"))