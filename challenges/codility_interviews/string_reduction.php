<?php
/*
The input is a string having only A, B or C.

Apply the rules below until the string not match more any rule and return
the string modified.

Rules:
    "AB" becomes "AA"
    "BA" becomes "AA"
    "CB" becomes "CC"
    "BC" becomes "CC"
    "AA" becomes "A"
    "CC" becomes "C"

Input:
    "AABCC"

Output:
    "AC"

Time complexity O(N)
Space complexity O(N)
*/

function solution($S) {
    $ans = $S;
    $stack = array();
    $sub = substr($ans, -2);
    array_push($stack, array($ans, $sub, ""));
    while ($stack) {
        list($ans, $sub, $left) = array_pop($stack);
        if ($sub == "AB" || $sub == "BA") {
            $ans = substr($ans, 0, -2) . "AA" . $left;
            $sub = substr($ans, -2);
            array_push($stack, array($ans, $sub, $left));
        } else if ($sub == "CB" || $sub == "BC") {
            $ans = substr($ans, 0, -2) . "CC" . $left;
            $sub = substr($ans, -2);
            array_push($stack, array($ans, $sub, $left));
        } else if ($sub == "AA") {
            $ans = substr($ans, 0, -2) . "A" . $left;
            $sub = substr($ans, -2);
            array_push($stack, array($ans, $sub, $left));
        } else if ($sub == "CC") {
            $ans = substr($ans, 0, -2) . "C" . $left;
            $sub = substr($ans, -2);
            array_push($stack, array($ans, $sub, $left));
        } else if ((substr($ans, -2) == "AC" || substr($ans, -2) == "CA") && strlen($ans) > 2) {
            if (strlen($ans) > 3) {
                $sub = substr($ans, 0, 2);
                $left = substr($ans, 2);
                $ans = "";
                array_push($stack, array($ans, $sub, $left));
            } else {
                $sub = substr($ans, 0, 2);
                $left = substr($ans, -1);
                $ans = "";
                array_push($stack, array($ans, $sub, $left));
            }
        } else if ($left == "BAC" || $left == "BCA" || $left == "AAC" || $left == "ACA" || $left == "CAC" || $left == "CCA") {
            $ans = $sub;
            $sub = substr($ans, -3, -1);
            $left = substr($ans, -1);
            array_push($stack, array($ans, $sub, $left));
        }
    }

    if ($ans) {
        return $ans;    
    } else {
        return $ans . $sub . $left;
    }
    
}

echo "Input: AABCC\n";
echo "Expected answer: AC\n";
echo "My answer: ". solution("AABCC");
echo "\n\n";
echo "Input: AAAABCC\n";
echo "Expected answer: AC\n";
echo "My answer: ". solution("AAAABCC");
echo "\n\n";
echo "Input: ABCABC\n";
echo "Expected answer: ACAC\n";
echo "My answer: ". solution("ABCABC");
echo "\n\n";
echo "Input: CBACBA\n";
echo "Expected answer: CACA\n";
echo "My answer: ". solution("CBACBA");
echo "\n\n";
echo "Input: BACBAC\n";
echo "Expected answer: AC\n";
echo "My answer: ". solution("BACBAC");
?>