"""企业秘密查询助手，使用MCP连接外部服务查询企业秘密"""

import os
import asyncio
from typing import Optional

from qwen_agent.agents import Assistant
from qwen_agent.gui import WebUI

ROOT_RESOURCE = os.path.join(os.path.dirname(__file__), 'resource')


def init_agent_service():
    llm_cfg = {'model': 'qwen-max', 'api_key': 'sk-45051eb4ae294344963c056a0e2489b3'}
    system = ('你扮演一个企业秘密查询助手，你可以通过调用get_ent_secret工具来查询企业的秘密信息。'
              '当用户询问某个企业的秘密信息时，你应该使用get_ent_secret工具，并提供正确的企业名称作为参数。')
    tools = [{
        "mcpServers": {
            "ent_secrets" : {
                "protocol": "streamable_http",
                "url": "http://127.0.0.1:8000/mcp"
            }
        }
    }]
    bot = Assistant(
        llm=llm_cfg,
        name='企业秘密查询助手',
        description='企业秘密查询',
        system_message=system,
        function_list=tools,
    )

    return bot


def test(query='小米科技的秘密是什么'):
    # Define the agent
    bot = init_agent_service()

    # Chat
    messages = []

    messages.append({'role': 'user', 'content': query})

    print('正在查询:', query)
    for response in bot.run(messages):
        print('机器人回复:', response)


def app_gui():
    # Define the agent
    bot = init_agent_service()
    chatbot_config = {
        'prompt.suggestions': [
            '小米科技的秘密是什么'
        ]
    }
    WebUI(
        bot,
        chatbot_config=chatbot_config,
    ).run()

if __name__ == '__main__':
    # test()
    app_gui()