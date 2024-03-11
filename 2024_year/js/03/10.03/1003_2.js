/**
 Task
Sum all the numbers of a given array ( cq. list ), 
except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single 
element at each edge, even if there are more than one with the same value.

Mind the input validation.

Example
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
Input validation
If an empty value ( null, None, Nothing etc. ) is given 
instead of an array, or the given array is an empty list or 
a list with only 1 element, return 0.

const {assert} = require("chai");

it("example tests", ()=>{
  assert.strictEqual( sumArray(null)                     , 0 );
  assert.strictEqual( sumArray([ ])                      , 0 );
  assert.strictEqual( sumArray([ 3 ])                    , 0 );
  assert.strictEqual( sumArray([ 3, 5 ])                 , 0 );
  assert.strictEqual( sumArray([ 6, 2, 1, 8, 10 ])       , 16 );
  assert.strictEqual( sumArray([ 0, 1, 6, 10, 10 ])      , 17 );
  assert.strictEqual( sumArray([ -6, -20, -1, -10, -12 ]), -28 );
  assert.strictEqual( sumArray([ -6, 20, -1, 10, -12 ])  , 3 );
});

 */


function sumArray(array) {
    if (Array.isArray(array) && array.length > 1) {
        let max_el = Math.max(...array)
        let indx_max = array.indexOf(max_el)
        
        let min_el = Math.min(...array)
        let indx_min = array.indexOf(min_el)
        
        let sm = 0;
        for (let i=0;i != array.length;i++){
            if (i != indx_max && i != indx_min){
                sm += array[i];
            }
        }
        
        return sm;
    }
    else return 0;
}


// sumArray(null)
// sumArray([ ])

// sumArray([ 3 ])

// sumArray([ 3, 5 ])
// sumArray([ 6, 2, 1, 8, 10 ])
// sumArray([ 0, 1, 6, 10, 10 ])
// sumArray([ -6, -20, -1, -10, -12 ])
// sumArray([ -6, 20, -1, 10, -12 ])