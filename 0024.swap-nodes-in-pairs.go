/*
 * @lc app=leetcode id=24 lang=golang
 *
 * [24] Swap Nodes in Pairs
 *
 * https://leetcode.com/problems/swap-nodes-in-pairs/description/
 *
 * algorithms
 * Medium (45.21%)
 * Likes:    2192
 * Dislikes: 167
 * Total Accepted:    462.7K
 * Total Submissions: 929K
 * Testcase Example:  '[1,2,3,4]'
 *
 * Given a linked list, swap every two adjacent nodes and return its head.
 * 
 * You may not modify the values in the list's nodes, only nodes itself may be
 * changed.
 * 
 * 
 * 
 * Example:
 * 
 * 
 * Given 1->2->3->4, you should return the list as 2->1->4->3.

 2 1 3 4
 * 
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {
	dummyHead := ListNode {
		Val: 	1,
		Next: head,
	}
	var prev, mid1, mid2, next *ListNode
	mid1 = &dummyHead // for initializing 'prev'
	for {
		prev = mid1
		mid1 = prev.Next
		if mid1 == nil {
			break;
		}
		mid2 = mid1.Next
		if mid2 == nil {
			break
		}
		next = mid2.Next

		// swap
		prev.Next = mid2
		mid2.Next = mid1
		mid1.Next = next
	}
	return dummyHead.Next
}
// @lc code=end

