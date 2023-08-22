package main

func removeDuplicates(nums []int) int {
	left := 0
	right := 0
	count := 0
	previous := 1000000
	for right < len(nums) {
		if nums[right] != previous {
			previous = nums[right]
			count = 0
		}
		count += 1
		if count > 2 {
			right++
			continue
		}
		nums[left] = nums[right]
		left++
		right++
	}
	return left
}

func main() {
	tcs := [][]int{
		{1, 1, 1, 2, 2, 3}, {0, 0, 1, 1, 1, 1, 2, 3, 3},
	}
	for _, tc := range tcs {
		removeDuplicates(tc)
	}
}
