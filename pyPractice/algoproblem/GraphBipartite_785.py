# -*- coding:utf-8 -*-
"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation:
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation:
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.


Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in graph[j].
"""




class Solution:
    def isBipartite(self, graph) -> bool:
        set1 = set()
        set2 = set()

        for node in range(len(graph)):
            neighbors = graph[node]
            if node in set1:
                for neighbor in neighbors:
                    set2.add(neighbor)
            elif node in set2:
                for neighbor in neighbors:
                    set1.add(neighbor)
            else:

                if len(set(neighbors) & set1) != 0:
                    set2.add(node)
                elif len(set(neighbors) & set2) != 0:
                    set1.add(node)
                else:
                    set1.add(node)
                    for neighbor in neighbors:
                        set2.add(neighbor)

            if len(set1 & set2) != 0:
                return False
        return True

    def isBipartite2(self, graph) -> bool:
        color = {}

        # 深度搜索，如果不能切分成功，返回False,
        def dfs_div(node):
            for neighbor in graph[node]:
                if neighbor in color:
                    if color[neighbor] == color[node]:  # 递归基准点，如果相邻两点的颜色判断相同，则不能
                        return False
                else:
                    color[neighbor] = 1 - color[node]
                    print(color)
                    if not dfs_div(neighbor):
                        return False
            return True

        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
            if not dfs_div(node):

                return False
        return True











# input = [[1, 3], [0, 2], [1, 3], [0, 2]]
input = [[1,2,3], [0,2], [0,1,3], [0,2]]
input = [[1],[0,3],[3],[1,2]]
input = [[3],[2,4],[1],[0,4],[1,3]]
#

s = Solution()
result = s.isBipartite2(input)
print(result)
