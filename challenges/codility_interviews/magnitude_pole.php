<?php
/*
Magnitude Pole: An element in an array whose left hand side elements are
lesser than or equal to it and whose right hand side element are greater
than or equal to it.

Input:
    [3, 1, 4, 5, 9, 7, 6, 11]

Output:
    4

Time complexity O(N)
Space complexity O(N)
*/

function solution($A) {
    $length = count($A);
    $aux_maxes = array_fill(0, $length, 0);
    $aux_mins = array_fill(0, $length, 0);

    $max_value = $aux_maxes[0] = -PHP_INT_MAX;
    $min_value = $aux_mins[$length - 1] = PHP_INT_MAX;

    for ($i = $length - 1; $i >= 0; --$i) {
        if ($A[$i] < $min_value) {
            $min_value = $A[$i];
        }
        $aux_mins[$i] = $min_value;
    }

    for ($i = 0; $i < $length; $i++) {
        if ($A[$i] > $max_value) {
            $max_value = $A[$i];
        }
        $aux_maxes[$i] = $max_value;
    }
    
    for ($i = 0; $i < $length; $i++) {
        if ($A[$i] >= $aux_maxes[$i] && $A[$i] <= $aux_mins[$i]) {
            if ($i == 0) {
                return -1;
            }
            return $A[$i];
        }
    }

    return -1;
}

echo "Input: [3, 1, 4, 5, 9, 7, 6, 11]\n";
echo "Expected answer: 4\n";
echo "My answer: ", solution([3, 1, 4, 5, 9, 7, 6, 11]);
echo "\n\n";
echo "Input: [1, 2, 3, 4, 5, 6, 7, 8]\n";
echo "Expected answer: -1\n";
echo "My answer: ", solution([1, 2, 3, 4, 5, 6, 7, 8]);
echo "\n\n";
echo "Input: [8, 7, 6, 5, 4, 3, 2, 1]\n";
echo "Expected answer: -1\n";
echo "My answer: ", solution([8, 7, 6, 5, 4, 3, 2, 1]);
echo "\n\n";
echo "Input: [2, 1, 3, 5, 4, 8, 6, 7]\n";
echo "Expected answer: 3\n";
echo "My answer: ", solution([2, 1, 3, 5, 4, 8, 6, 7]);
?>