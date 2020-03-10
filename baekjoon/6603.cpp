#include <iostream>
#include <vector>
#define MAX_SIZE 13
using namespace std;
int lotto[MAX_SIZE];
vector<vector<int> > ans;
int k;
void make_lotto(int start, int depth, vector<int> res) {
	if (depth == 6) {
		ans.push_back(res);
		return;
	}
	for (int i = start; i < k; i++) {
		res.push_back(lotto[i]);
		make_lotto(i + 1, depth + 1, res);
		res.pop_back();
	}
	res.clear();
}

int main() {
	while (1) {
		cin >> k;
		if (k == 0)
			break;
		for (int i = 0; i < k; i++) {
			cin >> lotto[i];
		}
		vector<int> res;
		make_lotto(0, 0, res);
		for (int i = 0; i < ans.size(); i++) {
			for (int j = 0; j < 6; j++) {
				cout << ans.at(i).at(j) << " ";
			}
			cout << "\n";
		}
		cout << "\n";
		ans.clear();
	}
	return 0;
}