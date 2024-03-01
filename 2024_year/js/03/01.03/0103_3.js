/**
Complete the function scramble(str1, str2) that returns true 
if a portion of str1 characters can be rearranged to match str2, 
otherwise returns false.

Notes:

Only lower case letters will be used (a-z). 
No punctuation or digits will be included.
Performance needs to be considered.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
 */

// !!!НЕ РЕШИЛ


function scramble(str1, str2) {
    function countLetterReturnObj (str) {
        const charCount = {};

        for (let char of str) {
            charCount[char] = (charCount[char] || 0) + 1;
        }

        return charCount;
    }

    let str1_obj = countLetterReturnObj(str1)
    let str2_obj = countLetterReturnObj(str2)

    return Object.keys(str1_obj).every(char => str1_obj[char] === str2_obj[char]);
    
    
  }
  

console.log(scramble('scriptjavx','javascript'))
console.log(scramble('scriptingjava', 'javascript'))
console.log(scramble('scriptsjava', 'javascripts'))

console.log(scramble('javscripts', 'javascript'))
console.log(scramble('jscripts', 'javascript'))
console.log(scramble('aabbcamaomsccdd', 'commas'))


// assert.strictEqual(scramble('scriptjavx',        'javascript' ), false);
// assert.strictEqual(scramble('scriptingjava',     'javascript' ), true );
// assert.strictEqual(scramble('scriptsjava',       'javascripts'), true );

// assert.strictEqual(scramble('javscripts',        'javascript' ), false);
// assert.strictEqual(scramble('jscripts',          'javascript' ), false);
// assert.strictEqual(scramble('aabbcamaomsccdd',   'commas'     ), true );
// assert.strictEqual(scramble('commas',            'commas'     ), true );
// assert.strictEqual(scramble('sammoc',            'commas'     ), true )