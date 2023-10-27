#include <iostream>

using namespace std;

int number = 15;

typedef struct node *nodePointer;
typedef struct node {
  int data;
  nodePointer left, right;
} node;

// 전위탐색, preorder
// - 현재 Node의 값 조회
// - 왼쪽 Node를 전위탐색
// - 오른쪽 Node를 전위탐색
void preOrder(nodePointer np) {
  if (np) {
    cout << np->data << "  ";
    preOrder(np->left);
    preOrder(np->right);
  }
}

// 중위탐색, inorder
// - 왼쪽 Node를 중위탐색
// - 현재 Node의 값 조회
// - 오른쪽 Node를 중위탐색
void inOrder(nodePointer np) {
  if (np) {
    inOrder(np->left);
    cout << np->data << "  ";
    inOrder(np->right);
  }
}

// 후위탐색, postorder
// - 왼쪽 Node를 후위탐색
// - 오른쪽 Node를 후위탐색
// - 현재 Node의 값 조회
void postOrder(nodePointer np) {
  if (np) {
    postOrder(np->left);
    postOrder(np->right);
    cout << np->data << "  ";
  }
}
int main() {
  node nodes[number + 1];
  for (int i = 1; i <= number; i++) {
    nodes[i].data = i;
    nodes[i].left = NULL;
    nodes[i].right = NULL;
  }

  for (int i = 2; i <= number; i++) {
    if (i % 2 == 0) {
      nodes[i / 2].left = &nodes[i];
    } else {
      nodes[i / 2].right = &nodes[i];
    }
  }

  preOrder(&nodes[1]);
  cout << endl;
  inOrder(&nodes[1]);
  cout << endl;
  postOrder(&nodes[1]);
  cout << endl;
  return 0;
}
// 참고:
// - https://hongku.tistory.com/160
// -
// https://velog.io/@rubyy/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%9D%B4%EC%A7%84%ED%8A%B8%EB%A6%AC%EC%88%9C%ED%9A%8C-Inorder-Preorder-Postorder