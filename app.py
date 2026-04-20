import time
import uuid
import datetime
import streamlit as st
from agent.react_agent import ReactAgent

# -------------------------- 初始化会话状态 --------------------------
# 初始化多会话存储（替代原单一message）
if "sessions" not in st.session_state:
    init_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    st.session_state["sessions"] = {
        "default": {
            "id": "default",
            "name": init_time,
            "messages": []
        }
    }

if "current_session_id" not in st.session_state:
    st.session_state["current_session_id"] = "default"

if "agent" not in st.session_state:
    st.session_state["agent"] = ReactAgent()

# -------------------------- 侧边栏会话管理 --------------------------
with st.sidebar:
    st.title("AI控制面板")
    st.divider()

    # 新建会话按钮
    if st.button("➕ 新建会话", use_container_width=True):
        new_session_id = str(uuid.uuid4())[:8]
        new_session_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        st.session_state["sessions"][new_session_id] = {
            "id": new_session_id,
            "name": new_session_name,
            "messages": []
        }
        st.session_state["current_session_id"] = new_session_id
        st.rerun()

    st.divider()
    st.subheader("会话历史")

    # 遍历会话（修复style参数问题，用primary类型实现高亮）
    session_ids = list(st.session_state["sessions"].keys())
    for session_id in session_ids:
        session = st.session_state["sessions"][session_id]
        is_current = session_id == st.session_state["current_session_id"]

        col1, col2 = st.columns([0.8, 0.2], gap="small")
        with col1:
            # 移除非法style参数，仅用type实现高亮（Streamlit原生支持）
            if st.button(
                    session["name"],
                    key=f"session_{session_id}",
                    use_container_width=True,
                    disabled=is_current,
                    type="primary" if is_current else "secondary"
            ):
                st.session_state["current_session_id"] = session_id
                st.rerun()

        with col2:
            if st.button(
                    "❌",
                    key=f"delete_{session_id}",
                    disabled=is_current,
                    use_container_width=True,
                    help="删除该会话"
            ):
                del st.session_state["sessions"][session_id]
                if len(st.session_state["sessions"]) == 0:
                    fallback_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    st.session_state["sessions"]["default"] = {
                        "id": "default",
                        "name": fallback_time,
                        "messages": []
                    }
                    st.session_state["current_session_id"] = "default"
                else:
                    new_current_id = list(st.session_state["sessions"].keys())[0]
                    st.session_state["current_session_id"] = new_current_id
                st.rerun()

# -------------------------- 主聊天界面 --------------------------
st.title("扫地机器人智能客服")
st.divider()

# 获取当前会话（替代原单一message）
current_session = st.session_state["sessions"][st.session_state["current_session_id"]]

# 显示当前会话的聊天记录
for message in current_session["messages"]:
    st.chat_message(message["role"]).write(message["content"])

# 用户输入处理
prompt = st.chat_input("请输入您的问题...")
if prompt:
    current_session["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response_messages = []
    with st.spinner("智能客服思考中..."):
        res_stream = st.session_state["agent"].execute_stream(prompt)


        def capture_and_stream(generator, cache_list):
            full_response = ""
            for chunk in generator:
                full_response += chunk
                cache_list.append(chunk)
                for char in chunk:
                    time.sleep(0.01)
                    yield char
            cache_list.append(full_response)


        assistant_msg = st.chat_message("assistant")
        assistant_msg.write_stream(capture_and_stream(res_stream, response_messages))

        # 修复原代码只取最后一个chunk的bug
        if response_messages:
            full_resp = response_messages[-1] if isinstance(response_messages[-1], str) else "".join(response_messages)
            current_session["messages"].append({"role": "assistant", "content": full_resp})

        st.rerun()