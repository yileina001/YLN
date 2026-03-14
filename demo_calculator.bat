@echo off
echo ========================================
echo         欢迎使用简单计算器程序
echo ========================================
echo.
:start
echo 请选择运算类型:
echo   + : 加法
echo   - : 减法
echo   * : 乘法
echo   / : 除法
set /p op="请输入运算符: "
if "%op%"=="+" goto calc
if "%op%"=="-" goto calc
if "%op%"=="*" goto calc
if "%op%"=="/" goto calc
echo 错误: 无效的运算符!
goto start

:calc
set /p num1="请输入第一个数字: "
set /p num2="请输入第二个数字: "
if "%op%"=="/" if %num2%==0 (
    echo 错误: 除数不能为零!
    goto ask_continue
)
set /a result=0
if "%op%"=="+" set /a result=%num1%+%num2%
if "%op%"=="-" set /a result=%num1%-%num2%
if "%op%"=="*" set /a result=%num1%*%num2%
if "%op%"=="/" set /a result=%num1%/%num2%
echo.
echo ----------------------------------------
echo 计算结果: %num1% %op% %num2% = %result%
echo ----------------------------------------

:ask_continue
echo.
set /p choice="是否继续计算? (y/n): "
if /i "%choice%"=="y" goto start
echo.
echo ========================================
echo         感谢使用计算器! 再见!
echo ========================================
pause
