# 伪代码：IBI1班级感染率模拟
# 1. 定义初始变量：初始感染人数、日增长率、班级总人数n=91、初始天数=0
# 2. 打印表头，显示每日感染人数
# 3. 使用循环（while），只要当前感染人数 < 91，就计算下一日感染人数
# 4. 每日感染人数 = 前一日感染人数 × (1 + 增长率)
# 5. 天数逐次加1，打印当日天数和感染人数
# 6. 当感染人数 ≥91时，退出循环，打印总天数
# # 实际代码
initial_infected = 5  # 初始感染人数
growth_rate = 0.4     # 日增长率40%
total_students = 91   # 班级总人数
current_infected = initial_infected
days = 0

# 打印初始信息
print("IBI1班级感染人数模拟")
print(f"第{days}天，感染人数：{current_infected}")

# while循环计算每日感染人数
while current_infected < total_students:
    current_infected = current_infected * (1 + growth_rate)
    days += 1
    print(f"第{days}天，感染人数：{current_infected:.1f}")  # 保留1位小数，更清晰

# 循环结束，打印总天数
print(f"\n全部{total_students}人感染共花费：{days}天")