# import streamlit as st
# from agent1 import chat_step

# st.title("Career Guiding Chatbot")
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# if "completed" not in st.session_state:
#     st.session_state.completed = False
# #printing chat
# for msg in st.session_state.messages:
#     if msg["role"] != "system":
#         with st.chat_message(msg["role"]):
#             st.write(msg["content"])

# if len(st.session_state.messages) == 0:
#     messages, response, completed = chat_step(st.session_state.messages)
#     st.session_state.messages = messages
#     st.session_state.completed = completed
#     with st.chat_message("assistant"):
#         st.write(response)

# if not st.session_state.completed:
#     user_input = st.chat_input("Your answer...")

#     if user_input:
#         st.session_state.messages.append({
#             "role": "user",
#             "content": user_input
#         })
#         with st.chat_message("user"):
#             st.write(user_input)
#         messages, response, completed = chat_step(st.session_state.messages)
#         st.session_state.messages = messages
#         st.session_state.completed = completed
#         with st.chat_message("assistant"):
#             st.write(response)

import streamlit as st
from agent1 import chat_step

st.title("Career Guiding Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "completed" not in st.session_state:
    st.session_state.completed = False

if "step" not in st.session_state:
    st.session_state.step = 0

for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

if len(st.session_state.messages) == 0:
    messages, response, completed, step = chat_step(
        st.session_state.messages,
        st.session_state.step
    )
    st.session_state.messages = messages
    st.session_state.completed = completed
    st.session_state.step = step

    with st.chat_message("assistant"):
        st.write(response)

if not st.session_state.completed:
    user_input = st.chat_input("Your answer...")

    if user_input:
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message("user"):
            st.write(user_input)

        messages, response, completed, step = chat_step(
            st.session_state.messages,
            st.session_state.step
        )
        st.session_state.messages = messages
        st.session_state.completed = completed
        st.session_state.step = step

        with st.chat_message("assistant"):
            st.write(response)