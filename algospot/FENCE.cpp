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

int mySolveCross(vector<int> &f, int l, int r, int mid) {
    // mid에서 시작해서 왼쪽으로 -1씩, 오른쪽으로 +1씩 하면서 값을 계산해나가면서 가장 큰 값을 저장해놓는 친구.
//    if (l == r) return f[l] * 1;
    int left = mid;
    int right = mid + 1;
    int height = min(f[left], f[right]);
    int width = 2;
    int ret = -1;
    while (l < left || right < r) {
        if (right < r && (left == l || f[left - 1] < f[right + 1])) {
            right++;
            height = min(height, f[right]);
        } else {
            left--;
            height = min(height, f[left]);
        }
        width = right - left + 1;
        ret = max(ret, height * width);
    }
    return ret;
}

// l이상 r미만 == [l, r)
int mySolve(vector<int> &f, int l, int r) {
    if (l == r)
        return f[l] * 1;
    int mid = (l + r) / 2;
    int leftVal = mySolve(f, l, mid);
    int rightVal = mySolve(f, mid + 1, r);
    int midVal = mySolveCross(f, l, r, mid);
    int ret = -1;
    ret = max(leftVal, ret);
    ret = max(rightVal, ret);
    ret = max(midVal, ret);
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
        cout << mySolve(fence, 0, n - 1) << endl;
//        cout << solve(fence) << endl;
    }
    return 0;
}
