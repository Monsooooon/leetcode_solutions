/*
 * @lc app=leetcode id=1497 lang=golang
 *
 * [1497] Check If Array Pairs Are Divisible by k
 *
 * https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/
 *
 * algorithms
 * Medium (38.79%)
 * Likes:    32
 * Dislikes: 5
 * Total Accepted:    3.6K
 * Total Submissions: 9.2K
 * Testcase Example:  '[1,2,3,4,5,10,6,7,8,9]\n5'
 *
 * Given an array of integers arr of even length n and an integer k.
 * 
 * We want to divide the array into exactly n / 2 pairs such that the sum of
 * each pair is divisible by k.
 * 
 * Return True If you can find a way to do that or False otherwise.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
 * Output: true
 * Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: arr = [1,2,3,4,5,6], k = 7
 * Output: true
 * Explanation: Pairs are (1,6),(2,5) and(3,4).
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: arr = [1,2,3,4,5,6], k = 10
 * Output: false
 * Explanation: You can try all possible pairs to see that there is no way to
 * divide arr into 3 pairs each with sum divisible by 10.
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: arr = [-10,10], k = 2
 * Output: true
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: arr = [-1,1,-2,2,-3,3,-4,4], k = 3
 * Output: true
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * arr.length == n
 * 1 <= n <= 10^5
 * n is even.
 * -10^9 <= arr[i] <= 10^9
 * 1 <= k <= 10^5
 * 
 */

// @lc code=start
func canArrange(arr []int, k int) bool {
    for i := range arr {
        arr[i] = ((arr[i] % k) + k) % k
    }

    // now every element in arr is in range [0, k-1]
    sort.Ints(arr)

	// we need to deal with preceeding zeros, since they
	// can also form pairs
    i := 0
    for i < len(arr) && arr[i] == 0 {
        if arr[i+1] != 0 {
            return false
        }
        i += 2
    }

	// then for all other mapped num, we check each pair
    for j := len(arr)-1; i < j; i, j = i+1, j-1{
        if arr[i] + arr[j] != k {
            return false
        }
    }

    return true
}
// @lc code=end

