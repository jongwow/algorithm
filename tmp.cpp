#include <iostream>
#include <string>
using namespace std;

string solution(string number, int k) {
	string answer = "";
	answer = number.substr(k);
	for (int i = k - 1; i >= 0; i--) {
		int j = 0;
		do {
			cout << "N: " << number << endl;
			cout << "A: " << answer << endl;
			cout << "i: " << i << ", j: " << j << endl;
			if (number[i] >= answer[j]) {
				char temp = answer[j];
				answer[j] = number[i];
				number[i] = temp;
				j++;
			}
			else {
				break;
			}
		} while (1);
	}

	return answer;
}


int main() {
	string inputStr;
	int inputK;

	cin >> inputStr;
	cin >> inputK;
	//1231234		3	3234
	//inputStr = "4177252841";
	//inputK = 4;
	cout << "===========" << endl;
	cout << inputStr.length() << endl;
	cout << solution(inputStr, inputK) << endl;
	return 0;
}

