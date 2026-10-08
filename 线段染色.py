# 题目：线段染色问题
# 在数轴上，一共有 n 条线段，小红已经将所有线段都染成了红色。
# 小紫准备至少选择一条线段染成紫色，使得剩余的红色线段互不相交。
# 请帮助小紫输出一个染色方案。

from typing import List, Tuple

def solve(n: int, segments: List[Tuple[int, int]]) -> List[int]:
    # 使用扫描线算法构建线段之间的关系
    events = []
    for i, (l, r) in enumerate(segments):
        events.append((l, 0, i))  # 0表示线段起点
        events.append((r, 1, i))  # 1表示线段终点
    events.sort()  # 按坐标排序
    
    # 构建图：记录相交的线段
    graph = [[] for _ in range(n)]
    active_segments = set()
    
    for _, event_type, seg_idx in events:
        if event_type == 0:  # 线段起点
            # 当前活跃的所有线段都与新线段相交
            for active_seg in active_segments:
                graph[seg_idx].append(active_seg)
                graph[active_seg].append(seg_idx)
            active_segments.add(seg_idx)
        else:  # 线段终点
            active_segments.remove(seg_idx)
    
    def check_no_intersection(segments_set: set) -> bool:
        # 检查给定集合中的线段是否互不相交
        events = []
        for idx in segments_set:
            l, r = segments[idx]
            events.append((l, 0, idx))
            events.append((r, 1, idx))
        events.sort()
        
        active = set()
        for _, event_type, seg_idx in events:
            if event_type == 0:
                if active:  # 如果有活跃线段，说明存在相交
                    return False
                active.add(seg_idx)
            else:
                active.remove(seg_idx)
        return True
    
    # 贪心策略：选择最优的线段染成紫色
    purple = set()
    red = set(range(n))
    
    while red:
        # 检查当前红色线段是否互不相交
        if check_no_intersection(red):
            break
        
        # 选择最优的线段染成紫色
        max_score = -1
        best_segment = -1
        
        for i in red:
            # 计算将i染成紫色后的得分
            # 得分 = 消除的相交数 / (线段长度 * 相邻线段数)
            intersect_count = sum(1 for j in graph[i] if j in red)
            if intersect_count > 0:
                length = segments[i][1] - segments[i][0]
                score = intersect_count / (length * len(graph[i]))
                if score > max_score:
                    max_score = score
                    best_segment = i
        
        if best_segment == -1:
            return [-1]
        
        # 将选中的线段染成紫色
        purple.add(best_segment)
        red.remove(best_segment)
        
        # 检查紫色线段是否互不相交
        if not check_no_intersection(purple):
            return [-1]
    
    if not purple:
        return [-1]
    
    # 返回需要染成紫色的线段编号（编号从1开始）
    return [x + 1 for x in sorted(purple)]

def main():
    # 读取输入
    n = int(input())
    segments = []
    for _ in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))
    
    # 计算结果
    result = solve(n, segments)
    
    # 输出结果
    if result == [-1]:
        print(-1)
    else:
        print(len(result))
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()