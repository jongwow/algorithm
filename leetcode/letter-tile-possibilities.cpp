#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

int counts[26] = {
    0,
};
vector<int> selected;
int solve3(int n, int r, int k) {
  if (k == r) {
    for (const auto c : selected) {
      cout << char(c + 'A') << " ";
    }
    cout << endl;
    return 1;
  }
  int ret = 0;
  for (int i = 0; i < 26; i++) {
    if (counts[i] > 0) {
      selected.push_back(i);
      counts[i]--;
      ret += solve3(n, r, k + 1);
      counts[i]++;
      selected.pop_back();
    }
  }
  return ret;
}

int solve3compact(int n, int r, int k) {
  if (k == r) {
    return 1;
  }
  int ret = 0;
  for (int i = 0; i < 26; i++) {
    if (counts[i] > 0) {
      counts[i]--;
      ret += solve3(n, r, k + 1);
      counts[i]++;
    }
  }
  return ret;
}

int main() {
  string s = "Z";
  for (int i = 0; i < s.size(); i++) {
    counts[s[i] - 'A']++;
  }
  for (int i = 1; i <= s.size(); i++) {
    int ret = solve3(s.size(), i, 0);
    cout << "result: " << ret << endl;
  }