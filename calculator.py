# 简单计算器程序 - Python版本
# 功能: 实现加、减、乘、除四则运算，带输入校验
# 适合Python新手学习

def get_number(prompt):
    """
    获取用户输入的数字，并进行合法性校验
    参数: prompt - 提示信息字符串
    返回: 有效的浮点数
    """
    while True:
        try:
            # 获取用户输入并转换为浮点数
            num = float(input(prompt))
            return num
        except ValueError:
            # 如果转换失败，说明输入不是有效数字
            print("❌ 输入错误! 请输入一个有效的数字.")

def get_operator():
    """
    获取并验证运算符
    返回: 有效的运算符 (+, -, *, /)
    """
    valid_operators = ['+', '-', '*', '/']
    while True:
        op = input("请输入运算符号 (+, -, *, /): ").strip()
        if op in valid_operators:
            return op
        else:
            print(f"❌ 无效的运算符! 请使用 {valid_operators} 中的一个.")

def calculate(num1, operator, num2):
    """
    根据运算符执行计算
    参数: num1 - 第一个数字, operator - 运算符, num2 - 第二个数字
    返回: 计算结果
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # 除法运算前检查除数是否为0
        if num2 == 0:
            return None  # 返回None表示除零错误
        return num1 / num2

def main():
    """
    主函数: 程序入口
    """
    print("=" * 40)
    print("🎉 欢迎使用Python简单计算器 🎉")
    print("=" * 40)
    print()

    # 1. 获取第一个数字
    num1 = get_number("请输入第一个数字: ")

    # 2. 获取运算符
    operator = get_operator()

    # 3. 获取第二个数字
    num2 = get_number("请输入第二个数字: ")

    # 4. 执行计算
    result = calculate(num1, operator, num2)

    # 5. 输出结果
    print()
    print("-" * 40)
    if result is None:
        print("❌ 错误: 除数不能为0! 除法运算无意义.")
    else:
        # 结果保留2位小数
        print(f"✅ 计算结果: {num1:.2f} {operator} {num2:.2f} = {result:.2f}")
    print("-" * 40)

# 程序入口: 只有直接运行此文件时才执行main()
if __name__ == "__main__":
    main()
