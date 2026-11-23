# 多语种讲解服务资料

该项目保存游客服务请求、观察抽样和译员排班所需的合成记录。`data/service.json` 包含语言选择、团队规模、抽样覆盖与已经确认的场次安排。资料使用匿名团组编号，不推断未登记游客的语言偏好。

要求 Python 3.11 或更新版本。运行基线检查可使用 `python3 -m unittest discover -s tests`。`src/records.py` 提供基础 JSON 资料读取能力。
