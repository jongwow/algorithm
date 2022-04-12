package main

import "fmt"

func removeDuplicates(nums []int) int {
	// 그냥 loop 돌면서 한다면?
	// index slw, fst,
	// slw는 중복제거된 애들.
	// fst는 비교할 애들
	slw := 0
	fst := 1
	if len(nums) == 1 {
		return 1
	}
	if len(nums) == 2 {
		if nums[slw] == nums[fst] {
			return 1
		} else {
			return 2
		}
	}
	for fst != len(nums) {
		i0, i1 := nums[slw], nums[fst]
		if i0 == i1 {
			fst++
		} else {
			slw += 1
			nums[slw] = nums[fst]
		}
	}
	return slw + 1
}
func main() {
	fmt.Println(removeDuplicates([]int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}))
	fmt.Println(removeDuplicates([]int{1, 1, 2}))
}
