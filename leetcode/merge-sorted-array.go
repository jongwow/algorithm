package main

import "fmt"

func merge2(nums1 []int, m int, nums2 []int, n int) {
	left := 0
	right := 0
	for left < m+n && right < n {
		fmt.Println(nums1)
		fmt.Println(nums2)
		fmt.Println(left, right)
		if nums1[left] > nums2[right] {
			nums1[left], nums2[right] = nums2[right], nums1[left]
		} else if nums1[left] == 0 {
			break
		} else {
			left++
		}
	}
	fmt.Println("===========")
	fmt.Println(nums1)
	fmt.Println(left, right)

	for left < m+n && right < n {
		nums1[left] = nums2[right]
		right += 1
		left += 1
	}

	fmt.Println(nums1)
}

func merge3(nums1 []int, m int, nums2 []int, n int) {
	ret := make([]int, n+m)
	idx := 0
	left := 0
	right := 0
	for idx < n+m {
		if right < n && left < m {
			if nums1[left] < nums2[right] {
				ret[idx] = nums1[left]
				left++
			} else {
				ret[idx] = nums2[right]
				right++
			}
		} else if right < n { // left == m
			ret[idx] = nums2[right]
			right++
		} else { // right == n
			ret[idx] = nums1[left]
			left++
		}
		idx++
	}
}

func merge(nums1 []int, m int, nums2 []int, n int) {
	nums11 := make([]int, m)
	for i := 0; i < m; i++ {
		nums11[i] = nums1[i]
	}
	idx := 0
	left := 0
	right := 0
	for idx < n+m {
		if right < n && left < m {
			if nums11[left] < nums2[right] {
				nums1[idx] = nums11[left]
				left++
			} else {
				nums1[idx] = nums2[right]
				right++
			}
		} else if right < n { // left == m
			nums1[idx] = nums2[right]
			right++
		} else { // right == n
			nums1[idx] = nums11[left]
			left++
		}
		idx++
	}
}

/*
4와 1을 비교

[4 5 6 0 0 0]
[1 2 3]

[1 5 6 0 0 0]
[4 2 3]

[1 4 6 0 0 0]
[5 2 3]

[1 4 5 0 0 0]
[6 2 3]

[1 4 5 6 0 0]
[0 2 3]
*/

func main() {
	nums1 := []int{1, 2, 3, 0, 0, 0}
	m := 3
	nums2 := []int{2, 5, 6}
	n := 3

	//nums1 := []int{1}
	//m := 1
	//nums2 := []int{}
	//n := 0
	//
	//nums1 := []int{0}
	//m := 0
	//nums2 := []int{1}
	//n := 1

	//nums1 := []int{4, 5, 6, 0, 0, 0}
	//m := 3
	//nums2 := []int{1, 2, 3}
	//n := 3

	merge(nums1, m, nums2, n)
}

func merge1(nums1 []int, m int, nums2 []int, n int) {
	left := 0
	right := 0
	for left+right < m+n && nums1[left] != 0 {
		if nums1[left] > nums2[right] {
			swap := nums1[left]
			nums1[left] = nums2[right]
			nums2[right] = swap
			right++
		} else {
			left++
		}
	}
	for left < m+n {
		nums1[left] = nums2[right-1]
		right += 1
		left += 1
	}

}
