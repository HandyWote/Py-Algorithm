#输入三角形三边形成列表赋值给abc
a,b,c = map(float,input().split())
#定义p
p = 0.5 * (a + c + b)
#三角形公式
print('%.1f'% pow(p*(p-b)*(p-c)*(p-a),0.5))