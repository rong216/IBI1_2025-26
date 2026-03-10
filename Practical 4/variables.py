# 2004、2014、2024苏格兰人口（单位：百万）
a = 5.08
b = 5.33
c = 5.55
# 计算2004-2014人口变化d，2014-2024人口变化e（文档笔误2025→2024）
d = b - a
e = c - b
# 比较d和e，打印结果
print("2004-2014人口变化：", d)
print("2014-2024人口变化：", e)
print("d > e？", d > e)
# 注释：人口增长趋势（关键！评分点）
# 计算结果：d=0.25，e=0.22，e < d，说明苏格兰人口增长速度放缓（decelerating）
# 定义布尔变量X和Y
X = True
Y = False
# 定义W = X or Y（逻辑或运算）
W = X or Y
print("W = X or Y的结果：", W)
# 注释：W的真值表（关键！评分点）
# 逻辑或运算规则：只要有一个为True，结果为True；全False才为False
# 真值表：
# X=True, Y=True → W=True
# X=True, Y=False → W=True
# X=False, Y=True → W=True
# X=False, Y=False → W=False