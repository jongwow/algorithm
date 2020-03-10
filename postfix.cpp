//
// main.cpp
// No1224
//
// Created by 정예주 on 02/09/2019.
// Copyright © 2019 정예주. All rights reserved.
//

#include <iostream>
#include <cstdio>
using std::cin;
using std::cout;

#define MAX_STACK_SIZE 10485

int getWeight(char value) {
	if (value == '*') return 2;
	else if (value == '+') return 1;
	else return 0;
}

int main() {
	//freopen("input.txt", "r", stdin);
	// insert code here...
	for (int test_case = 1; test_case <= 10; test_case++) {
		char formula[MAX_STACK_SIZE] = { 0 }; // 후위표기식
		char stack[MAX_STACK_SIZE] = { 0 };
		int top = -1;
		int index = 0;

		int length;
		cin >> length;
		for (int i = 0; i < length; i++) { // 후위표기식으로 만드는 과정
			char input;
			cin >> input;
			if (input - '0' >= 0 && input - '0' <= 9)
				formula[index++] = input;

			else {
				if (input == '(') stack[++top] = input;
				else if (input == ')') {
					while (true) {
						if (stack[top] != '(')
							formula[index++] = stack[top--];
						else {
							top--;
							break;
						}
					}
				}
				else if (getWeight(stack[top]) >= getWeight(input)) {
					formula[index++] = stack[top];
					stack[top] = input;
				}
				else stack[++top] = input;
			}
		}

		while (top > -1) formula[index++] = stack[top--];

		int calculateStack[MAX_STACK_SIZE] = { 0 };
		top = -1;
		for (int i = 0; i < index; i++) {
			char value = formula[i];
			if (value - '0' >= 0 && value - '0' <= 9) {
				calculateStack[++top] = value - '0';
			}
			else {
				int num1 = calculateStack[top--];
				int num2 = calculateStack[top--];
				if (value == '+') calculateStack[++top] = num1 + num2;
				else calculateStack[++top] = num1 * num2;
			}
		}
		cout << "#" << test_case << " " << calculateStack[top] << std::endl;

	}
	return 0;
}