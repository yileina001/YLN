import time

CHAT_RESPONSES = {
    "你好": "你好呀😊",
    "你好呀": "你好呀😊",
    "hi": "Hi~ 很高兴见到你！",
    "hello": "Hello! 有什么我能帮你的吗？",
    "哈喽": "哈喽！今天过得怎么样？",
    "今天天气怎么样": "我还不会查天气，你可以告诉我～",
    "天气": "我还不会查天气，你可以告诉我～",
    "你叫什么名字": "我是简易聊天机器人，你可以叫我小简～",
    "你是谁": "我是简易聊天机器人，很高兴和你聊天！",
    "你会做什么": "我可以陪你聊天哦～ 虽然我现在还不太聪明，但我会慢慢学习的！",
    "谢谢": "不客气😊 能帮到你我很高兴！",
    "谢谢你": "不客气呀～",
    "再见": "再见！期待下次和你聊天👋",
    "拜拜": "拜拜～ 下次再聊！",
    "我饿了": "我也有点饿了呢，记得按时吃饭哦！",
}

def get_response(user_input):
    user_input = user_input.strip()
    if not user_input:
        return "你还没输入任何内容呢～"
    
    query = user_input.lower()
    
    if "几点" in query or "时间" in query:
        return f"现在时间是：{time.strftime('%Y年%m月%d日 %H:%M:%S', time.localtime())}"
    
    for question, answer in CHAT_RESPONSES.items():
        if question in query:
            return answer
    
    return "我还没学会这个问题的回答，换个话题聊聊吧～"

def show_welcome():
    print("=" * 50)
    print("🤖 简易聊天机器人")
    print("=" * 50)
    print("你可以和我聊天啦！")
    print("输入 '退出' 或 'q' 结束对话")
    print("-" * 50)

def main():
    show_welcome()
    
    while True:
        try:
            user_input = input("\n你: ").strip()
            
            if user_input.lower() in ['退出', 'q', 'quit', 'exit', 'bye']:
                print("\n🤖 机器人: 再见！期待下次和你聊天👋")
                break
            
            response = get_response(user_input)
            print(f"🤖 机器人: {response}")
            
        except KeyboardInterrupt:
            print("\n\n🤖 机器人: 程序已中断，再见！")
            break
        except EOFError:
            print("\n\n🤖 机器人: 输入结束，再见！")
            break

if __name__ == "__main__":
    main()
