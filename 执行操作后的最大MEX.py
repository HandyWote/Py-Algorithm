from collections import Counter



class Solution:
    def findSmallestInteger(self, nums: list[int], m: int) -> int:
        cnt = Counter(x % m for x in nums)
        mex = 0
        while cnt[mex % m]:
            cnt[mex % m] -= 1
            mex += 1
        return mex

def test():
    """
    企业级测试函数，用于验证 Solution 类的 findSmallestInteger 方法
    
    测试策略：
    1. 边界值测试
    2. 正常情况测试
    3. 异常情况测试
    4. 性能测试
    """
    solution = Solution()
    
    # 测试用例数据结构：包含输入、预期输出和测试描述
    test_cases = [
        # 基本功能测试
        {
            "input": {"nums": [1, -10, 7, 13, 6, 8], "m": 5},
            "expected": 4,
            "description": "基本测试用例1"
        },
        {
            "input": {"nums": [1, -10, 7, 13, 6, 8], "m": 7},
            "expected": 2,
            "description": "基本测试用例2"
        },
        
        # 边界值测试
        {
            "input": {"nums": [], "m": 1},
            "expected": 0,
            "description": "空数组测试"
        },
        {
            "input": {"nums": [0], "m": 1},
            "expected": 1,
            "description": "单个元素测试"
        },
        {
            "input": {"nums": [0, 1, 2, 3, 4], "m": 5},
            "expected": 5,
            "description": "完整模数序列测试"
        },
        
        # 极端情况测试
        {
            "input": {"nums": [i for i in range(1000)], "m": 1},
            "expected": 1000,
            "description": "大数组测试"
        },
        {
            "input": {"nums": [i for i in range(100)], "m": 100},
            "expected": 100,
            "description": "大模数测试"
        }
    ]
    
    # 执行测试用例
    passed = 0
    failed = 0
    
    for i, test_case in enumerate(test_cases):
        try:
            result = solution.findSmallestInteger(
                test_case["input"]["nums"],
                test_case["input"]["m"]
            )
            
            if result == test_case["expected"]:
                print(f"✓ 测试用例 {i+1} 通过: {test_case['description']}")
                passed += 1
            else:
                print(f"✗ 测试用例 {i+1} 失败: {test_case['description']}")
                print(f"  输入: {test_case['input']}")
                print(f"  预期: {test_case['expected']}")
                print(f"  实际: {result}")
                failed += 1
                
        except Exception as e:
            print(f"✗ 测试用例 {i+1} 异常: {test_case['description']}")
            print(f"  异常信息: {str(e)}")
            failed += 1
    
    # 性能测试
    print("\n执行性能测试...")
    import time
    start_time = time.time()
    
    # 大数据集性能测试
    large_nums = [i for i in range(10000)]
    result = solution.findSmallestInteger(large_nums, 1000)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"大数据集测试完成 (10,000 元素)")
    print(f"执行时间: {execution_time:.6f} 秒")
    print(f"结果: {result}")
    
    # 测试结果汇总
    print(f"\n测试结果汇总:")
    print(f"通过: {passed}")
    print(f"失败: {failed}")
    print(f"总计: {passed + failed}")
    
    if failed == 0:
        print("🎉 所有测试用例都通过了！")
        return True
    else:
        print("❌ 有测试用例失败，请检查实现。")
        return False

if __name__ == "__main__":
    test()