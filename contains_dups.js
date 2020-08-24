// Contains Duplicates - Easy

// Given an array of integers, find if the array contains any duplicates.
// Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

// Example 1:
// Input: [1,2,3,1]
// Output: true

// Example 2:
// Input: [1,2,3,4]
// Output: false

// Example 3:
// Input: [1,1,1,3,3,4,3,2,4,2]
// Output: true

//U: if an array of nums has a dup, return true. otherwise return false
//P: iterate through the array & store each value, then check if that value is present in our store. if it's there return true otherwise add it to the store & keep iterating. if it doesn't find it ever then we will end with a return false clause.
//E:

function containsDuplicate(nums) {
  //a set to keep track of our numbers in nums
  let numbers = new Set();
  //create a variable for num to use in our for loop
  let num;
  //for each number in the nums array, if our numbers set has that number entry we return true, otherwise we add that number to the numbers set & continue iterating until either the set has it so true or it doesn't so false
  for (num of nums) {
    if (numbers.has(num)) {
      return true;
    } else {
      numbers.add(num);
    }
  }
  return false;
}

//test cases from examples
console.log(containsDuplicate([1, 2, 3, 1])); //expected true
console.log(containsDuplicate([1, 2, 3, 4])); //expected false
console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])); //expected true
