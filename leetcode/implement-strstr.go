package main

import "fmt"

func strStr(haystack string, needle string) int {
	needleHead := needle[0]
	for i := 0; i < len(haystack)-len(needle)+1; i++ {
		cur := haystack[i]
		if needleHead == cur {
			flag := true
			for j := 0; j < len(needle); j++ {
				if haystack[i+j] != needle[j] {
					flag = false
					break
				}
			}
			if flag {
				return i
			}
		}
	}
	return -1
}
func main() {
	fmt.Println(strStr("hello", "ll"))
	fmt.Println(strStr("aaaaa", "bba"))
	fmt.Println(strStr("a", "a"))
}

// com
// 시작위치부터 needle끝까지
// - 문자를 비교해서
// - 같으면 다음 위치로
// - 다르면 return
