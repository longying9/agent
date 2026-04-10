from langchain_community.chat_models import ChatTongyi
from langchain.agents import create_agent
from tools import get_weather,search_place,say_jokes


agent = create_agent(
    model=ChatTongyi(model="qwen-plus"),
    tools=[get_weather,search_place,say_jokes],
    system_prompt="你是一个善于提取信息的天气助手",
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "请你查询上海的天气如何，并为我推荐一个景点，附带一个笑话",
            }
        ]
    }
)

print(response["messages"][-1].content, type(response))
# for message in response["messages"]:
#     if message.__class__.__name__ == "AIMessage":
#         print(message)
#         print("="*20)
