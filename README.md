# Agent-RAG

<div align="center">
  <!-- Python版本（项目核心运行环境） -->
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg?style=flat-square" alt="Python Version">
  <!-- Streamlit（前端交互框架） -->
  <img src="https://img.shields.io/badge/Streamlit-1.30+-red.svg?style=flat-square" alt="Streamlit Version">
  <!-- LangChain（RAG流程核心） -->
  <img src="https://img.shields.io/badge/LangChain-0.1+-green.svg?style=flat-square" alt="LangChain Version">
  <!-- ChromaDB（向量数据库） -->
  <img src="https://img.shields.io/badge/ChromaDB-0.4+-orange.svg?style=flat-square" alt="ChromaDB Version">
  <!-- 通义千问（大模型对接） -->
  <img src="https://img.shields.io/badge/通义千问-API-yellow.svg?style=flat-square" alt="Tongyi Qwen">
  <!-- 新增：YAML（配置文件格式），贴合config目录的yml文件 -->
  <img src="https://img.shields.io/badge/配置文件-YAML-9cf.svg?style=flat-square" alt="Config Format YAML">
  <!-- 新增：SQLite（ChromaDB底层存储），贴合chroma.sqlite3文件 -->
  <img src="https://img.shields.io/badge/底层存储-SQLite-607d8b.svg?style=flat-square" alt="SQLite Storage">
</div>

<br>

一款基于 Streamlit + RAG 构建的交互式智能客服系统，专为扫地机器人场景设计，支持多会话管理、流式响应输出，具备灵活的会话创建/切换/删除能力。

## 🌟 核心特性
- 基于 RAG（检索增强生成）技术，精准匹配扫地机器人相关知识库（支持 PDF/TXT 等格式）
- Streamlit 可视化交互界面，支持多会话独立管理（创建/切换/删除）
- 流式响应输出，提升对话交互体验
- 灵活的配置化管理（Agent/Chroma/RAG/Prompt 均可通过 YAML 配置）
- 基于 Chroma DB 实现本地向量存储，保障数据隐私

## ▶️ 运行示例
![用户报告1](images/用户报告1.png)
![用户报告2](images/用户报告2.png)
![结合天气地址回答](images/结合天气地址回答.png)

## 📋 环境准备
### 1. 依赖安装
```bash
pip install -r requirements.txt  
```
### 2.配置文件说明
项目核心配置均存放于 config/ 目录：  
agent.ymll：智能体（Agent）行为配置（如思考逻辑、工具调用规则）   
{insert\_element\_1\_LSBgY2hyb21hLnlt}l：Chroma 向量数据库配置（存储路径、嵌入模型、相似度阈值）  
prompts.ymll：对话提示词模板（系统提示、用户问题引导等）   
{insert\_element\_3\_LSBgcmFnLnlt}l：RAG 流程配置（检索策略、上下文拼接规则、召回数量）  

## 🚀 快速启动
```bash
# 运行 Streamlit 应用
streamlit run app.py
```
## 📁 项目结构
```plaintext
Agent-RAG/
├── .idea/                      # PyCharm/IDEA 项目配置目录（自动生成）
│   ├── inspectionProfiles/
│   │   ├── Project_Default.xml
│   │   └── profiles_settings.xml
│   ├── .gitignore
│   ├── AI大模型RAG与智能体开发_Agent项目.iml
│   ├── misc.xml
│   └── modules.xml
├── agent/                      # Agent 智能体核心模块
│   ├── __pycache__/
│   │   ├── react_agent.cpython-310.pyc
│   │   └── react_agent.cpython-313.pyc
│   ├── chroma_db/               # Agent 内部向量库缓存
│   │   └── chroma.sqlite3
│   ├── tools/                   # 智能体工具包
│   │   ├── __pycache__/
│   │   │   ├── agent_tools.cpython-310.pyc
│   │   │   ├── agent_tools.cpython-313.pyc
│   │   │   ├── middleware.cpython-310.pyc
│   │   │   └── middleware.cpython-313.pyc
│   │   ├── agent_tools.py       # 工具实现（知识库查询/故障诊断等）
│   │   └── middleware.py        # 中间件（权限/日志/请求拦截）
│   └── react_agent.py           # ReAct 智能体核心（思考+工具调用+生成回答）
├── chroma_db/                   # 全局向量数据库目录（最终持久化存储）
│   └── chroma.sqlite3           # Chroma 向量库核心文件（存储向量化知识库）
├── config/                      # 配置文件目录
│   ├── agent.yml                # Agent 配置（思考次数/工具开关/参数设定）
│   ├── chroma.yml               # 向量库配置（路径/集合名/嵌入模型）
│   ├── prompts.yml              # 提示词模板配置（Prompt加载/拼接规则）
│   └── rag.yml                  # RAG 配置（检索数量/相似度阈值/重排序开关）
├── data/                        # 业务数据/知识库目录
│   └── external/                 # 外部原始知识库
│       ├── records.csv
│       ├── 扫地机器人100问.pdf
│       ├── 扫地机器人100问2.txt
│       ├── 扫拖一体机机器人100问.txt
│       ├── 故障排除.txt
│       ├── 维护保养.txt
│       └── 选购指南.txt
├── images/                      # 图片资源/截图（含.gitkeep 占位文件）
│   ├── .gitkeep
│   ├── 用户报告1.png
│   ├── 用户报告2.png
│   └── 结合天气地址回答.png
├── logs/                        # 日志目录
│   ├── agent_20260125.log
│   ├── agent_20260126.log
│   └── agent_20260420.log
├── model/                       # 模型工厂/实例化模块
│   ├── __pycache__/
│   │   ├── factory.cpython-310.pyc
│   │   └── factory.cpython-313.pyc
│   └── factory.py               # 模型工厂（统一创建LLM/向量库/RAG实例）
├── prompts/                     # 提示词模板文件
│   ├── main_prompt.txt          # 主提示词（定义角色/语气/回答规则）
│   ├── rag_summarize.txt        # RAG 结果总结提示词（精简知识库内容）
│   └── report_prompt.txt        # 报告生成提示词（对话总结/故障报告生成）
├── rag/                         # RAG 检索增强核心模块
│   ├── __pycache__/
│   │   ├── rag_service.cpython-310.pyc
│   │   ├── rag_service.cpython-313.pyc
│   │   ├── vector_store.cpython-310.pyc
│   │   └── vector_store.cpython-313.pyc
│   ├── chroma_db/                # RAG 模块专属向量库（实际持久化路径）
│   │   └── 6f7a4ea4-efb3-48b4-9497-3cd085a21da0/
│   │       ├── data_level0.bin
│   │       ├── header.bin
│   │       ├── length.bin
│   │       ├── link_lists.bin
│   │       └── chroma.sqlite3
│   ├── rag_service.py           # RAG 服务核心（检索知识库/拼接上下文）
│   └── vector_store.py          # 向量库操作（创建索引/存文档/查相似内容）
├── utils/                       # 通用工具类
│   ├── __pycache__/
│   │   ├── config_handler.cpython-310.pyc
│   │   ├── config_handler.cpython-313.pyc
│   │   ├── file_handler.cpython-310.pyc
│   │   ├── file_handler.cpython-313.pyc
│   │   ├── logger_handler.cpython-310.pyc
│   │   ├── logger_handler.cpython-313.pyc
│   │   ├── path_tool.cpython-310.pyc
│   │   ├── path_tool.cpython-313.pyc
│   │   ├── prompt_loader.cpython-310.pyc
│   │   └── prompt_loader.cpython-313.pyc
│   ├── config_handler.py        # 配置文件处理（读取yml/json）
│   ├── file_handler.py          # 文件处理（读取pdf/txt/csv）
│   ├── logger_handler.py        # 日志配置（自定义日志格式/输出）
│   ├── path_tool.py             # 路径工具（统一管理项目绝对路径）
│   └── prompt_loader.py         # Prompt 加载器（读取prompt文件并格式化）
├── .gitignore                    # Git 忽略规则（排除缓存/日志/环境文件）
├── LICENSE                       # 开源许可证
├── README.md                     # 项目说明（功能/启动方式/使用说明）
├── app.py                        # 项目入口（Streamlit 网页界面+对话系统）
├── md5.text                      # 文件校验文件（标记知识库是否更新）
└── requirements.txt              # 项目依赖包（python版本+第三方库）
```

## 📖 使用说明
1.将扫地机器人相关知识库文档（PDF/TXT）放入 data/external/ 目录  
2.调整 config/ 下的配置文件（按需修改向量库、RAG 策略、Agent 规则）  
3.启动应用后，在网页端即可进行多会话问答，支持切换 / 删除会话  
4.系统会自动检索知识库，结合大模型生成精准回答  
