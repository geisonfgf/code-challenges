<?php
/*
Logic to find adjacency of numbers 0 & 1 in an array
Consider N coins aligned in a row. Each coin is showing either heads or tails.
The adjacency of these coins is the number of adjacent pairs of coins with the
same side facing up.

It must return the maximum possible adjacency that can be obtained by
reversing exactly one coin (that is, one of the coins must be reversed).
Consecutive elements of array A represent consecutive coins in the row.
Array A contains only 0s and/or 1s: 0 represents a coin with heads facing up;
1 represents a coin with tails facing up. For example, given array A
consisting of six numbers, such that:

A[0] = 1 
A[1] = 1 
A[2] = 0
A[3] = 1 
A[4] = 0 
A[5] = 0

the function should return 4. The initial adjacency is 2, as there are two
pairs of adjacent coins with the same side facing up, namely (0, 1) and
(4, 5). After reversing the coin represented by A[2], the adjacency equals 4,
as there are four pairs of adjacent coins with the same side facing up,
namely: (0, 1), (1, 2), (2, 3) and (4, 5), and it is not possible to obtain
a higher adjacency. The same adjacency can be obtained by reversing the coin
represented by A[3].

I should mention here that number of elements can be from 1....10'000. And it
has to be done as O(N)
*/

function solution($A) {
    $length = count($A);
    $heads = $tails = 0;

    for ($i = 0; $i < $length; $i++) {
        if ($A[$i] == 1) {
            $heads++;
        } else {
            $tails++;
        }
    }

    $flipped = false;
    for ($i = 0; $i < $length - 1; $i++) {
        if ($i + 2 < $length && !$flipped) {
            if (($A[$i] == 0 && $A[$i + 1] == 1 && $A[$i + 2] == 0) || ($A[$i] == 1 && $A[$i + 1] == 0 && $A[$i + 2] == 0)) {
                $flipped = true;
                $tails++;
            } else if (($A[$i] == 1 && $A[$i + 1] == 0 && $A[$i + 2] == 1) || ($A[$i] == 0 && $A[$i + 1] == 1 && $A[$i + 2] == 1)) {
                $flipped = true;
                $heads++;
            }
        }
    }

    return max($heads, $tails);
}

echo "Input: [1, 1, 0, 1, 0, 0]\n";
echo "Expected answer: 4\n";
echo "My answer: ", solution([1, 1, 0, 1, 0, 0]);
echo "\n\n";
echo "Input: [1, 1, 0, 1, 0, 0, 1, 1]\n";
echo "Expected answer: 6\n";
echo "My answer: ", solution([1, 1, 0, 1, 0, 0, 1, 1]);
echo "\n\n";
echo "Input: [1, 1, 1, 1, 1, 0, 1, 1]\n";
echo "Expected answer: 8\n";
echo "My answer: ", solution([1, 1, 1, 1, 1, 0, 1, 1]);
echo "\n\n";
echo "Input: [1, 0, 1]\n";
echo "Expected answer: 3\n";
echo "My answer: ", solution([1, 0, 1]);
echo "\n\n";
echo "Input: [0, 1, 0]\n";
echo "Expected answer: 3\n";
echo "My answer: ", solution([0, 1, 0]);
echo "\n\n";
echo "Input: [1, 1, 0, 0, 0]\n";
echo "Expected answer: 4\n";
echo "My answer: ", solution([1, 1, 0, 0, 0]);
?>