/**
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expandedForm(12); // Should return '10 + 2'
expandedForm(42); // Should return '40 + 2'
expandedForm(70304); // Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!!
 */


function expandedForm(num) {
    let text = ''
    let num_nul = String(num).length - 1
    for (let el of String(num)){
      if (el != '0') {
        text += `${el}${"0".repeat(num_nul)} + `
        
      }
      num_nul -= 1
    }
    console.log(text.slice(0, -3));
  }


  expandedForm(12); // Should return '10 + 2'
  expandedForm(42); // Should return '40 + 2'
  expandedForm(70304); // Should return '70000 + 300 + 4'