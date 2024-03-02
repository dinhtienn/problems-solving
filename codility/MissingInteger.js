// This is a demo task.

// Write a function:

// function solution(A);

// that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

// For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

// Given A = [1, 2, 3], the function should return 4.

// Given A = [−1, −3], the function should return 1.

// Write an efficient algorithm for the following assumptions:

// N is an integer within the range [1..100,000];
// each element of array A is an integer within the range [−1,000,000..1,000,000].

// Solution 1: 88%
function solution1(A) {
  let smallestPositiveNum = 1;
  const a = new Set();

  for (const num of A) {
    if (num === smallestPositiveNum) {
      smallestPositiveNum++;
      smallestPositiveNum = getSmallestPositiveNumInSet(smallestPositiveNum, a);
    } else if (num > smallestPositiveNum) a.add(num);
  }

  return smallestPositiveNum;
}

function getSmallestPositiveNumInSet(num, a) {
  if (a.has(num)) return getSmallestPositiveNumInSet(num + 1, a);
  return num;
}

// Solution 2: 100%
function solution2(A) {
  let min = 1;

  A.sort(function (a, b) {
    return a - b;
  });

  for (const k of A) {
    if (k === min) min++;
  }

  return min;
}

// [1, 3, 6, 4, 1, 2]
