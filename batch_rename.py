# 文件批量重命名工具
# 功能: 批量重命名指定文件夹下特定后缀的文件
# 作者: Trae AI
# 日期: 2026-03-14

import os  # 操作系统接口模块
import sys # 系统模块

def get_user_input():
    """
    获取用户输入参数
    返回: (folder_path, prefix, start_num, extensions)
    """
    print("=" * 50)
    print("📁 文件批量重命名工具")
    print("=" * 50)
    print()
    
    # 获取目标文件夹路径
    folder_path = input("请输入目标文件夹路径: ").strip()
    
    # 获取前缀名
    prefix = input("请输入文件名前缀(如photo_): ").strip()
    
    # 获取起始编号
    while True:
        try:
            start_num = int(input("请输入起始编号(如1): "))
            if start_num < 0:
                print("❌ 编号不能为负数，请重新输入!")
                continue
            break
        except ValueError:
            print("❌ 请输入有效的整数!")
    
    # 获取文件后缀
    extensions_input = input("请输入要重命名的文件后缀(用空格分隔,如 .txt .jpg): ").strip()
    extensions = tuple(ext.lower() for ext in extensions_input.split())
    
    print()
    print("-" * 50)
    print(f"目标文件夹: {folder_path}")
    print(f"文件名前缀: {prefix}")
    print(f"起始编号: {start_num}")
    print(f"目标后缀: {extensions if extensions else '所有文件'}")
    print("-" * 50)
    
    confirm = input("\n确认开始重命名? (y/n): ").strip().lower()
    if confirm != 'y':
        print("❌ 操作已取消!")
        sys.exit(0)
    
    return folder_path, prefix, start_num, extensions

def batch_rename_files(folder_path, prefix, start_num, extensions):
    """
    批量重命名文件
    参数: folder_path - 目标文件夹路径
          prefix - 文件名前缀
          start_num - 起始编号
          extensions - 文件后缀元组
    返回: (success_list, failed_list)
    """
    success_list = []   # 重命名成功的文件列表
    failed_list = []    # 重命名失败的文件列表
    current_num = start_num  # 当前编号
    
    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        print(f"\n❌ 错误: 文件夹 '{folder_path}' 不存在!")
        return [], [("文件夹不存在", folder_path)]
    
    # 检查是否有访问权限
    if not os.access(folder_path, os.R_OK | os.W_OK):
        print(f"\n❌ 错误: 没有权限访问文件夹 '{folder_path}'!")
        return [], [("无访问权限", folder_path)]
    
    # 获取文件夹下所有文件
    try:
        all_items = os.listdir(folder_path)
    except PermissionError:
        return [], [("无权限读取文件列表", folder_path)]
    
    # 筛选出文件(排除文件夹)
    files = []
    for item in all_items:
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            files.append(item)
    
    # 筛选指定后缀的文件
    if extensions:
        target_files = [f for f in files if f.lower().endswith(extensions)]
    else:
        target_files = files
    
    # 对文件进行排序(按名称和数字智能排序)
    try:
        target_files.sort(key=lambda x: int(''.join(filter(str.isdigit, x))) if any(c.isdigit() for c in x) else x)
    except:
        target_files.sort()  # 排序失败时使用普通排序
    
    if not target_files:
        print(f"\nℹ️ 文件夹中没有找到符合条件的文件!")
        return [], []
    
    print(f"\n找到 {len(target_files)} 个符合条件的文件，开始处理...\n")
    
    # 执行重命名
    for filename in target_files:
        try:
            # 获取文件扩展名
            _, ext = os.path.splitext(filename)
            # 构建新文件名
            new_filename = f"{prefix}{current_num}{ext}"
            # 完整路径
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            
            # 检查新文件名是否已存在
            if os.path.exists(new_path):
                failed_list.append((filename, f"目标文件 '{new_filename}' 已存在"))
                continue
            
            # 执行重命名
            os.rename(old_path, new_path)
            success_list.append((filename, new_filename))
            print(f"✅ {filename} → {new_filename}")
            
            current_num += 1
            
        except PermissionError:
            failed_list.append((filename, "无权限重命名"))
        except FileExistsError:
            failed_list.append((filename, "目标文件已存在"))
        except Exception as e:
            failed_list.append((filename, str(e)))
    
    return success_list, failed_list

def print_results(success_list, failed_list):
    """
    打印重命名结果
    """
    print()
    print("=" * 50)
    print("📊 重命名结果统计")
    print("=" * 50)
    
    # 打印成功列表
    if success_list:
        print(f"\n✅ 成功重命名 {len(success_list)} 个文件:")
        for old, new in success_list:
            print(f"   {old} → {new}")
    else:
        print("\nℹ️ 没有文件被重命名")
    
    # 打印失败列表
    if failed_list:
        print(f"\n❌ 失败 {len(failed_list)} 个文件:")
        for filename, reason in failed_list:
            print(f"   {filename}: {reason}")
    
    print(f"\n总计: 成功 {len(success_list)}, 失败 {len(failed_list)}")
    print("=" * 50)

def main():
    """
    主函数
    """
    try:
        # 获取用户输入
        folder_path, prefix, start_num, extensions = get_user_input()
        
        # 执行批量重命名
        success_list, failed_list = batch_rename_files(
            folder_path, prefix, start_num, extensions
        )
        
        # 打印结果
        print_results(success_list, failed_list)
        
    except KeyboardInterrupt:
        print("\n\n❌ 用户取消操作!")
    except Exception as e:
        print(f"\n\n❌ 程序发生未知错误: {str(e)}")

if __name__ == "__main__":
    main()
