#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
 public:
  int minSubArrayLen(int target, vector<int>& nums) {
    int left = 0, right = 0;
    int sum = 0, ans = 1000000;
    while (right < nums.size()) {
      sum += nums[right];
      while (sum >= target) {
        if (right - left + 1 < ans) {
          ans = right - left + 1;
        }
        sum -= nums[left];
        left++;
      }
      right++;
    }
    return ans == 1000000 ? 0 : ans;
  };
};

int main() {
  Solution sol = Solution();
  vector<int> nums(6);
  nums.push_back(2);
  nums.push_back(3);
  nums.push_back(1);
  nums.push_back(2);
  nums.push_back(4);
  nums.push_back(3);

  int answer = sol.minSubArrayLen(7, nums);
  cout << answer << endl;
}