package main

import "fmt"

func plusOne(digits []int) []int {
	digits[len(digits)-1] += 1
	for i := len(digits) - 1; i > 0; i-- {
		if digits[i] > 9 {
			digits[i-1]++
			digits[i] = 0
		}
	}
	if digits[0] > 9 {
		digits = append([]int{1, 0}, digits[1:]...)
	}
	return digits
}
func main() {
	digits := plusOne([]int{1, 2, 3})
	//digits := plusOne([]int{9})
	fmt.Println(digits)

}
