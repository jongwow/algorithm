#include <iostream>
#include <vector>
#define MIN_HEAP 0
#define MAX_HEAP 1

// [17, 13, 6, 1, 4, 2, 5]

struct Heap {
  int *array;
  int count;     // 힙 안의 항목 개수
  int capacity;  // 힙의 용량
  int heap_type;  // 최소 힙인지, 최대 힙인지. 0 이라면 최소, 1 이라면 최대
};

struct Heap *CreateHeap(int capacity, int heap_type) {
  struct Heap *h = (struct Heap *)malloc(sizeof(struct Heap));
  if (h == NULL) {
    printf("Memory Error");
    exit(1);
    return NULL;
  }
  h->heap_type = heap_type;
  h->count = 0;
  h->capacity = capacity;
  h->array = (int *)malloc(sizeof(int) * h->capacity);
  if (h->array == NULL) {
    printf("Memory Error");
    exit(1);
    return NULL;
  }
  return h;
}

int Parent(struct Heap *h, int i) {
  if (i <= 0 || i >= h->count) {  // 배열 밖을 벗어나게 된다면
    return -1;
  }
  return (i - 1) / 2;
}

int LeftChild(struct Heap *h, int i) {
  int left = 2 * i + 1;
  if (left >= h->count) {
    return -1;
  }
  return left;
}
int RightChild(struct Heap *h, int i) {
  int right = 2 * i + 2;
  if (right >= h->count) {
    return -1;
  }
  return right;
}
int GetMaximum(Heap *h) {
  if (h->count == 0) return -1;
  return h->array[0];
}

int main() {
  printf("Hello World\n");
  return 0;
}