// Add Two Numbers

// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Example:

// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8
// Explanation: 342 + 465 = 807.

//U: given two arrays in reverse order, add them together, get a solution & return it in reverse order
//P: reverse the arrays, add them together, reverse again & return that
//E:

const addTwoNumbers = (arr1, arr2) => {
  //reverse the first array & then join it together
  revArr1 = arr1.reverse().join("");
  //reverse the first array & then join it together
  revArr2 = arr2.reverse().join("");
  //make each string a number & add those 2 numbers together
  revSum = Number(revArr1) + Number(revArr2);
  //take that sum, turn it into a string
  revSumStr = revSum.toString();
  //return that string split back into an array & reversed to fit the format of the inputs
  return revSumStr.split("").reverse();
};

console.log(addTwoNumbers([2, 4, 3], [5, 6, 4])); //expect 342 + 465 = 807 ===> [7,0,8]
console.log(addTwoNumbers([1, 2, 3], [4, 5, 6])); //expect 321 + 654 = 975 ===> [5, 7, 9]