//Exes & Ohs

// Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

//examples:
//XO("ooxx") => true
// XO("xooxx") => false
// XO("ooxXm") => true
// XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
// XO("zzoo") => false

//other solution
// const XO = str => {
//   str = str.toLowerCase().split('');
//   return str.filter(x => x === 'x').length === str.filter(x => x === 'o').length;
// }

//other solution
// function XO(str) {
//   var a = str.replace(/x/gi, ''),
//       b = str.replace(/o/gi, '');
//   return a.length === b.length;
// }

//my solution
function XO(str) {
  //first convert the string to lowercase for sensitivity, then split into an array
  //run filter on the array to get the x's out & again to get the o's out
  //lastly, if the length of the x array equals the length of the o array, return true or else return false
  let arr = str.toLowerCase().split("");
  let filterX = arr.filter((a) => a === "x");
  let filterO = arr.filter((a) => a === "o");
  return filterX.length === filterO.length ? true : false;
}

console.log(XO("ooxx")); //expected true
console.log(XO("xooxx")); //expected false
console.log(XO("oOxXz")); //expected true
