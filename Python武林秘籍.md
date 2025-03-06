### Python 数据类型与运算
* **寻求帮助**：  
  ```python
  dir(obj)            # 简单的列出对象obj所包含的方法名称，返回一个字符串列表
  help(obj.func)      # 查询obj.func的具体介绍和用法
  ```

* **测试类型的三种方法**：  
  ```python
  if type(L) == type([]): print("L is list")
  if type(L) == list: print("L is list")
  if isinstance(L, list): print("L is list")
  ```

* **Python 数据类型**：  
  * **哈希类型**：可利用 `hash` 函数查看哈希值，也可作为字典的 `key`。  
    ```python
    "数字类型：int, float, decimal.Decimal, fractions.Fraction, complex"
    "字符串类型：str, bytes"
    "元组：tuple"
    "冻结集合：frozenset"
    "布尔类型：True, False"
    "None"
    ```
  * **不可哈希类型**：原地可变类型，不可作为字典的 `key`。  
    ```python
    "可变类型：list、dict和set"
    ```

### Python 数据类型与运算
* **数字常量**：  
  ```python
  1234, -1234, 0, 999999999                    # 整数
  1.23, 1., 3.14e-10, 4E210, 4.0e+210          # 浮点数
  0o177, 0x9ff, 0X9FF, 0b101010                # 八进制、十六进制、二进制数字
  3+4j, 3.0+4.0j, 3J                           # 复数常量，也可以用complex(real, image)来创建
  hex(I), oct(I), bin(I)                       # 将十进制数转化为十六进制、八进制、二进制表示的“字符串”
  int(str, base)                               # 将字符串转化为整数，base为进制数
  float('inf'), float('-inf'), float('nan')    # 无穷大, 无穷小, 非数
  ```

### Python 数字相关
* **数字相关模块**：  
  * math模块  
  * Decimal模块：小数模块  
    ```python
    import decimal
    from decimal import Decimal
    Decimal("0.01") + Decimal("0.02")        # 返回Decimal("0.03")
    decimal.getcontext().prec = 4            # 设置全局精度为4 即小数点后边4位
    ```
  * Fraction模块：分数模块  
    ```python
    from fractions import Fraction
    x = Fraction(4, 6)                       # 分数类型 4/6
    x = Fraction("0.25")                     # 分数类型 1/4 接收字符串类型的参数
    ```

* **集合 `set`**：  
  ```python
  s = set([3,5,9,10])                        # 创建一个数值集合，返回{3, 5, 9, 10}
  t = set("Hello")                           # 创建一个唯一字符的集合返回{}
  a = t | s          t.union(s)              # t 和 s的并集
  b = t & s         t.intersection(s)        # t 和 s的交集
  c = t – s         t.difference(s)          # 求差集（项在t中, 但不在s中）  
  d = t ^ s          t.symmetric_difference(s) # 对称差集（项在t或s中, 但不会同时出现在二者中）
  {x**2 for x in [1, 2, 3, 4]}               # 集合解析，结果：{16, 1, 4, 9}
  {x for x in 'spam'}                        # 集合解析，结果：{'a', 'p', 's', 'm'}
  ```

### Python 字符串相关
* **字符串操作**：  
  ```python
  S = ''                                      # 空字符串
  S = "spam’s"                                # 双引号和单引号相同
  S = "s\np\ta\x00m"                          # 转义字符
  S = """spam"""                              # 三重引号字符串，一般用于函数说明
  s1+s2, s1*3, s[i], s[i:j], len(s)           # 字符串操作
  'a %s parrot' % 'kind'                      # 字符串格式化表达式
  'a {0} parrot'.format('kind')               # 字符串格式化方法
  ```

* **字符串工具**：  
  ```python
  int('42'),  str(42)                         # 返回(42, '42')
  float('4.13'),  str(4.13)                   # 返回(4.13, '4.13')
  ord('s'),  chr(115)                         # 返回(115, 's')
  int('1001', 2)                              # 将字符串作为二进制数字，转化为数字，返回13
  bin(13), oct(13), hex(13)                   # 将整数转化为二进制/八进制/十六进制字符串，返回('1001', '0o15', '0xd')
  ```
### Python 文件操作
  * **文件基本操作**：  
    ```python
    output = open(r'C:\spam', 'w')          # 打开输出文件，用于写
    fp.read([size])                         # size为读取的长度，以byte为单位
    fp.readline([size])                     # 读一行，如果定义了size，有可能返回的只是一行的一部分
    fp.readlines([size])                    # 把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长。
    fp.readable()                           # 是否可读
    fp.write(str)                           # 把str写到文件中，write()并不会在str后加上一个换行符
    fp.writelines(seq)                      # 把seq的内容全部写到文件中(多行一次性写入)
    fp.writeable()                          # 是否可写
    fp.close()                              # 关闭文件。
    fp.flush()                              # 把缓冲区的内容写入硬盘
    fp.fileno()                             # 返回一个长整型的”文件标签“
    fp.isatty()                             # 文件是否是一个终端设备文件（unix系统中的）
    fp.tell()                               # 返回文件操作标记的当前位置，以文件的开头为原点
    fp.next()                               # 返回下一行，并将文件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。
    fp.seek(offset[,whence])                # 将文件打操作标记移到offset的位置。whence可以为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。
    fp.seekable()                           # 是否可以seek
    fp.truncate([size])                     # 把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。
    for line in open('data'): 
        print(line)                         # 使用for语句，比较适用于打开比较大的文件
    open('f.txt', encoding = 'latin-1')     # Python3.x Unicode文本文件
    open('f.bin', 'rb')                     # Python3.x 二进制bytes文件
    # 文件对象还有相应的属性：buffer closed encoding errors line_buffering name newlines等
    ```

# Python 语法和语句
## 赋值语句
* **基本形式**：  
  ```python
  spam = 'spam'                          # 基本形式
  spam, ham = 'spam', 'ham'              # 元组赋值形式
  [spam, ham] = ['s', 'h']               # 列表赋值形式
  a, b, c, d = 'abcd'                    # 序列赋值形式
  a, *b, c = 'spam'                      # 序列解包形式（Python3.x中才有）
  spam = ham = 'no'                      # 多目标赋值运算，涉及到共享引用
  spam += 42                             # 增强赋值，涉及到共享引用
  ```

* **序列赋值**：  
  ```python
  [a, b, c] = (1, 2, 3)                  # a = 1, b = 2, c = 3
  a, b, c, d = "spam"                    # a = 's', b = 'p'
  a, b, c = range(3)                     # a = 0, b = 1
  a, *b = [1, 2, 3, 4]                   # a = 1, b = [2, 3, 4]
    *a, b = [1, 2, 3, 4]                   # a = [1, 2, 3], b = 4
  a, *b, c = [1, 2, 3, 4]                # a = 1, b = [2, 3], c = 4
  # 带有*时 会优先匹配*之外的变量 如
  a, *b, c = [1, 2]                      # a = 1, c = 2, b = []
  ```

## 条件与循环
* **条件表达式**：  
  ```python
  A = 1 if X else 2
  A = 1 if X else (2 if Y else 3)
  result = (a > 20 and "big than 20" or a > 10 and "big than 10" or a > 5 and "big than 5")
  ```

* **循环**：  
  ```python
  while a > 1:
      ......
  else:
      ......              # else语句会在循环结束后执行，除非在循环中执行了break，同样的还有for语句
  for i in range(5):
      ......
  else:
      ......
  ```

## 控制流
* **列表解析**：  
  ```python
  M = [[1,2,3], [4,5,6], [7,8,9]]
  res = [sum(row) for row in M]                     # G = [6, 15, 24] 一般的列表解析生成一个列表
  res = [c * 2 for c in 'spam']                     # ['ss', 'pp', 'aa', 'mm']
  res = [a * b for a in [1, 2] for b in [4, 5]]     # 多解析过程 返回[4, 5, 8, 10]
  res = [a for a in [1, 2, 3] if a < 2]             # 带判断条件的解析过程
  res = [a if a > 0 else 0 for a in [-1, 0, 1]]     # 带判断条件的高级解析过程
  ```

* **生成器表达式**：  
  ```python
  G = (sum(row) for row in M)                       # 使用小括号可以创建所需结果的生成器generator object
  next(G), next(G), next(G)                         # 输出(6, 15, 24)
  G = {sum(row) for row in M}                       # 解析语法还可以生成集合
  G = {i:sum(M[i]) for i in range(3)}               # 生成字典 {0: 6, 1: 15, 2: 24}
  ```

## 其他
* **print函数**：  
  ```python
  print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
  ```

* **流的重定向**：  
  ```python
  print('hello world')                   # 等于sys.stdout.write('hello world')
  temp = sys.stdout                      # 原有流的保存
  sys.stdout = open('log.log', 'a')      # 流的重定向
  print('hello world')                   # 写入到文件log.log
  sys.stdout.close()
  sys.stdout = temp                      # 原有流的复原
  ```

* **布尔值运算**：  
  ```python
  1 or 2 or 3                            # 返回 1
  1 and 2 and 3                          # 返回 3
  ```

# Python 函数
## 函数定义与调用
* **基本定义与调用**：  
  ```python
  f = lambda x, y, z : x + y + z      # 普通匿名函数，使用方法f(1, 2, 3)
  f = lambda x = 1, y = 1: x + y      # 带默认参数的lambda函数
  def action(x):                      # 嵌套lambda函数
      return (lambda y : x + y)
  ```

* **函数参数**：  
  ```python
  def f(a, b, c): print(a, b, c)
  f(1, 2, 3)                                   # 参数位置匹配
  f(1, c = 3, b = 2)                           # 参数关键字匹配
  def f(a, b = 1, c = 2): print(a, b, c)
  f(1)                                         # 默认参数匹配
  f(1, 2)                                      # 默认参数匹配
  f(a = 1, c = 3)                              # 关键字参数和默认参数的混合
  ```

* **参数解包**：  
  ```python
  def f(a, b, c): print(a, b, c)
  args = (1, 2, 3)
  f(*args)                                    # 1 2 3
  kwargs = {'a':1, 'b':2, 'c':3}
  f(**kwargs)                                 # 1 2 3
  ```

## 生成器函数
* **生成器**：  
  ```python
  def gensquare(N):
      for i in range(N):
          yield i** 2                 # 状态挂起 可以恢复到此时的状态
  for i in gensquare(5):              # 使用方法
      print(i, end = ' ')             # [0, 1, 4, 9, 16]
  ```

* **生成器表达式**：  
  ```python
  G = (x ** 2 for x in range(3))      # 使用小括号可以创建所需结果的生成器generator object
  next(G), next(G), next(G)           # 和上述中的生成器函数的返回值一致
  ```

## 函数属性
* **函数注解**：  
  ```python
  def func(a:'spam', b:(1, 10), c:float) -> int :
      print(a, b, c)
  func.__annotations__                # {'c': <class 'float'>, 'b': (1, 10), 'a': 'spam', 'return': <class 'int'>}
  ```

### Python 内置函数
* **序列操作**：  
  ```python
  list(map(str.upper, open('t')))    # map内置函数
  sorted(iter([2, 5, 8, 3, 1]))      # sorted内置函数
  list(zip([1, 2], [3, 4]))          # zip内置函数 [(1, 3), (2, 4)]
  ```

* **数值操作**：  
  ```python
  abs(x)                              # 求绝对值，参数可以是整型，也可以是复数，若参数是复数，则返回复数的模
  complex([real[, imag]])             # 创建一个复数
  divmod(a, b)                        # 分别取商和余数，注意：整型、浮点型都可以
  float([x])                          # 将一个字符串或数转换为浮点数。如果无参数将返回0.0
  int([x[, base]])                    # 将一个字符串或浮点数转换为int类型，base表示进制
  long([x[, base]])                   # 将一个字符串或浮点数转换为long类型
  pow(x, y)                           # 返回x的y次幂
  range([start], stop[, step])        # 产生一个序列，默认从0开始
  round(x[, n])                       # 四舍五入
  sum(iterable[, start])              # 对集合求和
  oct(x)                              # 将一个数字转化为8进制字符串
  hex(x)                              # 将一个数字转换为16进制字符串
  chr(i)                              # 返回给定int类型对应的ASCII字符
  unichr(i)                           # 返回给定int类型的unicode
  ord(c)                              # 返回ASCII字符对应的整数
  bin(x)                              # 将整数x转换为二进制字符串
  bool([x])                           # 将x转换为Boolean类型
  ```

* **集合操作**：  
  ```python
  basestring()                        # str和unicode的超类，不能直接调用，可以用作isinstance判断
  format(value [, format_spec])       # 格式化输出字符串，格式化的参数顺序从0开始，如“I am {0},I like {1}”
  enumerate(sequence[, start=0])      # 返回一个可枚举的对象，注意它有第二个参数
  iter(obj[, sentinel])               # 生成一个对象的迭代器，第二个参数表示分隔符
  max(iterable[, args...][key])       # 返回集合中的最大值
  min(iterable[, args...][key])       # 返回集合中的最小值
  dict([arg])                         # 创建数据字典
  list([iterable])                    # 将一个集合类转换为另外一个集合类
  set()                               # set对象实例化
  frozenset([iterable])               # 产生一个不可变的set
  tuple([iterable])                   # 生成一个tuple类型
  str([object])                       # 转换为string类型
  sorted(iterable[, cmp[, key[, reverse]]])             # 集合排序
      L = [('b',2),('a',1),('c',3),('d',4)]
      sorted(L, key=lambda x: x[1], reverse=True)      # 使用Key参数和reverse参数
      sorted(L, key=lambda x: (x[0], x[1]))             # 使用key参数进行多条件排序，即如果x[0]相同，则比较x[1]
  ```

* **逻辑判断**：  
  ```python
  all(iterable)                       # 代码:help(all)返回: 当且仅当所有的元素为真的时候为真
  any(iterable)                       # 集合中的元素有一个为真的时候为真
  cmp(x, y)                           # 如果x < y ,返回负数；x == y, 返回0；x > y,返回正数
  ```

* **IO操作**：  
  ```python
  file(filename [, mode [, bufsize]]) # file类型的构造函数。
  input([prompt])                     # 获取用户输入，推荐使用raw_input，因为该函数将不会捕获用户的错误输入
  raw_input([prompt])                 # 设置输入，输入都是作为字符串处理
  open(name[, mode[, buffering]])     # 打开文件，与file有什么不同？推荐使用open
  ```

# Python 模块
## 模块搜索路径
* **确定模块的搜索路径**：  
  ```python
  import sys
  sys.path
  ```

## 模块的导入
* **导入模块**：  
  ```python
  import module1, module2   # 导入模块module1 使用module1.printer()
  from module1 import printer   # 导入module1中的printer变量 使用printer()
  from module1 import *   # 导入模块中的全部变量 使用不必添加module1前缀
  ```

* **重载模块**：  
  ```python
  from imp import reload
  reload(module)
  ```

* **模块的包导入**：  
  ```python
  import dir1.dir2.mod   # d导入包(目录)dir1中的包dir2中的mod模块 此时dir1必须在Python可搜索路径中
  ```
# Python 类与面向对象
## 类的定义
* **普通类定义**：  
  ```python
  class C1(C2, C3):
      spam = 42                       # 数据属性
      def __init__(self, name):       # 函数属性:构造函数
          self.name = name
      def __del__(self):              # 函数属性:析构函数
          print("goodbey ", self.name)    
  I1 = C1('bob')
  ```

## 继承与多态
* **多重继承**：  
  ```python
  class A(B, C):
      pass
  ```

* **子类的初始化**：  
  ```python
  class FooParent(object):
      def __init__(self, a):
          self.parent = 'I\'m the Parent.'
          print('Parent:a=' + str(a))
      def bar(self, message):
          print(message + ' from Parent')
  class FooChild(FooParent):
      def __init__(self, a):
          FooParent.__init__(self, a)
          print('Child:a=' + str(a))
      def bar(self, message):
          FooParent.bar(self, message)
          print(message + ' from Child')
  fooChild = FooChild(10)
  fooChild.bar('HelloWorld')
  ```

### Python 类的高级题材
## 类的高级功能
* **类方法、静态方法、实例方法**：  
  ```python
  class Methods:
      def imeth(self, x): print(self, x)      # 实例方法
      def smeth(x): print(x)                  # 静态方法
      def cmeth(cls, x): print(cls, x)        # 类方法
      smeth = staticmethod(smeth)
      cmeth = classmethod(cmeth)
  obj = Methods()
  obj.imeth(1)                                # <__main__.Methods object...> 1
  Methods.smeth(3)                            # 3
  Methods.cmeth(5)                            # <class '__main__.Methods'> 5
  ```

* **内置函数 `isinstance` 和 `issubclass`**：  
  ```python
  isinstance(1, int)                          # True
  issubclass(bool, int)                       # True
  ```

## 类的修饰器
* **函数装饰器**：  
  ```python
  def decorator(aClass):.....
  @decorator
  class C:....
  ```

## 约束槽
* **限制类属性**：  
```python
class Student:
    __slots__ = ('name', 'age')             # 限制Student及其实例只能拥有name和age属性
```



# Python 异常处理
## 异常的捕获
* **基本语法**：  
  ```python
  try:
      # 可能会引发异常的代码
  except Exception as e:
      # 处理异常的代码
      print(e)
  else:
      # 如果没有发生异常，执行的代码
  finally:
      # 无论是否发生异常，都会执行的代码
  ```
# Python Unicode与字节字符串的处理
## 编码与解码
* **编码和解码的例子**：  
  ```python
  text = "中文"       # Unicode字符串
  encoded_text = text.encode('utf-8')   # 将字符串编码为字节对象
  print(encoded_text)                   # 输出字节形式
  decoded_text = encoded_text.decode('utf-8')   # 将字节对象解码为字符串
  print(decoded_text)                   # 输出原字符串
  ```

## 处理文件
* **写入文本文件**：  
```python
with open('example.txt', 'w', encoding='utf-8') as f:
    f.write("这是一个测试文本。")
```

* **读取文本文件**：  
```python
with open('example.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
```

## 字符串与字节串的互转
* **字符串到字节串**：  
  ```python
  s = 'hello'
  b = s.encode('utf-8')
  print(b)  # b'hello'
  ```

* **字节串到字符串**：  
  ```python
  b = b'hello'
  s = b.decode('utf-8')
  print(s)  # 'hello'
  ```



# Python 其他技巧
## 列表推导式与生成器表达式
* **列表推导式**：  
```python
squares = [x**2 for x in range(10)]
```

* **生成器表达式**：  
```python
squares = (x**2 for x in range(10))
```

## 动态创建类
* **利用 `type` 函数创建类**：  
```python
def greet(self):
    print(f"Hello, my name is {self.name}!")

Person = type('Person', (object,), {'greet': greet})
```

## 元编程
* **装饰器**：  
```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def say_hello(name):
    print(f"Hello, {name}!")
```

## 反射机制
* **检查属性和方法**：  
  ```python
  hasattr(obj, 'name')  # 是否存在属性或方法
  getattr(obj, 'name')  # 获取属性或方法
  setattr(obj, 'name', value)  # 设置属性或方法
  ```
# Python 应用场景
* **自动化脚本**：  
利用 Python 快速编写脚本来完成文件和目录操作、系统任务自动化等。

### 网络爬虫
* **爬取网页**：  
利用 `requests` 和 `BeautifulSoup` 等库爬取网页数据。

### 数据分析
* **处理数据**：  
使用 `pandas` 和 `NumPy` 等库进行数据清洗、转换和分析。

### 机器学习
* **构建模型**：  
利用 `scikit-learn` 和 `TensorFlow` 等库构建和训练机器学习模型。