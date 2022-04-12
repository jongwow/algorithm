package main

import "fmt"

func climbStairs(n int) int {
	ret := make([]int, 46)
	ret[0] = 0
	ret[1] = 1
	ret[2] = 2
	for i := 3; i <= n; i++ {
		ret[i] = ret[i-1] + ret[i-2]
	}
	return ret[n]
}

func climbStairs1(n int) int {

	dp := make([]int, 46)
	dp[0] = 0
	dp[1] = 1
	dp[2] = 2

	var looping func(k int) int
	looping = func(k int) int {
		if dp[k] != 0 {
			return dp[k]
		}
		dp[k] = looping(k-1) + looping(k-2)
		return dp[k]
	}
	ret := looping(n)
	return ret
}
func main() {
	fmt.Println(climbStairs(4))
}
