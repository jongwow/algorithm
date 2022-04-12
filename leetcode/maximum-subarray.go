package main

import "fmt"

const MaxUint = ^uint(0)
const MinUint = 0
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1

func maxSubArray(nums []int) int {
	// 부분합?
	// 분할정복?
	low, high, sum := findMaximumSubarray(nums, 0, len(nums)-1)
	fmt.Println("low: ", low, ", high: ", high)
	// method 1. 분할정복.
	// 1.1 edge case. pivot 이 중간에 있으면?
	// 1.2 left
	// 1.3 right
	return sum
}

func findMaxCrossingSubarray(arr []int, low, mid, high int) (int, int, int) {
	fmt.Println("findMaxCrossingSubarray: ", low, mid, high)
	leftSum := MinInt
	sum := 0
	maxLeft := 0
	for i := mid; i >= low; i-- {
		sum = sum + arr[i]
		if sum > leftSum {
			leftSum = sum
			maxLeft = i
		}
	}
	if leftSum == MinInt {
		leftSum = 0
	}
	rightSum := MinInt
	sum = 0
	maxRight := 0
	for j := mid + 1; j <= high; j++ {
		sum = sum + arr[j]
		if sum > rightSum {
			rightSum = sum
			maxRight = j
		}
	}
	if rightSum == MinInt {
		rightSum = 0
	}
	return maxLeft, maxRight, leftSum + rightSum
}

func findMaximumSubarray(arr []int, low, high int) (int, int, int) {
	fmt.Println("findMaximumSubarray: ", low, high)
	if high == low {
		return low, high, arr[low]
	} else {
		mid := (low + high) / 2
		leftLow, leftHigh, leftSum := findMaximumSubarray(arr, low, mid)
		rightLow, rightHigh, rightSum := findMaximumSubarray(arr, mid+1, high)
		crossLow, crossHigh, crossSum := findMaxCrossingSubarray(arr, low, mid, high)
		if leftSum >= rightSum && leftSum >= crossSum {
			return leftLow, leftHigh, leftSum
		} else if rightSum >= leftSum && rightSum >= crossSum {
			return rightLow, rightHigh, rightSum
		} else {
			return crossLow, crossHigh, crossSum
		}
	}
}
func main() {
	nums := []int{
		-2, 1, -3, 4, -1, 2, 1, -5, 4,
	}
	//nums := []int{
	//	5, 4, -1, 7, 8,
	//}
	//nums := []int{
	//	-2, -1,
	//}
	//nums := []int{
	//	1, 2,
	//}
	//nums := []int{
	//	-1, 0, -2,
	//}
	//nums := []int{
	//	8, -19, 5, -4, 20,
	//}
	largestSum := maxSubArray(nums)
	fmt.Println(largestSum)
}
