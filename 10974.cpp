#include <iostream>
using namespace std;

int next_permu(int* arr,int arrSize) {
	//뒤에서부터 오름차순인 부분까지 찾는다.
	int idx = -1;
	for (int i = arrSize - 1; i > 0; i--) {
		if (arr[i] > arr[i - 1]){
			idx = i - 1;
			break;
		}
	}
	if (idx == -1){
		return -1;
	}
	else {
		int j = idx + 1;
		for (; j < arrSize; j++)
			if (arr[idx] > arr[j])
				break;
		j -= 1;
		//swap하기
		swap(arr[idx], arr[j]);
		//순서 거꾸로
		for (int i = idx + 1; i <= (arrSize + idx) / 2; i++) {
			swap(arr[i], arr[arrSize - i + idx]);
		}
		for (int i = 0; i < arrSize; i++)
			cout << arr[i] << " ";
		cout << "\n";
		return 1;
	}
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int N;
	int A[9];
	cin >> N;
	for (int i = 0; i < N; i++) {
		A[i] = i+1;
	}

	for (int i = 0; i < N; i++)
		cout << A[i] << " ";
	cout << "\n";
	while (1) {
		if (next_permu(A, N) == 1)
			continue;
		else
			break;
	}
	return 0;
}

//배운 점 : ios::base랑 endl은 flush를 해서 엄청 느리다는 것.