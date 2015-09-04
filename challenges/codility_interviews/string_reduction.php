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
    $aux_string = $ans = "";

    for ($i = 0; $i < strlen($S); $i++) {
        $sub = $S[$i] . $S[$i + 1];
        if ($sub == "AB" || $sub == "BA" || $sub == "AA") {
            $aux_string .= "A";
        } else if ($sub == "CB" || $sub == "BC" || $sub == "CC") {
            $aux_string .= "C";
        } else if ($sub == "AC" || $sub == "CA") {
            $aux_string .= $sub;
        }
    }

    for ($i = 0; $i < strlen($aux_string); $i++) {
        if ($aux_string[$i] != $aux_string[$i + 1]) {
            $ans .= $aux_string[$i];
        }
        if ($i + 2 == strlen($aux_string)) {
            $ans .= $aux_string[$i + 1];
            break;
        }
    }

    return $ans;
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
echo "Expected answer: ACAC\n";
echo "My answer: ". solution("BACBAC");
echo "\n\n";
echo "Input: BACAAC\n";
echo "Expected answer: ACAC\n";
echo "My answer: ". solution("BACAAC");
echo "\n\n";
echo "Input: BACCAC\n";
echo "Expected answer: ACAC\n";
echo "My answer: ". solution("BACCAC");
echo "\n\n";
echo "Input: ACCACAC\n";
echo "Expected answer: ACACAC\n";
echo "My answer: ". solution("ACCACAC");
?>