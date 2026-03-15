import sys
sys.path.insert(0, '.')
from weather_query import get_weather_backup

print("=== 多城市测试 ===")
for city in ['北京', '广州', '深圳']:
    print(f"\n测试 {city}...")
    result = get_weather_backup(city)
    if result:
        print(f"  温度: {result['temp']}°C, 风力: {result['wind_dir']} {result['wind_scale']}级")
    else:
        print("  查询失败")
print("\n=== 测试完成 ===")
