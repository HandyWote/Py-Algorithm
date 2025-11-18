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
        for i, c in enumerate(self.cases['input']):
            print(f"\n=== Test {i+1}: {c} ===")
            
            # 处理参数解包
            if isinstance(c, tuple):
                result = method(*c)
            else:
                result = method(c)
            
            expected = self.cases['output'][i]
            print(f"Result: {result}, Expected: {expected}")
            
            assert result == expected, f"Test {i+1} failed, expected {expected} but get {result}"
            print(f"Test {i+1} passed")
        
        print('All test passed')