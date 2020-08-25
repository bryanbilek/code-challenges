//Two Sum
// Given an array of integers, return indices of the two numbers such that they add up to a specific target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.

//U: return 2 indices that equal the target
//P: iterate through & start storing the values somewhere
//P: if the target minus the current value equals a value stored, get the indices

var twoSum = function (nums, target) {
  let numbers = new Set();
  for (i = 0; i < nums.length; i++) {
    let comp = target - nums[i];
    if (numbers[comp] !== undefined && numbers[comp] !== i) {
      return [i, numbers[comp]];
    } else {
      numbers[nums[i]] = i;
    }
  }
};

console.log(twoSum([2, 7, 11, 15], 9)); //expected output is 9 in form of [0, 1]
