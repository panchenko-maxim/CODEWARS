/**
Write function RemoveExclamationMarks 
which removes all exclamation marks from a given string.
 */


function removeExclamationMarks(s) {
    let text = '';
    for (let el of s){
        if (el != '!') text += el;
    }
    return text;
  }