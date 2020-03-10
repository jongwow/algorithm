#include <string>
#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

string nums = "0123456789";
string onebyone(string origin, int n) {
	if (n == 0) origin = "1" + origin;
	else{
		char ch = origin[n-1];
		if (ch == '1') {
			origin[n-1] = '2';
		}
		else if (ch == '2') {
			origin[n-1] = '4';
		}
		else { // ch == 4
			origin[n-1] = '1';
			origin = onebyone(origin, n - 1);
		}
	}
	return origin;
}

string solution(int n) {
	string answer = "";
	for (int i = 0; i < n; i++) {
		answer = onebyone(answer, answer.length() - 1);
	}
	return answer;
}

string tri(int n) {
	string str = "";
	while (n >0) {
		str += nums[n % 3];
		n /= 3;
	}
	reverse(str.begin(), str.end());
	return str;
}

string proc(string origin,int n) {
	if(origin[n] == '0'){
		origin = proc(origin, n - 1);
		origin[n] = '3';
	}
	else if (origin[n] == '1') {
		origin[n] = '0';
	}
	else if (origin[n] == '2') {
		origin[n] = '1';
	}
//	cout << "PROC: " << origin << endl;
	return origin;
}
string proc2(string origin) {
	for (int i = 0; i < origin.length(); i++) {
		if (origin[i] == '3') origin[i] = '2';
	}
	return origin;
}
int main() {
	int N;
	string answer = "";
	cin >> N;
	answer = tri(N);
//	cout << answer<< endl;
	for (int i = answer.length()-1; i >0; i--) {
		if (answer[i] == '0') {
			answer = proc(answer, i);
			answer[i] = '4';
//			cout << answer << endl;
		}
	}
//	cout << answer << endl;
	answer = proc2(answer);
	if (answer[0] == '0')
		answer = answer.substr(1, answer.length());
	cout << answer << endl;
	return 0;
}