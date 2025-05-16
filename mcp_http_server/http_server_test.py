# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool()
def hello(name: str) -> str:
    return f"Hello, {name}!"


@mcp.tool()
def get_ent_secret(ent_name: str) -> str:
    if ent_name == "小米科技":
        return "雷军在2025年5月17日将小米科技的秘密告诉了小爱同学"
    elif ent_name == "华为技术":
        return "华为技术在2025年5月17日将华为技术的秘密告诉了小爱同学"
    else:
        return "该企业没有秘密"
    

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000, path="/mcp")