// Multiples of 3 and 5

// Description:
// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
// Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
// Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)

//top solution
// function solution(number) {
//   var sum = 0;

//   for (var i = 1; i < number; i++) {
//     if (i % 3 == 0 || i % 5 == 0) {
//       sum += i;
//     }
//   }
//   return sum;
// }

//my solution to pass 
function solution(number) {
  //mults array to store values
  mults = [];
  //loop through each number less than the input number
  //if the number divided by 3 or 5 has no remainder push it to our mults store
  for (i = 1; i < number; i++) {
      if (i % 3 === 0 || i % 5 === 0) {
          mults.push(i);
          console.log(mults);
        }
    }
    //use the reduce array method to add the values in mults together & return that total
    let total = mults.reduce((accum, cur) => {
        return accum + cur;
    }, 0);
    return total;
}

console.log(solution(10));//expected output would be total of 23