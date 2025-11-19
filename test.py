import time

class test():
    def __init__(self, cases: dict, solution: object = None, func: str = None) -> None:
        """
        初始化测试类

        参数:
            cases: 测试用例字典,格式为 {'input': [...], 'output': [...]}
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
        for i, c in enumerate(self.cases['input']):
            print(f"\n{'='*60}")
            print(f"Test {i+1}: {c}")
            print(f"{'='*60}")

            # 记录开始时间
            start_time = time.time()

            # 处理参数解包
            if isinstance(c, tuple):
                result = method(*c)
            else:
                result = method(c)

            # 记录结束时间并计算耗时
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000  # 转换为毫秒
            total_time += elapsed_time

            expected = self.cases['output'][i]

            # 打印结果和耗时
            print(f"  Result   : {result}")
            print(f"  Expected : {expected}")
            print(f"  Status   : {'✓ PASS' if result == expected else '✗ FAIL'}")
            print(f"  Time     : {elapsed_time:.2f} ms")

            assert result == expected, f"Test {i+1} failed, expected {expected} but got {result}"

        # 打印总结
        print(f"\n{'='*60}")
        print(f"All tests passed! ({len(self.cases['input'])} tests)")
        print(f"Total time: {total_time:.2f} ms")
        print(f"Average time: {total_time/len(self.cases['input']):.2f} ms")
        print(f"{'='*60}")