import sys
input = sys.stdin.readline

def get_input():
    """读取输入数据"""
    n = int(input())  # 读取数组长度
    from collections import defaultdict
    pos = defaultdict(list)
    maxv = 0
    for i, x in enumerate(list(map(int, input().split()))):
        pos[x].append(i)
        maxv = max(maxv, x)
    return n, pos, maxv

if __name__ == "__main__":
    N, pos, maxv = get_input()
    
    # end[v] 记录值 v 当前还未匹配的最右位置（从右往左扫描）
    end = {v: len(pos[v]) - 1 for v in pos}

    ans = 0  # 记录配对数量
    
    # 贪心策略：从小到大遍历每个值 v，尝试将 v 和 v+1 配对
    for v in range(1, maxv):
        i = end.get(v, -1)      # v 当前最右未匹配位置
        j = end.get(v + 1, -1)  # v+1 当前最右未匹配位置
        
        # 如果 v 或 v+1 不存在，跳过
        if i < 0 or j < 0:
            continue
        
        P, Q = pos[v], pos[v + 1]  # P 是 v 的位置列表，Q 是 v+1 的位置列表
        
        # 贪心匹配：从右往左扫描，尝试让 P[i] < Q[j] 配对
        # 因为需要 i < j（索引要求），所以优先匹配右侧的元素
        while i >= 0 and j >= 0:
            if P[i] < Q[j]:  # 如果 v 的位置在 v+1 位置的左边，可以配对
                ans += 1
                i -= 1  # v 的这个位置已使用，左移
                j -= 1  # v+1 的这个位置已使用，左移
            else:
                i -= 1  # 当前 v 位置太靠右，无法配对，尝试更左的 v
        
        # 更新 end 指针，记录剩余未匹配的位置
        end[v] = i
        end[v + 1] = j
    
    print(ans)
