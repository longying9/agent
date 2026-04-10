from langchain_core.tools import tool
import requests
from tavily import TavilyClient

@tool(description="查询天气")
def get_weather(city:str)->str:
    url=f"https://wttr.in/{city}?format=j1"
    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()
        
        current=data["current_condition"][0]
        
        return current
    except Exception as e:
        return f"未知错误:{e}"
    
    
@tool(description="查询景点")
def search_place(city:str,weather:str)->str:
    tavily=TavilyClient()
    
    query=f"在{city}在{weather}天气下适合去的景点"
    try:
        response=tavily.search(query=query,seach_depth="basic",include_answer=True)
        return response["answer"]
    except Exception as e:
        return f"未知错误:{e}"
@tool(description="讲笑话")
def say_jokes()->str:
    url="https://v2.jokeapi.dev/joke/Any?type=single"
    response=requests.get(url=url)
    joke=response.json()["joke"]
    return joke
    
# if __name__=="__main__":
#     res=say_jokes()
#     print(res)