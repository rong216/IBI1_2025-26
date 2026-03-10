# 伪代码：肌酐清除率（CrCl）计算器
# 1. 定义输入变量：年龄(age)、体重(weight)、性别(gender)、肌酐浓度(Cr)
# 2. 输入合法性校验规则：
#    - 年龄 < 100岁
#    - 体重 20kg < weight < 80kg
#    - 肌酐浓度 0 < Cr < 100 μmol/l
#    - 性别只能是male/female（小写，统一格式）
# 3. 校验逻辑：逐个判断变量是否符合规则，若有非法变量，打印错误提示（说明哪个变量需修正）
# 4. 若所有输入合法，根据性别计算CrCl
# 5. 输出最终的CrCl结果

# 实际代码：定义测试变量（可自行修改数值测试合法/非法情况）
age = 50
weight = 60
gender = "female"  # 仅支持male/female，小写
Cr = 80  # 肌酐浓度，μmol/l

# 初始化错误标记
is_invalid = False
error_msg = "需修正的变量："

# 合法性校验
if age >= 100:
    is_invalid = True
    error_msg += "年龄（需<100)、"
if weight <= 20 or weight >= 80:
    is_invalid = True
    error_msg += "体重(需20<体重<80)、"
if Cr <= 0 or Cr >= 100:
    is_invalid = True
    error_msg += "肌酐浓度(需0<Cr<100)、"
if gender not in ["male", "female"]:
    is_invalid = True
    error_msg += "性别(仅支持male/female)、"

# 处理错误信息，去除末尾的顿号
if is_invalid:
    error_msg = error_msg[:-1]
    print(error_msg)
else:
    # 输入合法，计算CrCl
    if gender == "female":
        crcl = ((140 - age) * weight) / (72 * Cr) * 0.85
    else:
        crcl = ((140 - age) * weight) / (72 * Cr)
    # 打印结果，保留2位小数更符合临床规范
    print(f"肌酐清除率(CrCl):{crcl:.2f} ml/min")