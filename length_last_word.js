// Length of Last Word - LeetCode

// Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

// If the last word does not exist, return 0.

// Note: A word is defined as a maximal substring consisting of non-space characters only.

// Example:

// Input: "Hello World"
// Output: 5

//understand: return the length of the last word. if there isn't one, return 0
//plan: split the string by space to get an array of strings in order. target the last string and then return the length of it
//plan: if the length of the string is < 2, there isn't a last word so return 0

var lengthOfLastWord = function (s) {
  if (s.length < 2) {
    return 0;
  } else {
    let arr = s.split(" ");
    return arr[arr.length - 1].length;
  }
};
