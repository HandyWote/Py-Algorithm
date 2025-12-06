import time
from typing import Any


class Case:
    """测试用例类，用于存储和管理测试输入输出数据"""
    
    def __init__(self):
        """初始化测试用例对象"""
        self.input: list = []
        self.output: list = []
    
    def add_case(self, input_data: Any, expected_output: Any) -> None:
        """
        添加单个测试用例
        
        参数:
            input_data: 测试输入数据
            expected_output: 期望的输出结果
        """
        self.input.append(input_data)
        self.output.append(expected_output)
    
    def add_cases(self, cases: list) -> None:
        """
        批量添加测试用例
        
        参数:
            cases: 测试用例列表，每个元素为 (input, output) 元组
        """
        for input_data, expected_output in cases:
            self.add_case(input_data, expected_output)
    
    def clear(self) -> None:
        """清空所有测试用例"""
        self.input.clear()
        self.output.clear()
    
    def __len__(self) -> int:
        """返回测试用例数量"""
        return len(self.input)


class Test:
    """测试执行类，用于运行和验证测试用例"""
    
    def __init__(self, cases: Case, solution: object = None, func: str = None) -> None:
        """
        初始化测试类
        
        参数:
            cases: Case对象，包含所有测试用例
            solution: 解决方案对象(可选,可以在run时传入)
            func: 要调用的方法名(可选,可以在run时传入)
        """
        self.cases = cases
        self.solution = solution
        self.func = func
    
    def run(self, solution: object = None, func_name: str = None):
        """
        运行测试用例
        
        参数:
            solution: 解决方案对象(如果初始化时未传入,则必须在此传入)
            func_name: 要调用的方法名(如果初始化时未传入,则必须在此传入)
        """
        # 使用传入的参数或初始化时保存的参数
        solution_obj = solution or self.solution
        method_name = func_name or self.func
        
        if solution_obj is None:
            raise ValueError("必须提供解决方案对象")
        if method_name is None:
            raise ValueError("必须提供方法名")
        
        # 获取方法对象
        method = getattr(solution_obj, method_name)
        
        # 运行测试用例
        total_time = 0
        passed_count = 0
        
        for i, input_data in enumerate(self.cases.input):
            print(f"\n{'='*60}")
            print(f"Test {i+1}: {input_data}")
            print(f"{'='*60}")
            
            # 记录开始时间
            start_time = time.time()
            
            # 处理参数解包
            try:
                if isinstance(input_data, tuple):
                    result = method(*input_data)
                else:
                    result = method(input_data)
                
                # 记录结束时间并计算耗时
                end_time = time.time()
                elapsed_time = (end_time - start_time) * 1000  # 转换为毫秒
                total_time += elapsed_time
                
                expected = self.cases.output[i]
                
                # 检查结果
                passed = result == expected
                
                # 打印结果和耗时
                print(f"  Result   : {result}")
                print(f"  Expected : {expected}")
                print(f"  Status   : {'✓ PASS' if passed else '✗ FAIL'}")
                print(f"  Time     : {elapsed_time:.2f} ms")
                
                if passed:
                    passed_count += 1
                else:
                    print(f"  Error    : 结果不匹配")
                    
            except Exception as e:
                # 记录结束时间并计算耗时
                end_time = time.time()
                elapsed_time = (end_time - start_time) * 1000  # 转换为毫秒
                total_time += elapsed_time
                
                print(f"  Result   : ERROR")
                print(f"  Expected : {self.cases.output[i]}")
                print(f"  Status   : ✗ FAIL")
                print(f"  Time     : {elapsed_time:.2f} ms")
                print(f"  Error    : {str(e)}")
        
        # 打印总结
        print(f"\n{'='*60}")
        print(f"测试结果: {passed_count}/{len(self.cases.input)} 通过")
        print(f"总耗时: {total_time:.2f} ms")
        if len(self.cases.input) > 0:
            print(f"平均耗时: {total_time/len(self.cases.input):.2f} ms")
        print(f"{'='*60}")


# 示例使用方法
if __name__ == '__main__':
    # 示例解决方案类
    class Solution:
        def add(self, a, b):
            return a + b
            
        def multiply(self, a, b):
            return a * b
    
    # 创建测试用例
    cases = Case()
    cases.add_case((1, 2), 3)  # add(1, 2) = 3
    cases.add_case((3, 4), 7)  # add(3, 4) = 7
    cases.add_case((-1, 1), 0) # add(-1, 1) = 0
    cases.clear()
    cases.add_cases([
        ((1, 2), 3),    # add(1, 2) 应该返回 3
        ((3, 4), 7),    # add(3, 4) 应该返回 7
        ((-1, 1), 0),   # add(-1, 1) 应该返回 0
        ((5, -2), 3)    # add(5, -2) 应该返回 3
    ])
    
    # 创建测试对象
    solution = Solution()
    test = Test(cases, solution, "add")
    
    # 运行测试
    test.run()