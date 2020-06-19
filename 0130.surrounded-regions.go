/*
 * @lc app=leetcode id=130 lang=golang
 *
 * [130] Surrounded Regions
 *
 * https://leetcode.com/problems/surrounded-regions/description/
 *
 * algorithms
 * Medium (23.19%)
 * Likes:    1711
 * Dislikes: 651
 * Total Accepted:    233.5K
 * Total Submissions: 847.8K
 * Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
 *
 * Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
 * surrounded by 'X'.
 *
 * A region is captured by flipping all 'O's into 'X's in that surrounded
 * region.
 *
 * Example:
 *
 *
 * X X X X
 * X O O X
 * X X O X
 * X O X X
 *
 *
 * After running your function, the board should be:
 *
 *
 * X X X X
 * X X X X
 * X X X X
 * X O X X
 *
 *
 * Explanation:
 *
 * Surrounded regions shouldn't be on the border, which means that any 'O's on
 * the border of the board are not flipped to 'X'. Any 'O's that is not on the
 * border and it is not connected to an 'O's on the border will be flipped to
 * 'X'. Two cells are connected if they are adjacent cells connected
 * horizontally or vertically.
 *
 */

// @lc code=start
func mark_dfs(board [][]byte, x, y int) {
	// x, y is the pos to start search

	if x < 0 || x >= len(board) || y < 0 || y >= len(board[0]) {
		return
	}

	if board[x][y] == 'O' {
		board[x][y] = '#'
		mark_dfs(board, x + 1, y)
		mark_dfs(board, x - 1, y)
		mark_dfs(board, x, y + 1)
		mark_dfs(board, x, y - 1)
	}
}

func solve(board [][]byte) {
	// start from 4 borders and mark all 'O's that shouldn't be flipped
	if len(board) == 0 {
		return
	}
	n_rows, n_cols := len(board), len(board[0])

	for row := range board {
		mark_dfs(board, row, n_cols-1)
		mark_dfs(board, row, 0)
	}

	for col := range board[0] {
		mark_dfs(board, 0, col)
		mark_dfs(board, n_rows-1, col)
	}

	for row := range board {
		for col := range board[row] {
			if board[row][col] == '#' {
				board[row][col] = 'O'
			} else {
				board[row][col] = 'X'
			}
		}
	}
}

// @lc code=end
