/*
 * @lc app=leetcode id=279 lang=golang
 *
 * [279] Perfect Squares
 *
 * https://leetcode.com/problems/perfect-squares/description/
 *
 * algorithms
 * Medium (42.32%)
 * Likes:    2756
 * Dislikes: 182
 * Total Accepted:    288.4K
 * Total Submissions: 622.9K
 * Testcase Example:  '12'
 *
 * Given a positive integer n, find the least number of perfect square numbers
 * (for example, 1, 4, 9, 16, ...) which sum to n.
 *
 * Example 1:
 *
 *
 * Input: n = 12
 * Output: 3
 * Explanation: 12 = 4 + 4 + 4.
 *
 * Example 2:
 *
 *
 * Input: n = 13
 * Output: 2
 * Explanation: 13 = 4 + 9.
 */

/*
 两种思路：
 第一种是BFS，从0开始搜索，当搜索到n的时候就是最短路径，需要额外记录某个数字是否已经被访问过了
 第二种是dp，dp[n] = 最小的 dp[n-k] + 1)
*/
// @lc code=start

func Min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func numSquares(n int) int {
	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = i
		for j := 1; j*j <= i; j++ {
			dp[i] = Min(dp[i], dp[i-j*j]+1)
		}
	}
	return dp[n]
}

func numSquares_2(n int) int {
	queue := []int{0}
	visited := make(map[int]bool)
	cnt := 0
	for len(queue) != 0 {
		curr_len := len(queue) // number of elements in current level
		for i := 0; i < curr_len; i++ {
			v := queue[i] // pop
			if v == n {
				return cnt
			}
			for j := 1; v+j*j <= n; j++ {
				if !visited[v+j*j] {
					queue = append(queue, v+j*j) // push
					visited[v+j*j] = true
				}
			}
		}
		queue = queue[curr_len:] // delete elements from previous level
		cnt++
	}
	return -1
}

// @lc code=end
