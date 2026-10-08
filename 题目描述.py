# 题目：红色连通块
# 小红拿到了一张由 n 个节点组成的网，她已经把所有节点染成了红色。这时，小紫准备将 k 个节点染成紫色，使得最大的红色连通块大小尽可能小。
# 对于网上的两个点，如果它们均为红色且相连，则称它们为红色连通块。特别地，一个单独的点也构成一个红色连通块，连通块的大小为连通块中节点的数量。

# 输入格式：
# 第一行输入两个正整数 n, k (1 ≤ k ≤ n ≤ 10^5)，代表节点数量和小紫准备染色的次数。
# 此后 n-1 行，第 i 行输入两个正整数 ui, vi (1 ≤ ui, vi ≤ n)，代表第 i 条边的连接节点。ui 和节点 vi。保证输入的图是一棵树。

# 输出格式：
# 一个整数，代表最大红色连通块大小的最小值。特别的，如果不存在红色连通块，请输出 0。

from collections import defaultdict
from typing import List, Set

def solve(n: int, k: int, edges: List[List[int]]) -> int:
    # 构建邻接表表示的图
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(node: int, visited: Set[int], purple: Set[int]) -> int:
        # 如果当前节点是紫色，返回0
        if node in purple:
            return 0
        
        # 标记当前节点为已访问
        visited.add(node)
        size = 1  # 当前节点计入连通块大小
        
        # 遍历所有相邻节点
        for neighbor in graph[node]:
            if neighbor not in visited:
                size += dfs(neighbor, visited, purple)
        
        return size
    
    def get_max_component_size(purple: Set[int]) -> int:
        visited = set()
        max_size = 0
        
        # 遍历所有节点，找到最大的红色连通块
        for node in range(1, n + 1):
            if node not in visited and node not in purple:
                max_size = max(max_size, dfs(node, visited, purple))
        
        return max_size
    
    # 如果可以将所有节点都染成紫色
    if k >= n:
        return 0
    
    # 贪心策略：选择将关键节点染成紫色
    # 这里我们选择度数最大的节点进行染色
    degree = [(len(graph[i]), i) for i in range(1, n + 1)]
    degree.sort(reverse=True)
    
    # 选择前k个度数最大的节点染成紫色
    purple = set(node for _, node in degree[:k])
    
    return get_max_component_size(purple)

def main():
    # 读取输入
    n, k = map(int, input().split())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append([u, v])
    
    # 计算并输出结果
    result = solve(n, k, edges)
    print(result)

if __name__ == "__main__":
    main()