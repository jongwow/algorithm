import assert from "node:assert";

function sort(arr) {
  for (let i = 0; i < arr.length - 1; i += 1) {
    for (let j = i; j < arr.length; j += 1) {
      if (arr[j] < arr[i]) {
        let tmp = arr[j];
        arr[j] = arr[i];
        arr[i] = tmp;
      }
    }
  }
  return arr;
}
let given = [3, 2, 1, 5, 4];
let expected = [1, 2, 3, 4, 5];
let output = sort(given);

assert.deepEqual(output, expected);
// console.assert(output === expected, "Wrong answer");
