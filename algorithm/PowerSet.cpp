//
// Created by Jongwoo on 2020-03-10.
//

#include <iostream>
#include <string>

using namespace std;

int n;
string myData = "abcdef";
bool include[6];

void funPowerSet(int k) {
    if (k == n) {
        for (int i = 0; i < n; i++) {
            if (include[i]) cout << myData[i] << " ";
        }
        cout << endl;
        return;
    }
    // 포함하지 않는 부분
    include[k] = false;
    funPowerSet(k + 1);

    // 포함하는 부분
    include[k] = true;
    funPowerSet(k + 1);
}

int main() {
    n = myData.size();
    funPowerSet(0);
}

