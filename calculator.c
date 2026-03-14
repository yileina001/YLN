/*
 * 简单计算器程序
 * 功能: 实现加、减、乘、除四则运算
 * 作者: Trae AI
 * 日期: 2026-03-14
 */

#include <stdio.h>   // 标准输入输出头文件
#include <ctype.h>   // 字符处理函数头文件

// 使用宏定义避免魔法数字，提高代码可读性
#define ADD '+'       // 加法运算符
#define SUBTRACT '-'  // 减法运算符
#define MULTIPLY '*'  // 乘法运算符
#define DIVIDE '/'    // 除法运算符

// 函数声明（提前声明函数，使代码结构更清晰）
void showWelcomeMessage();       // 显示欢迎信息
void showMenu();                 // 显示运算菜单
char getOperator();              // 获取并验证运算符
double getOperand(const char *prompt); // 获取操作数（带校验）
double calculate(double num1, char op, double num2); // 核心计算函数
void printResult(double num1, char op, double num2, double result); // 输出结果
void clearInputBuffer();         // 清空输入缓冲区（处理非法输入）

/*
 * 主函数: 程序入口，控制整体流程
 */
int main() {
    char operator;    // 存储运算符
    double num1, num2; // 存储两个操作数
    double result;     // 存储计算结果
    char continueChoice; // 存储用户是否继续的选择

    // 显示欢迎信息
    showWelcomeMessage();

    // 主循环: 支持多次计算
    do {
        // 显示运算菜单
        showMenu();
        
        // 获取并验证运算符
        operator = getOperator();
        if (operator == '?') {  // '?'表示无效输入
            printf("错误: 无效的运算符! 请使用 + - * /\n");
            clearInputBuffer(); // 清空缓冲区，避免影响后续输入
            continue;           // 跳过本次循环，重新开始
        }

        // 获取两个操作数
        num1 = getOperand("请输入第一个数字: ");
        num2 = getOperand("请输入第二个数字: ");

        // 除法运算特殊处理: 除数不能为零
        if (operator == DIVIDE && num2 == 0) {
            printf("错误: 除数不能为零! 除法无意义.\n");
            continue;
        }

        // 执行计算
        result = calculate(num1, operator, num2);
        
        // 输出结果
        printResult(num1, operator, num2, result);

        // 询问是否继续计算
        printf("\n是否继续计算? (y/n): ");
        while (1) {
            scanf(" %c", &continueChoice);
            continueChoice = tolower(continueChoice); // 转换为小写
            if (continueChoice == 'y' || continueChoice == 'n') {
                break; // 输入有效，退出循环
            }
            printf("请输入 'y' 或 'n': ");
            clearInputBuffer();
        }

    } while (continueChoice == 'y'); // 用户输入'y'则继续

    printf("\n========================================\n");
    printf("        感谢使用计算器! 再见!\n");
    printf("========================================\n");
    
    return 0; // 程序正常结束
}

/*
 * 函数: showWelcomeMessage
 * 功能: 显示程序欢迎界面
 */
void showWelcomeMessage() {
    printf("========================================\n");
    printf("        欢迎使用简单计算器程序\n");
    printf("========================================\n");
}

/*
 * 函数: showMenu
 * 功能: 显示运算类型菜单
 */
void showMenu() {
    printf("\n请选择运算类型:\n");
    printf("  + : 加法 (Addition)\n");
    printf("  - : 减法 (Subtraction)\n");
    printf("  * : 乘法 (Multiplication)\n");
    printf("  / : 除法 (Division)\n");
    printf("请输入运算符: ");
}

/*
 * 函数: getOperator
 * 功能: 获取用户输入的运算符并验证有效性
 * 返回: 有效运算符 或 '?'（表示无效）
 */
char getOperator() {
    char op;
    scanf(" %c", &op); // 空格跳过前导空白字符
    
    // 验证运算符是否合法
    if (op == ADD || op == SUBTRACT || op == MULTIPLY || op == DIVIDE) {
        return op; // 返回有效运算符
    }
    return '?'; // 返回'?'表示无效输入
}

/*
 * 函数: getOperand
 * 功能: 获取用户输入的数字，带输入校验
 * 参数: prompt - 提示信息字符串
 * 返回: 用户输入的有效数字
 */
double getOperand(const char *prompt) {
    double num;
    printf("%s", prompt);
    
    // 循环直到输入有效数字
    while (scanf("%lf", &num) != 1) {
        printf("输入无效! 请输入一个数字: ");
        clearInputBuffer(); // 清空缓冲区中的非法字符
    }
    return num;
}

/*
 * 函数: calculate
 * 功能: 核心计算函数，根据运算符执行相应计算
 * 参数: num1 - 第一个操作数, op - 运算符, num2 - 第二个操作数
 * 返回: 计算结果
 */
double calculate(double num1, char op, double num2) {
    switch (op) {
        case ADD:
            return num1 + num2;
        case SUBTRACT:
            return num1 - num2;
        case MULTIPLY:
            return num1 * num2;
        case DIVIDE:
            return num1 / num2;
        default:
            return 0; // 理论上不会执行到这里
    }
}

/*
 * 函数: printResult
 * 功能: 格式化输出计算结果
 * 参数: num1, op, num2 - 参与运算的数和运算符, result - 结果
 */
void printResult(double num1, char op, double num2, double result) {
    printf("\n----------------------------------------\n");
    printf("计算结果: %.2lf %c %.2lf = %.2lf\n", num1, op, num2, result);
    printf("----------------------------------------\n");
}

/*
 * 函数: clearInputBuffer
 * 功能: 清空输入缓冲区，处理非法输入残留
 * 原理: 读取缓冲区字符直到遇到换行符或文件结束
 */
void clearInputBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}
