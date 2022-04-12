package main

import "fmt"

func isValid(s string) bool {
	// cur 문자 읽어서
	// - left면 Left 스택에 넣음.
	// - right면 left 스택에서 Pop한게 matching 확인.
	// - loop
	myStack := stack{values: []rune{}}
	for _, c := range s {
		if isLeft(c) {
			myStack.push(c)
			continue
		}
		if myStack.isEmpty() {
			return false
		} else if isMatching(myStack.peek(), c) {
			myStack.pop()
		} else {
			return false
		}
	}
	return myStack.len() == 0
}

type stack struct {
	values []rune
}

func (s *stack) push(ch rune) {
	s.values = append(s.values, ch)
}
func (s *stack) pop() rune {
	ret := s.values[len(s.values)-1]
	s.values = s.values[:len(s.values)-1]
	return ret
}
func (s *stack) peek() rune {
	return s.values[len(s.values)-1]
}
func (s *stack) len() int {
	return len(s.values)
}
func (s *stack) isEmpty() bool {
	return len(s.values) == 0
}

func isLeft(c rune) bool {
	return c == rune('(') || c == rune('[') || c == rune('{')
}
func isMatching(left, right rune) bool {
	if left == rune('(') {
		return right == rune(')')
	}
	if left == rune('{') {
		return right == rune('}')
	}
	if left == rune('[') {
		return right == rune(']')
	}
	return false
}

func main() {
	fmt.Println(isValid("(])"))
}
