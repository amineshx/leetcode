<?php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function longestPalindrome($s) {
        $n = strlen($s);
        $start = 0;   
        $maxLen = 1;  
        
        $arrOfChecks = array_fill(0, $n, array_fill(0, $n, false)); 
        
        for ($i = 0; $i < $n; $i++) {
            $arrOfChecks[$i][$i] = true;
        }
        
        // Check for substrings of length 2
        for ($i = 0; $i < $n - 1; $i++) {
            if ($s[$i] == $s[$i + 1]) {
                $arrOfChecks[$i][$i + 1] = true;
                $start = $i;
                $maxLen = 2;
            }
        }
        
        // Check for substrings > 2
        for ($k = 3; $k <= $n; $k++) {
            for ($i = 0; $i < $n - $k + 1; $i++) {
                $j = $i + $k - 1;
                if ($arrOfChecks[$i + 1][$j - 1] && $s[$i] == $s[$j]) {
                    $arrOfChecks[$i][$j] = true;
                    if ($k > $maxLen) {
                        $start = $i;
                        $maxLen = $k;
                    }
                }
            }
        }
        
        return substr($s, $start, $maxLen);

        }
}
?>