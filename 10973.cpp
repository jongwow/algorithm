#include <iostream>
#include <vector>
using namespace std;

/*
1.증가순열찾기
2.바꿀 숫자 찾기. (증가순열 앞의 숫자)와 (증가순열안에서 처음으로 작은 숫자의  전거)
3.스왑하기
4.거꾸로정렬하기*/
int main() {
	int N;
	int tmp;
	vector<int> perm;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> tmp;
		perm.push_back(tmp);
	}
	//뒤에서부터 오름차순인 부분까지 찾는다.(감소순열찾기)
	int idx = -1;
	for (int i = N - 1; i > 0; i--) {
		if (perm[i] < perm[i - 1]) {
			idx = i - 1;
			break;
		}
	}
	if (idx != -1) {
		//바꿀 숫자 찾기.
		int j = idx + 1;
		for (; j < N; j++)
			if (perm[idx] < perm[j])
				break;
		j -= 1;
		for (int i = 0; i < N; i++)
			cout << perm[i] << " ";
		cout << endl;
		//swap하기
		cout << "j:" << j << endl;
		swap(perm[idx], perm[j]);
		for (int i = 0; i < N; i++)
			cout << perm[i] << " ";
		cout << endl;
		//순서 거꾸로
		for (int i = idx + 1; i <= (N + idx) / 2; i++) {
			swap(perm[i], perm[N - i + idx]);
		}
		for (int i = 0; i < N; i++)
			cout << perm[i] << " ";
		cout << endl;
	}
	else {
		cout << idx << endl;
	}
}