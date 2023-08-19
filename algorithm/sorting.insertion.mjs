import assert from "node:assert";

function sort(arr) {
  for (let i = 1; i < arr.length; i++) {
    let targetIndex = i;
    let targetValue = arr[i];
    for (let j = i - 1; j >= 0; j -= 1) {
      if (arr[j] > targetValue) {
        targetIndex = j;
        arr[j + 1] = arr[j];
      } else {
        break;
      }
    }
    arr[targetIndex] = targetValue;
  }
  return arr;
}

let given = [5, 7, 8, 1, 4, 6, 9];
let expected = [1, 4, 5, 6, 7, 8, 9];
let output = sort(given);
assert.deepEqual(output, expected);
