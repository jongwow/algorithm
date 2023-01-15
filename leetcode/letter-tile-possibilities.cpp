#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;
/*
#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>
class Solution {
int visited[26] = {
    0,
};
vector<string> containers;
public:
    int numTilePossibilities(string tiles) {
        vector<char> v(tiles.begin(), tiles.end());
        vector<char> newOne;
        for (size_t i = 1; i <= v.size(); i++) {
            solve(v, newOne, v.size(), i);
        }
        return containers.size();
    }
    void solve(vector<char>& origin, vector<char>& arr, int n, int k) {
  stringstream ss;
  for (size_t i = 0; i < arr.size(); ++i) {
    ss << arr[i];
  }
  string current = ss.str();
  if (current.size() != 0 && !(std::find(containers.begin(), containers.end(),
                                         current) != containers.end())) {
    containers.push_back(current);
  }
  for (int i = 0; i < n; i++) {
    if (visited[i] == false) {
      visited[i] = true;
      arr.push_back(origin[i]);
      solve(origin, arr, n, k);
      visited[i] = false;
      arr.pop_back();
    }
  }
}
};
int cacheFactor[26] = {
    0,
};
int facto(int num) {
  if (cacheFactor[num] != 0) {
    return cacheFactor[num];
  }
  if (num == 0) {
    cacheFactor[num] = 1;
    return 1;
  }
  int ret = 1;
  for (int i = 1; i <= num; i++) {
    ret *= i;
  }
  cacheFactor[num] = ret;
  return cacheFactor[num];
}
int permutationChar(vector<char>& arr, int start, int end) {
  if (start == end) {
    cout << start << ", " << end << " : ";
    for (const auto cc : arr) {
      cout << cc << " ";
    }
    cout << endl;
    return 1;
  } else {
    int ret = 0;
    for (int i = start; i <= end; i++) {
      swap(arr[start], arr[i]);
      ret += permutationChar(arr, start + 1, end);
      swap(arr[start], arr[i]);
    }
    return ret;
  }
}
vector<int> counting(vector<char>& given) {
  vector<int> duplicated(26);  // 26 자리
  for (int i = 0; i < given.size(); i++) {
    duplicated[given[i] - 'A']++;
  }
  return duplicated;
}
int divider(vector<int>& arr) {
  int ret = 1;
  for (int i = 0; i < arr.size(); i++) {
    ret *= facto(arr[i]);
  }
  return ret;
}
// std::string s = "Hello World!";
// std::vector<char> v(s.begin(), s.end());
int visited[26] = {
    0,
};
vector<string> containers;
void solve(vector<char>& origin, vector<char>& arr, int n, int k) {
  stringstream ss;
  for (size_t i = 0; i < arr.size(); ++i) {
    ss << arr[i];
  }
  string current = ss.str();
  if (current.size() != 0 && !(std::find(containers.begin(), containers.end(),
                                         current) != containers.end())) {
    containers.push_back(current);
  }
  for (int i = 0; i < n; i++) {
    if (visited[i] == false) {
      visited[i] = true;
      arr.push_back(origin[i]);
      solve(origin, arr, n, k);
      visited[i] = false;
      arr.pop_back();
    }
  }
}
void solve2(int depth, int n, int k) {
  if (depth == k) {
    // depth 만큼 factorial
    int up = facto(depth);
    int div = 1;
    for (int i = 0; i < 26; i++) {
      if (counts[i] >= 1) {
        div *= facto(i);
      }
    }
    cout << up << " " << div << endl;
    // int down =
    // 중복된 element의 개수만큼 divide
  }
  for (int i = 0; i < n; i++) {
    if (visited[i] == false) {
      visited[i] = true;  // i 번째 index의 char를 사용했다.
      counts[i]++;        // i번째 index의 char의 사용횟수를 +1한다.
      depth++;            // depth 를 하나 증가시킨다.
      solve2(depth + 1, n, k);
      depth--;
      visited[i] = false;
      counts[i]--;
    }
  }
}
int main() {
  string s = "AAB";
  vector<char> v(s.begin(), s.end());
  int end = v.size() - 1;  // variable
  vector<char> newOne;
  for (size_t i = 1; i <= v.size(); i++) {
    solve(v, newOne, v.size(), i);
  }
  // int ret = solve(v, s.size(), 3);
  cout << containers.size() << endl;
*/
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