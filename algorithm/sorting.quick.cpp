#include <algorithm>
#include <iostream>
using namespace std;

int Partition(int A[], int low, int high) {
  int left, right, pivot_item = A[low];
  left = low;
  right = high;
  while (left < right) {
    while (A[left] <= pivot_item) {
      left++;
    }
    while (A[right] > pivot_item) {
      right--;
    }
    if (left < right) {
      swap(A[left], A[right]);
    }
  }
  A[low] = A[right];
  A[right] = pivot_item;
  return right;
}

void QuickSort(int A[], int low, int high) {
  int pivot;
  // 종료 조건
  if (high > low) {
    pivot = Partition(A, low, high);
    QuickSort(A, low, pivot - 1);
    QuickSort(A, pivot + 1, high);
  }
}

int main() {
  int a[10] = {1, 6, 5, 8, 4, 10, 2, 7, 3, 9};
  int sizeOfA = (sizeof(a) / sizeof(*a));
  QuickSort(a, 0, sizeOfA - 1);
  for (size_t i = 0; i < sizeOfA; i++) {
    cout << a[i] << " ";
  }
  cout << endl;
}