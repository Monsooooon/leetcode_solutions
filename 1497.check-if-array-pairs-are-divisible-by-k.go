/*
 * @lc app=leetcode.cn id=5449 lang=golang
 *
 * [5449] 检查数组对是否可以被 k 整除
 *
 * https://leetcode-cn.com/problems/check-if-array-pairs-are-divisible-by-k/description/
 *
 * algorithms
 * Medium (35.52%)
 * Likes:    5
 * Dislikes: 0
 * Total Accepted:    1.5K
 * Total Submissions: 4.1K
 * Testcase Example:  '[1,2,3,4,5,10,6,7,8,9]\n5'
 *
 * 给你一个整数数组 arr 和一个整数 k ，其中数组长度是偶数，值为 n 。
 * 
 * 现在需要把数组恰好分成 n / 2 对，以使每对数字的和都能够被 k 整除。
 * 
 * 如果存在这样的分法，请返回 True ；否则，返回 False 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：arr = [1,2,3,4,5,10,6,7,8,9], k = 5
 * 输出：true
 * 解释：划分后的数字对为 (1,9),(2,8),(3,7),(4,6) 以及 (5,10) 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：arr = [1,2,3,4,5,6], k = 7
 * 输出：true
 * 解释：划分后的数字对为 (1,6),(2,5) 以及 (3,4) 。
 * 
 * 
 * 示例 3：
 * 
 * 输入：arr = [1,2,3,4,5,6], k = 10
 * 输出：false
 * 解释：无法在将数组中的数字分为三对的同时满足每对数字和能够被 10 整除的条件。
 * 
 * 
 * 示例 4：
 * 
 * 输入：arr = [-10,10], k = 2
 * 输出：true
 * 
 * 
 * 示例 5：
 * 
 * 输入：arr = [-1,1,-2,2,-3,3,-4,4], k = 3
 * 输出：true
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * arr.length == n
 * 1 <= n <= 10^5
 * n 为偶数
 * -10^9 <= arr[i] <= 10^9
 * 1 <= k <= 10^5
 * 
 * 
 */

 /*
先排序？
回溯：避免重复：状态记录，防止重复
重新映射每一个元素，使其在 [0, k-1]的区间上

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

