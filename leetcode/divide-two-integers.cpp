#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
 public:
  int divide(int dividend, int divisor) {
    long long one = dividend;
    long long two = divisor;
    // cout << dividend << ", " << divisor << endl;
    long long result = one / two;
    if (result > 2147483647) {
      return 2147483647;
    }
    if (result < -2147483648) {
      return -2147483648;
    }
    // cout << one / two << endl;
    return one / two;
  }
  //   int divideBestSolution(int dividend, int divisor) {
  //     if (dividend == divisor) return 1;
  //     bool isPositive =
  //         (dividend < 0 ==
  //          divisor < 0);  // if both are of same sign, answer is positive
  //     unsigned int a = abs(dividend);
  //     unsigned int b = abs(divisor);
  //     unsigned int ans = 0;
  //     while (a >= b) {  // while dividend is greater than or equal to divisor
  //       short q = 0;
  //       while (a > (b << (q + 1))) q++;
  //       ans += (1 << q);   // add the power of 2 found to the answer
  //       a = a - (b << q);  // reduce the dividend by divisor * power of 2
  //       found
  //     }
  //     if (ans == (1 << 31) and
  //         isPositive)  // if ans cannot be stored in signed int
  //       return INT_MAX;
  //     return isPositive ? ans : -ans;
  //   }
};
// -2147483648
// -1
int main() {
  Solution sol = Solution();
  int result = sol.divide(-2147483648, -1);
  cout << result << endl;
}