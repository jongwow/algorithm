#include <algorithm>
#include <iostream>
#include <vector>
#define ll long long

using namespace std;
vector<ll> answers;
bool visited[10];
bool cmp(ll a, ll b) { return a < b; }

ll makeNumbers() {
  ll result = 0;
  for (int i = 9; i >= 0; i--) {
    if (visited[i]) {
      result *= 10;
      result += i;
    }
  }

  return result;
}
void backtracking(int cur) {
  int num = makeNumbers();
  answers.push_back(num);
  for (int i = cur; i < 10; i++) {
    if (visited[i] == false) {
      visited[i] = true;
      backtracking(i + 1);
      visited[i] = false;
    }
  }
}

ll solve(int n) {
  if (n >= 1023) {
    return -1;
  }
  if (n == 0) {
    return 0;
  }
  backtracking(0);
  sort(answers.begin(), answers.end(), cmp);

  return answers[n + 1];
}

int main() {
  int N = 1022;

  cout << solve(N) << endl;
}