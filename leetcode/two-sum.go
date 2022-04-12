package main

import (
	"fmt"
	"sort"
)

type Item struct {
	Value int
	Index int
}

func twoSum(nums []int, target int) []int {
	nNums := make([]Item, len(nums))
	for i := 0; i < len(nNums); i++ {
		nNums[i].Value = nums[i] - target
		nNums[i].Index = i
	}

	sort.Slice(nNums, func(i, j int) bool {
		return nNums[i].Value < nNums[j].Value
	})

	//fmt.Println(nNums)

	leftIdx := 0
	rightIdx := len(nNums) - 1

	for leftIdx < rightIdx {
		guess := nNums[leftIdx].Value + nNums[rightIdx].Value + target
		fmt.Println(guess, leftIdx, rightIdx)
		if guess == 0 {
			return []int{nNums[leftIdx].Index, nNums[rightIdx].Index}
		}
		if guess < 0 {
			leftIdx++
		} else {
			rightIdx--
		}
	}
	return []int{nNums[leftIdx].Index, nNums[rightIdx].Index}
}

func twoSum1(nNums []int, target int) []int {
	sort.Slice(nNums, func(i, j int) bool {
		return nNums[i] < nNums[j]
	})
	fmt.Println(nNums)

	leftIdx := 0
	rightIdx := len(nNums) - 1

	for leftIdx < rightIdx {
		guess := nNums[leftIdx] + nNums[rightIdx]
		fmt.Println(guess, leftIdx, rightIdx)
		guess = guess - target
		if guess == 0 {
			return []int{leftIdx, rightIdx}
		}
		if guess < 0 {
			leftIdx++
		} else {
			rightIdx--
		}
	}
	return []int{leftIdx, rightIdx}
}

func abs(n int) int {
	if n >= 0 {
		return n
	} else {
		return -n
	}
}
