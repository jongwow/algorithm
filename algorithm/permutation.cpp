#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int varCount = 0;

int duplicated[10] = {
    0,
};

int facto(int num) {
  if (num == 0) return 1;
  int ret = 1;
  for (int i = 1; i <= num; i++) {
    ret *= i;
  }
  return ret;
}

int permutationInt(vector<int>& arr, int start, int end) {
  if (start == end) {
    return 1;
  } else {
    int ret = 0;
    for (int i = start; i <= end; i++) {
      swap(arr[start], arr[i]);
      ret += permutationInt(arr, start + 1, end);
      swap(arr[start], arr[i]);
    }
    return ret;
  }
}

void permutation(vector<int>& arr, int start, int end) {
  if (start == end) {
    for (const auto current : arr) {
      cout << current << " ";
    }
    varCount++;
    cout << endl;
  } else {
    for (int i = start; i <= end; i++) {
      swap(arr[start], arr[i]);
      permutation(arr, start + 1, end);
      swap(arr[start], arr[i]);
    }
  }
  return;
}
int permutationPractice(vector<int>& arr, int start, int end) {
  if (start == end) {
    return 1;
  } else {
    int ret = 0;
    for (int i = start; i <= end; i++) {
      swap(arr[start], arr[i]);
      ret += permutationPractice(arr, start + 1, end);
      swap(arr[start], arr[i]);
    }
    return ret;
  }
}
void permutationForDuplicated(vector<int>& arr, int start, int end) {
  permutation(arr, 0, arr.size() - 1);
}
void counting(vector<int>& arr) {
  for (const auto curr : arr) {
    duplicated[curr]++;
  }
}
int divider() {
  int ret = 1;
  for (const auto curr : duplicated) {
    ret *= facto(curr);
  }
  return ret;
}
int main() {
  vector<int> given = {1, 1, 2, 3};
  counting(given);
  int div = divider();
  int result = permutationInt(given, 0, given.size() - 1);
  cout << result / div << endl;
  return 0;
}