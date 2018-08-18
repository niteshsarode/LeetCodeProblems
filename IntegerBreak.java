/** 

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

**/

class Solution {
    public int integerBreak(int n) {
        int maxProd = 1;
        int x = n/3;
        if (n == 2)
            return 1;
        if (n == 3)
            return 2;
        if ((n % 3) == 0) {
            maxProd = (int) Math.pow(3,x);
        } else if((n % 3 ) == 1) {
            maxProd = (int) Math.pow(3,(x - 1)) * 4;
        } else {
            maxProd = (int) Math.pow(3,x) * 2;
        }
        return maxProd;
    }
}