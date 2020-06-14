#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
#
# algorithms
# Medium (37.63%)
# Likes:    1636
# Dislikes: 57
# Total Accepted:    87.4K
# Total Submissions: 229.9K
# Testcase Example:  '3\n[[0,1,100],[1,2,100],[0,2,500]]\n0\n2\n1'
#
# There are n cities connected by m flights. Each flight starts from city u and
# arrives at v with a price w.
# 
# Now given all the cities and flights, together with starting city src and the
# destination dst, your task is to find the cheapest price from src to dst with
# up to k stops. If there is no such route, output -1.
# 
# 
# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation: 
# The graph looks like this:
# 
# 
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as
# marked red in the picture.
# 
# 
# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation: 
# The graph looks like this:
# 
# 
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as
# marked blue in the picture.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to
# n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.
# 
# 
#

# @lc code=start
import collections
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        '''
            Use dijkstra algorithm
            Every time a new (price, node, n_steps) tuple is poped out from the min heap
            it means that the node is in the current explored space, and has the cheapest 
            path to the src node.
            Therefore, once the dst node is discovered, the path to it must also be cheapest
        '''
        # step 1, create an internal representation of the graph
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w

        # step 2, create min heap to store exploration state
        heap = [(0, src, K + 1)]
        while heap:
            price, u, n_steps = heapq.heappop(heap)
            if u == dst:
                return price
            if n_steps > 0:  # if we can go more steps from this node u
                for v in graph[u]:
                    heapq.heappush(heap, (price + graph[u][v], v, n_steps - 1))
        return -1

        
# @lc code=end

