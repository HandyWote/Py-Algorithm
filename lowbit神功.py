import sys
from functools import lru_cache

MOD = 998244353

def lowbit(x):
    """返回x在二进制表示中，最低位的1及其后所有0组成的数"""
    return x & -x

@lru_cache(maxsize=200000)  # 限制缓存大小，最多约25MB内存
def get_value_after_ops(x, ops):
    """计算x经过ops次操作后的值，使用LRU缓存"""
    x = x % MOD
    for _ in range(ops):
        lb = lowbit(x)
        if lb == 0:
            break
        x = (x + lb) % MOD
    return x

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    q = int(data[idx]); idx += 1
    a = []
    for i in range(n):
        a.append(int(data[idx])); idx += 1
    
    ops_count = 0  # 全局操作计数器
    
    for _ in range(q):
        opt = int(data[idx]); idx += 1
        if opt == 1:
            # 操作1：所有元素执行一次lowbit操作
            ops_count += 1
        else:
            # 操作2：查询总和
            result = 0
            # 限制操作次数，避免重复计算
            actual_ops = min(ops_count, 31)
            for i in range(n):
                result = (result + get_value_after_ops(a[i], actual_ops)) % MOD
            print(result)

if __name__ == '__main__':
    main()