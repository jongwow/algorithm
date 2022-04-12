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

func inorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	leftValues := inorderTraversal(root.Left)
	middleValue := root.Val
	rightValues := inorderTraversal(root.Right)
	ret := []int{}
	ret = append(ret, leftValues...)
	ret = append(ret, middleValue)
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

	traversal := inorderTraversal(root)
	fmt.Println(traversal)

}
