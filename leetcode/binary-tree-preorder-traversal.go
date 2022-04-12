package main

import "fmt"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func preorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	leftValues := preorderTraversal(root.Left)
	rightValues := preorderTraversal(root.Right)
	middleValue := root.Val
	ret := []int{}
	ret = append(ret, middleValue)
	ret = append(ret, leftValues...)
	ret = append(ret, rightValues...)
	return ret

}
func main() {
	root := &TreeNode{
		Val:  1,
		Left: nil,
		Right: &TreeNode{
			Val:   2,
			Left:  &TreeNode{Val: 3, Left: nil, Right: nil},
			Right: nil,
		},
	}

	traversal := preorderTraversal(root)
	fmt.Println(traversal)

}
