package leetcode

type ListNode struct {
	Val  int
	Next *ListNode
}

func ReverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	var prev *ListNode
	curr := head
	var next_tmp *ListNode

	for curr != nil {
		next_tmp = curr.Next
		curr.Next = prev
		prev = curr
		curr = next_tmp
	}
	return prev
}
