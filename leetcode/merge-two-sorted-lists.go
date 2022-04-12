package main

import (
	"fmt"
	"strconv"
)

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func push(head *ListNode, val int) {
	cur := head
	for cur != nil {
		cur = cur.Next
	}
	cur = &ListNode{Val: val, Next: nil}
}

func mergeTwoListCopy(list1 *ListNode, list2 *ListNode) *ListNode {
	var dummy *ListNode
	var temp *ListNode
	dummy = &ListNode{}
	temp = dummy

	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			temp.Next = list1
			list1 = list1.Next
		} else {
			temp.Next = list2
			list2 = list2.Next
		}
		temp = temp.Next
	}
	if list1 != nil {
		temp.Next = list1
	}
	if list2 != nil {
		temp.Next = list2
	}
	return dummy.Next
}

func mergeTwoListsNew(list1 *ListNode, list2 *ListNode) *ListNode {
	var ptr *ListNode
	var head *ListNode
	if list1 == nil && list2 == nil {
		return head
	}

	for list1 != nil && list2 != nil {
		var val int
		if list1.Val < list2.Val {
			val = list1.Val
			list1 = list1.Next
		} else {
			val = list2.Val
			list2 = list2.Next
		}
		if head == nil {
			head = &ListNode{Val: val, Next: nil}
			ptr = head
			continue
		}
		ptr.Next = &ListNode{Val: val, Next: nil}
		ptr = ptr.Next
	}

	for list1 != nil {
		val := list1.Val
		list1 = list1.Next
		if head == nil {
			head = &ListNode{Val: val, Next: nil}
			ptr = head
			continue
		}
		ptr.Next = &ListNode{Val: val, Next: nil}
		ptr = ptr.Next
	}
	for list2 != nil {
		val := list2.Val
		list2 = list2.Next
		if head == nil {
			head = &ListNode{Val: val, Next: nil}
			ptr = head
			continue
		}
		ptr.Next = &ListNode{Val: val, Next: nil}
		ptr = ptr.Next
	}

	return head
}

func mockListNode(a ...int) *ListNode {
	var ptr *ListNode
	var head *ListNode
	for _, val := range a {
		if head == nil {
			head = &ListNode{Val: val, Next: nil}
			ptr = head
			continue
		}
		ptr.Next = &ListNode{Val: val, Next: nil}
		ptr = ptr.Next
	}
	return head
}
func mockListNodeV2(a ...int) *ListNode {
	var ptr *ListNode
	var head *ListNode
	for _, val := range a {
		if head == nil {
			head = &ListNode{Val: val, Next: nil}
			ptr = head
			continue
		}
		ptr.Next = &ListNode{Val: val, Next: nil}
		ptr = ptr.Next
	}
	return head
}

func mockListNode4(a, b, c, d int) *ListNode {
	step1 := &ListNode{Val: a, Next: nil}

	step2 := &ListNode{Val: b, Next: nil}
	step1.Next = step2

	step3 := &ListNode{Val: c, Next: nil}
	step2.Next = step3

	step4 := &ListNode{Val: d, Next: nil}
	step3.Next = step4

	return step1
	//return &ListNode{Val: a, Next: &ListNode{Val: b, Next: &ListNode{Val: c}}}
}

func mockListNode3(a, b, c int) *ListNode {
	step1 := &ListNode{Val: a, Next: nil}

	step2 := &ListNode{Val: b, Next: nil}
	step1.Next = step2

	step3 := &ListNode{Val: c, Next: nil}
	step2.Next = step3
	return step1
	//return &ListNode{Val: a, Next: &ListNode{Val: b, Next: &ListNode{Val: c}}}
}
func mockListNode2(a, b int) *ListNode {
	return &ListNode{Val: a, Next: &ListNode{Val: b, Next: nil}}
}

func printListNode(node *ListNode) {
	ret := ""
	for node != nil {
		n := strconv.Itoa(node.Val)
		ret += n + " "
		node = node.Next
	}
	fmt.Println(ret)
}

func mergeTwoLists3(list1 *ListNode, list2 *ListNode) *ListNode {
	var ret *ListNode
	str := ret
	//for list1 != nil && list2 != nil {
	//	if list1.Val < list2.Val {
	//		list1 = list1.Next
	//	} else {
	//		list1
	//	}
	//}
	return str
}

func mergeTwoLists2(list1 *ListNode, list2 *ListNode) *ListNode {
	var ret *ListNode
	str := ret
	for list1 != nil && list2 != nil {
		//fmt.Println(list1.Val, list2.Val)
		if list1.Val < list2.Val {
			ret = list1
			list1 = list1.Next
		} else {
			ret = list2
			list2 = list2.Next
		}
		ret = ret.Next
	}
	for list1 != nil {
		ret = list1
		list1 = list1.Next
		ret = ret.Next
	}
	for list2 != nil {
		ret = list2
		list2 = list2.Next
		ret = ret.Next
	}
	return str
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	var cur *ListNode
	ret := cur
	for list1 != nil && list2 != nil {
		cur = &ListNode{}
		if ret == nil {
			fmt.Println("1")
			ret = cur
		}
		if list1.Val < list2.Val {
			cur.Val = list1.Val
			list1 = list1.Next
		} else {
			cur.Val = list2.Val
			list2 = list2.Next
		}
		cur = cur.Next
	}
	// for list1 과 list2가 둘 중 하나가 끝?
	// - list1과 list2 중 더 작은걸 넣는다.
	// - list1과 list2 중 넣은 걸 다음거로 옮긴다.

	// 끝이 남아있는 경우, 그 끝까지 넘긴다.
	if list1 != nil {
		for list1 != nil {
			cur = &ListNode{}
			if ret == nil {
				fmt.Println("2")
				ret = cur
			}

			cur.Val = list1.Val
			list1 = list1.Next
			cur = cur.Next
		}
	} else if list2 != nil {
		for list2 != nil {
			cur = &ListNode{}
			if ret == nil {
				fmt.Println("3")

				ret = cur
			}

			cur.Val = list2.Val
			list2 = list2.Next
			cur = cur.Next
		}
	}

	return ret
}

//func main() {
//list1 := mergeTwoLists(nil, nil)
//list1 := mergeTwoLists(mockListNode(1, 2, 4), mockListNode(1, 3, 4))
//list1 := mergeTwoListCopy(mockListNode(-9, 3), mockListNode(5, 7))
//printListNode(list1)
//}

//[-9, 3]
//[5, 7]
