#include <algorithm>
#include <iostream>
#include <vector>
#define INF 1000000

using namespace std;

int solve2(vector<int>& nums) {
  vector<int> partialSum;
  int best = -INF;
  int sum = 0;
  int gap = 0;
  int maxValue = -INF;
  int minValue = INF;

  for (int i = 0; i < nums.size() - 1; i++) {
    int left = nums[i];
    int right = nums[i + 1];
    sum += abs(right - left);
    int extraStart = abs(nums[0] - right) - abs(right - left);
    int extraEnd = abs(nums[nums.size() - 1] - left) - abs(right - left);
    gap = max(max(gap, extraStart), extraEnd);
    maxValue = max(maxValue, min(left, right));
    minValue = min(minValue, max(left, right));
  }
  return sum + max(gap, (maxValue - minValue) * 2);
}
int solve3(vector<int>& nums) {
  int sum = 0;
  int lowest = INF;
  int highest = -INF;
  int edgeCase = -INF;
  for (int i = 0; i < nums.size() - 1; i++) {
    /*
    순회하면서, nums[i], nums[i+1] 중 큰 값이 가장 작은 값일 때,
    순회하면서, nums[i], nums[i+1] 중 작은 값이 가장 큰 값일 때,
    */
    int a = nums[i];
    int b = nums[i + 1];
    int minAmong = min(a, b);
    int maxAmong = max(a, b);

    if (maxAmong < lowest) {
      lowest = maxAmong;
    }
    if (minAmong > highest) {
      highest = minAmong;
    }
    // 0번째 index와의 비교
    int firstIndexValue =
        max(nums[0], b) - min(nums[0], b) - maxAmong + minAmong;
    if (edgeCase < firstIndexValue) {
      edgeCase = firstIndexValue;
    }
    // n-1번째 index와의 비교
    int lastIndexValue = max(nums[nums.size() - 1], a) -
                         min(nums[nums.size() - 1], a) - maxAmong + minAmong;
    if (edgeCase < lastIndexValue) {
      edgeCase = lastIndexValue;
    }
    sum += maxAmong - minAmong;
  }
  sum += max(edgeCase, (highest - lowest) * 2);
  return sum;
}
// if (i == 0) {
// }
// if (i == nums.size() - 1 - 1) {
// }

int solve(vector<int>& nums) {
  int sum = 0;
  int best = -INF;
  for (int left = 0; left < nums.size() - 1; left++) {
    sum += abs(nums[left] - nums[left + 1]);
    for (int right = left + 1; right < nums.size(); right++) {
      int red;
      int red2;
      int blue;
      int blue2;
      if (left == 0) {  // 끝이라면
        red = 0;
        red2 = 0;
      } else {
        red = abs(nums[left - 1] - nums[left]);
        red2 = abs(nums[left - 1] - nums[right]);
      }
      if (right == nums.size() - 1) {  // 끝이라면
        blue = 0;
        blue2 = 0;
      } else {
        blue = abs(nums[right] - nums[right + 1]);
        blue2 = abs(nums[left] - nums[right + 1]);
      }
      int opt = red2 + blue2 - red - blue;
      if (best < opt) {
        // cout << left << ", " << right << endl;
        best = opt;
      }
    }
  }
  return sum + best;
}
void printVector(vector<int>& arr) {
  for (size_t i = 0; i < arr.size(); i++) {
    cout << arr[i] << " ";
  }
  cout << endl;
}

int main() {
  vector<int> ret;
  vector<int> answer;
  // ret.push_back(2);
  // ret.push_back(3);
  // ret.push_back(1);
  // ret.push_back(5);
  // ret.push_back(4);

  // ret.push_back(2);
  // ret.push_back(4);
  // ret.push_back(9);
  // ret.push_back(24);
  // ret.push_back(2);
  // ret.push_back(1);
  // ret.push_back(10);
  ret.push_back(2);
  ret.push_back(5);
  ret.push_back(1);
  ret.push_back(3);
  ret.push_back(4);

  for (size_t i = 0; i < ret.size(); i++) {
    answer.push_back(ret[i]);
  }

  cout << solve3(ret) << endl;
  cout << solve2(answer) << endl;
  return 0;
}