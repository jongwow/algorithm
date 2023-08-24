package main

func minSubArrayLen(target int, nums []int) int {
	opts := len(nums) + 1
	sum := 0
	left := 0
	right := 0
	for right = 0; right < len(nums); right++ {
		sum += nums[right]
		for sum >= target {
			if right-left+1 < opts {
				opts = right - left + 1
			}
			sum -= nums[left]
			left += 1
		}
	}
	if opts == len(nums)+1 {
		return 0
	}
	return opts
}
func tc1() {

	numbers := []int{
		2, 3, 1, 2, 4, 3,
	}
	sol := minSubArrayLen(7, numbers)
	println(sol)
}
func tc2() {

	numbers := []int{
		1, 4, 4}
	sol := minSubArrayLen(4, numbers)
	println(sol)
}
func tc3() {

	numbers := []int{
		1, 1, 1, 1, 1, 1, 1, 1,
	}
	sol := minSubArrayLen(11, numbers)
	println(sol)
}

func tc4() {

	numbers := []int{
		1, 2, 3, 4, 5,
	}
	sol := minSubArrayLen(11, numbers)
	println(sol)
}
func main() {
	tc1()
	tc2()
	tc3()
	tc4()
}
