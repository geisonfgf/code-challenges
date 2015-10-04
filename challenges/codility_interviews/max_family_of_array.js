/*
Two non-negative integers are called siblings if they can be obtained from
each other by rearranging the digits of their decimal representations. For
example, 123 and 213 are siblings. 535 and 355 are also siblings.

A set consisting of a non-negative integer N and all of its siblings is called
the family of N. For example, the family of 553 comprises three numbers:
355, 535 and 553.

Write a function:
function solution(N);

that, given a non-negative integer N, returns the largest number in the
family of N. The function should return —1 if the result exceeds
100,000,000.

For example, given N = 213 the function should return 321. Given N = 553
the function should return 553.

Assume that:
- N is an integer within the range [0..2,147,483,647].

Complexity:
0 expected worst-case time complexity is 0(1);
0 expected worst-case space complexity is 0(1).

*/

function solution(N) {
  var result = "";
  var numbers = ('' + N).split('');

  numbers.sort(function (a, b) {
    var ab = a + b;
    var ba = b + a;
    return parseInt(ab) < parseInt(ba) ? 1 : 0;
  });

  for (var i = 0; i < numbers.length; i++) {
    result += numbers[i];
  }

  result = parseInt(result);
  if (result > 100000000)
    return -1;

  return result;
}