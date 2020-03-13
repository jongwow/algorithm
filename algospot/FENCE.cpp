//
// Created by Jongwoo on 2020-03-12.
//
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;


int solve(vector<int> &f) {
    int ret = 0;
    int height;
    for (int l = 0; l < f.size() - 1; l++) {
        height = f[l];
        for (int r = l; r < f.size(); r++) {
            if (height > f[r])
                height = f[r];
            int width = (r - l + 1);
            ret = max(ret, height * width);
        }
    }
    return ret;
}

int main() {
    freopen("../algospot/algospotInput.txt", "r", stdin);
    int tc;
    cin >> tc;
    while (tc-- > 0) {
        vector<int> fence;
        int n;
        int tmp;
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> tmp;
            fence.push_back(tmp);
        }
        cout << solve(fence) << endl;
    }
    return 0;
}
