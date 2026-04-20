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
├── .gitignore                # 忽略不需要提交的文件（缓存、日志、环境文件等）
├── LICENSE                   # 开源许可证，说明项目使用权限
├── README.md                 # 项目说明文档：介绍项目功能、启动方式、使用说明
├── app.py                    # 项目主入口，Streamlit 网页界面 + 对话系统启动文件
├── md5.text                  # 文件校验/缓存标记文件，用于判断知识库是否更新
├── model/
│   └── factory.py            # 模型工厂：统一创建 LLM、向量库、RAG 等模型实例
├── agent/
│   ├── react_agent.py        # ReAct 智能体核心：思考、调用工具、生成回答
│   ├── chroma_db/            # Agent 内部使用的向量库缓存目录
│   └── tools/                # 智能体工具包：如知识库查询、故障诊断、指令解析
├── .idea/                    # PyCharm/IDEA 编辑器配置文件夹（开发环境自动生成）
├── config/
│   ├── agent.yml             # 智能体配置：思考次数、工具开关、行为参数
│   ├── chroma.yml            # 向量库配置：路径、集合名、嵌入模型
│   ├── prompts.yml           # 提示词模板配置：加载哪些 prompt、如何拼接
│   └── rag.yml               # RAG 配置：检索数量、相似度阈值、重排序开关
├── rag/
│   ├── rag_service.py        # RAG 服务核心：检索知识库、拼接上下文
│   ├── vector_store.py       # 向量库操作：创建索引、存入文档、查询相似内容
│   └── chroma_db/            # RAG 模块自己的向量库存储目录
├── chroma_db/                # 项目全局向量库目录（最终持久化位置）
│   └── chroma.sqlite3        # Chroma 向量数据库文件（知识库向量化后存在这里）
├── prompts/
│   ├── main_prompt.txt       # 主提示词：定义机器人身份、语气、回答规则
│   ├── rag_summarize.txt     # RAG 结果总结提示词：让模型根据知识库精简回答
│   └── report_prompt.txt     # 报告生成提示词：用于生成对话总结/故障报告
├── data/
│   └── external/             # 外部知识库目录：放扫地机器人说明书、文档、资料
├── utils/                    # 工具函数文件夹：日志、文件处理、字符串格式化等
└── logs/                     # 日志目录：保存系统运行日志、对话记录、错误信息
```

## 📖 使用说明
1.将扫地机器人相关知识库文档（PDF/TXT）放入 data/external/ 目录  
2.调整 config/ 下的配置文件（按需修改向量库、RAG 策略、Agent 规则）  
3.启动应用后，在网页端即可进行多会话问答，支持切换 / 删除会话  
4.系统会自动检索知识库，结合大模型生成精准回答  
