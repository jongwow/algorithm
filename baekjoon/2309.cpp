#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int heights[9];
	int sum = 0;
	for (int i = 0; i < 9; i++) {
		cin >> heights[i];
	}
	sort(heights, heights + 9);
	for (int i = 0; i < 8; i++) {
		int tmp = heights[i];
		heights[i] = 0;
		for (int j = i+1; j < 9; j++) {
			int ttmp = heights[j];
			heights[j] = 0;
			for (int idx = 0; idx < 9; idx++) {
				sum += heights[idx];
			}
			if (sum == 100) {
				break;
			}
			sum = 0;
			heights[j] = ttmp;
		}
		if (sum == 100)
			break;
		heights[i] = tmp;
	}
	for (int i = 0; i < 9; i++)
		if (heights[i] != 0)
			cout << heights[i] << endl;
}