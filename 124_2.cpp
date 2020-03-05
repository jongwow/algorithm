
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

string nums = "0123456789";
string tri(int n) {
	string str = "";
	while (n > 0) {
		str += nums[n % 3];
		n /= 3;
	}

	reverse(str.begin(), str.end());

	return str;
}

string proc(string origin, int n) {
	if (origin[n] == '0') {
		origin = proc(origin, n - 1);
		origin[n] = '3';
	}
	else if (origin[n] == '1') {
		origin[n] = '0';
	}
	else if (origin[n] == '2') {
		origin[n] = '1';
	}
	return origin;
}
string proc2(string origin) {
	for (int i = 0; i < origin.length(); i++) {
		if (origin[i] == '3') origin[i] = '2';
	}
	return origin;
}
string solution2(int n) {
	string answer = "";
	answer = tri(n);
	for (int i = answer.length() - 1; i > 0; i--) {
		if (answer[i] == '0') {
			answer = proc(answer, i);
			answer[i] = '4';
		}
	}
	answer = proc2(answer);
	if (answer[0] == '0')
		answer = answer.substr(1, answer.length());
	return answer;
}


string solution(int n) {
	string answer = "";
	long long curPos = 3; // 10진수
	long long clone = n;
	string otf = "124";

	while (clone > curPos) {
		clone -= curPos;
		curPos *= 3;
	}
	clone = n;

	while (true) {
		cout << "while:" << answer << endl;
		curPos /= 3;

		if (clone <= 3) {
			answer += otf[clone - 1];
			break;
		}

		if (clone <= 12) {
			if (clone > curPos * 3) {
				answer += '4';
				clone -= curPos * 3;
			}
			else if (clone > curPos * 2) {
				answer += '2';
				clone -= curPos * 2;
			}
			else {
				answer += '1';
				clone -= curPos;
			}
			continue;
		}

		if (clone - (curPos * 7 - 1) / 2 >= 0) {
			answer += '4';
			clone -= curPos * 3;
		}
		else if (clone - (curPos * 5 - 1) / 2 >= 0) {
			answer += '2';
			clone -= curPos * 2;
		}
		else if (clone - (curPos * 3 - 1) / 2 >= 0) {
			answer += '1';
			clone -= curPos;
		}
	}

	return answer;
}

int main(int argc, const char* argv[]) {
	// insert code here...

	int n;
	cin >> n;
	cout << solution(n) << endl;
	cout << solution2(n) << endl;
	return 0;
}
