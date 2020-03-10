//
// Created by Jongwoo on 2020-03-10.
//
#include <iostream>
#include <vector>

using namespace std;
void pick(int, vector<int>&, int);
int main() {
    vector<int> p;
    pick(5, p, 3);
}

void printPicked(vector<int> picked) {
    int pSize = picked.size();
    for (int i = 0; i < pSize; i++) {
        cout << picked[i]+1 << " ";
    }
    cout << endl;
}

// n: 전체 원소의 수
// picked: 지금까지 고른 원소들의 번호
// toPick: 더 고를 원소 수
// 일때, 앞으로 toPick개의 원소를 고르는 모든 방법을 출력한다.
void pick(int n, vector<int> &picked, int toPick) {
    // base Case: 더 고를 원소가 없을 때 고른 원소들을 출력한다.
    if (toPick == 0) {
        printPicked(picked);
        return;
    }
    // 고를 수 있는 가장 작은 번호를 계산한다.
    int smallest = picked.empty() ? 0 : picked.back() + 1;
    // 이 단계에서 원소 하나를 고른다.
    for (int next = smallest; next < n; next++) {
        picked.push_back(next);
        pick(n, picked, toPick - 1);
        picked.pop_back();
    }
}