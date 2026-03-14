# 天气查询工具
# 功能: 查询指定城市的实时天气信息
# API: 和风天气 (https://dev.qweather.com/)
# 作者: Trae AI
# 日期: 2026-03-14

import requests
import json
import sys

# ============================ API说明 ============================
# 和风天气API使用说明:
# 1. 免费版申请地址: https://dev.qweather.com/
# 2. 注册账号 → 进入控制台 → 创建应用 → 获取API Key
# 3. 免费版限制: 
#    - 每天可调用1000次
#    - 支持全球15万个城市
#    - 并发限制: 每秒10次
#    - 支持实时天气、7天预报等
# =================================================================

# 请在这里填写你申请的API Key
API_KEY = "YOUR_API_KEY_HERE"  # 替换为你的实际API Key

# 城市代码映射 (常用城市, 更多代码可在和风天气官网查询)
CITY_CODES = {
    "北京": "101010100",
    "上海": "101020100",
    "广州": "101280101",
    "深圳": "101280601",
    "杭州": "101210101",
    "南京": "101190101",
    "成都": "101270101",
    "武汉": "101200101",
    "西安": "101110101",
    "重庆": "101040100",
    "天津": "101030100",
    "苏州": "101190401",
    "青岛": "101120201",
    "长沙": "101250101",
    "沈阳": "101070101",
}

def get_city_code(city_name):
    """
    根据城市名称获取城市代码
    参数: city_name - 城市中文名称
    返回: 城市代码 或 None
    """
    return CITY_CODES.get(city_name)

def search_city_code(city_name):
    """
    通过API查询城市代码 (如果不在预定义列表中)
    参数: city_name - 城市名称
    返回: 城市代码 或 None
    """
    url = f"https://geoapi.qweather.com/v2/city/lookup?location={city_name}&key={API_KEY}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("code") == "200" and data.get("location"):
            return data["location"][0]["id"]
    except Exception as e:
        print(f"查询城市代码时出错: {str(e)}")
    return None

def get_weather_heweather(city_code):
    """
    通过和风天气API获取实时天气
    参数: city_code - 城市代码
    返回: 天气数据字典 或 None
    """
    url = f"https://devapi.qweather.com/v7/weather/now?location={city_code}&key={API_KEY}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("code") == "200":
            now = data["now"]
            return {
                "temp": now["temp"],
                "weather": now["text"],
                "wind_dir": now["windDir"],
                "wind_scale": now["windScale"]
            }
        else:
            print(f"API返回错误: {data.get('code')}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("❌ 网络连接失败，请检查网络设置")
        return None
    except requests.exceptions.Timeout:
        print("❌ 请求超时，请稍后重试")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ 请求出错: {str(e)}")
        return None
    except json.JSONDecodeError:
        print("❌ 服务器返回数据格式错误")
        return None

def get_weather_backup(city_name):
    """
    备用天气查询接口 (中国天气网公开数据)
    参数: city_name - 城市名称
    返回: 天气数据字典 或 None
    """
    # 先尝试通过预定义列表获取城市代码
    city_code = get_city_code(city_name)
    if not city_code:
        print(f"❌ 暂不支持查询 '{city_name}' 的天气信息")
        print(f"   支持的城市: {', '.join(list(CITY_CODES.keys())[:10])}...")
        return None
    
    url = f"http://www.weather.com.cn/data/sk/{city_code}.html"
    try:
        response = requests.get(url, timeout=10)
        response.encoding = 'utf-8'
        data = response.json()
        
        if "weatherinfo" in data:
            info = data["weatherinfo"]
            return {
                "temp": info.get("temp", "N/A"),
                "weather": "请使用和风天气API获取详细天气",
                "wind_dir": info.get("WD", "N/A"),
                "wind_scale": info.get("WS", "N/A")
            }
    except Exception as e:
        print(f"❌ 备用接口查询失败: {str(e)}")
    return None

def print_weather_info(city, weather_data):
    """
    格式化输出天气信息
    参数: city - 城市名称, weather_data - 天气数据
    """
    print()
    print("=" * 50)
    print(f"🌤️ {city} 实时天气")
    print("=" * 50)
    print(f"🌡️  当前温度: {weather_data['temp']}°C")
    print(f"☁️  天气状况: {weather_data['weather']}")
    print(f"💨  风力风向: {weather_data['wind_dir']} {weather_data['wind_scale']}级")
    print("=" * 50)

def show_supported_cities():
    """显示支持的城市列表"""
    print("\n📋 支持查询的城市(部分):")
    cities = list(CITY_CODES.keys())
    for i in range(0, len(cities), 5):
        print("   " + " | ".join(cities[i:i+5]))

def main():
    """主函数"""
    print("=" * 50)
    print("🌤️  天气查询小工具")
    print("=" * 50)
    
    # 检查API Key
    if API_KEY == "YOUR_API_KEY_HERE":
        print("\n⚠️  注意: 您还未配置和风天气API Key")
        print("   程序将使用备用接口查询(功能有限)")
        print("   申请API Key请参考代码注释说明\n")
    
    while True:
        city = input("\n请输入要查询的城市名称(输入'q'退出, 'list'查看支持城市): ").strip()
        
        if city.lower() == 'q':
            print("\n👋 感谢使用天气查询工具!")
            break
        
        if city.lower() == 'list':
            show_supported_cities()
            continue
        
        if not city:
            print("❌ 城市名称不能为空!")
            continue
        
        print(f"\n🔍 正在查询 {city} 的天气信息...")
        
        # 优先使用和风天气API
        if API_KEY != "YOUR_API_KEY_HERE":
            city_code = get_city_code(city)
            if not city_code:
                city_code = search_city_code(city)
            
            if city_code:
                weather = get_weather_heweather(city_code)
            else:
                weather = None
        else:
            # 使用备用接口
            weather = get_weather_backup(city)
        
        if weather:
            print_weather_info(city, weather)
        
        # 询问是否继续
        choice = input("\n是否继续查询? (y/n): ").strip().lower()
        if choice != 'y':
            print("\n👋 感谢使用天气查询工具!")
            break

if __name__ == "__main__":
    main()
