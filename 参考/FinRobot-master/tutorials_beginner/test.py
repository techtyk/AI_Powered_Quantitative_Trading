print("hello world!")
import warnings
from pydantic import BaseModel, ConfigDict
BaseModel.model_config = ConfigDict(protected_namespaces=()) # 移除 Pydantic 默认的 protected_namespaces（默认为 ("model_",)），以避免与 autogen 的 model_config 冲突

import os
import autogen
from textwrap import dedent
from finrobot.utils import register_keys_from_json
print("ok1")

# import sys
# sys.setprofile(lambda frame, event, arg: print(f"{event}: {frame.f_code.co_filename}"))
# from finrobot.agents.workflow import SingleAssistantShadow
# print("ok2")
# 执行from finrobot.agents.workflow import SingleAssistantShadow出现问题，需要排查可能存在的循环导入

# 分步导入
import finrobot
print("基本模块导入成功")
# import sys
# sys.setprofile(lambda frame, event, arg: print(f"{event}: {frame.f_code.co_filename}"))
import finrobot.agents
print("agents模块导入成功")

from finrobot.agents import agent_library
print("agent_library模块导入成功")

# 最后再导入workflow
from finrobot.agents import workflow
print("workflow模块导入成功")



