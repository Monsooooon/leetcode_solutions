/*
 * @lc app=leetcode id=287 lang=golang
 *
 * [287] Find the Duplicate Number
 *
 * https://leetcode.com/problems/find-the-duplicate-number/description/
 *
 * algorithms
 * Medium (50.04%)
 * Likes:    4566
 * Dislikes: 558
 * Total Accepted:    332.4K
 * Total Submissions: 607.5K
 * Testcase Example:  '[1,3,4,2,2]'
 *
 * Given an array nums containing n + 1 integers where each integer is between
 * 1 and n (inclusive), prove that at least one duplicate number must exist.
 * Assume that there is only one duplicate number, find the duplicate one.
 * 
 * Example 1:
 * 
 * 
 * Input: [1,3,4,2,2]
 * Output: 2
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [3,1,3,4,2]
 * Output: 3
 * 
 * Note:
 * 
 * 
 * You must not modify the array (assume the array is read only).
 * You must use only constant, O(1) extra space.
 * Your runtime complexity should be less than O(n^2).
 * There is only one duplicate number in the array, but it could be repeated
 * more than once.
 * 
 * 
 */

// 为什么通过第一个位置的数字中的跳转一定可以找到环
// 这是因为数组中下标的范围是 0 ~ N
// 而数组中所有数的范围是 1 ~ N
// 1. 从下标0开始跳，能否跳回到0呢？不能，因为数组中所有数都是大于0的
// 2. 从下标0开始跳，能否一定遇到环呢？能，因为我们始终是在数组内 1 ~ N 的范围跳动，没有离开 
// 	  因为不可能无限制地跳，所以一定会遇到环。
// 3. 如果条件改为下标范围是（0 ~ N-1)，情况会怎样
// 	  可能出现无重复的链路，比如数组的值是[1 3 2 4 5]，0 -> 1 -> 3 -> 4 -> 5，不能再跳，结束
// 	  可能出现重复的链路，比如如数组的值是[1 2 3 1 5], 0 -> 1 -> 2 -> 3 -> 1，出现重复

// @lc code=start
func findDuplicate(nums []int) int {
	fast, slow := nums[nums[0]], nums[0]
	for fast != slow {
		fast = nums[nums[fast]]
		slow = nums[slow]
	}
	fast = 0
	for fast != slow {
		fast = nums[fast]
		slow = nums[slow]
	}
	return slow
}
// @lc code=end

