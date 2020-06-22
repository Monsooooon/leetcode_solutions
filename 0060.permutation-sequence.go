/*
 * @lc app=leetcode id=60 lang=golang
 *
 * [60] Permutation Sequence
 *
 * https://leetcode.com/problems/permutation-sequence/description/
 *
 * algorithms
 * Medium (33.40%)
 * Likes:    1613
 * Dislikes: 328
 * Total Accepted:    197.9K
 * Total Submissions: 521.3K
 * Testcase Example:  '3\n3'
 *
 * The set [1,2,3,...,n] contains a total of n! unique permutations.
 *
 * By listing and labeling all of the permutations in order, we get the
 * following sequence for n = 3:
 *
 *
 * "123"
 * "132"
 * "213"
 * "231"
 * "312"
 * "321"
 *
 *
 * Given n and k, return the k^th permutation sequence.
 *
 * Note:
 *
 *
 * Given n will be between 1 and 9 inclusive.
 * Given k will be between 1 and n! inclusive.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 3, k = 3
 * Output: "213"
 *
 *
 * Example 2:
 *
 *
 * Input: n = 4, k = 9
 * Output: "2314"
 *
 *
 */

// @lc code=start
/*
it is not corrcet to generate all permutations
instead, we can
*/
package main

func getPermutation(n int, k int) string {

	factorial := 1
	nums := []int{}

	for i := 1; i <= n; i++ {
		factorial *= i
		nums = append(nums, i)
	}

	k--
	var result []rune
	for i := n; i >= 1; i-- {
		factorial /= i
		// order means the number to append next is in Nth group.
		order := k / factorial
		result = append(result, rune(getNthFromNums(nums, order+1))+'0')
		k %= factorial
	}
	return string(result)
}

// n should be in range [1, len(nums)]
func getNthFromNums(nums []int, n int) int {
	for i, v := range nums {
		if v != -1 {
			n--
			if n == 0 {
				nums[i] = -1
				return v
			}
		}
	}
	return -1
}

// @lc code=end
