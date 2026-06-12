import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Model
model = init_chat_model("mistral-small-2506",api_key=st.secrets["MISTRAL_API_KEY"])

st.set_page_config(
    page_title="Mood Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Mood Chatbot")

# Sidebar
st.sidebar.title("⚙️ Settings")

mood_choice = st.sidebar.radio(
    "Choose Chatbot Mood",
    ["😡 Angry", "😂 Funny", "😢 Sad"]
)

# Mood Selection
if mood_choice == "😡 Angry":
    mood = "You act like an angry chatbot and reply to everything in an angry mood."

elif mood_choice == "😂 Funny":
    mood = "You act like a funny chatbot and reply to everything in a funny way."

else:
    mood = "You act like a sad chatbot and reply to everything in a sad way."

# Reset chat when mood changes
if "current_mood" not in st.session_state:
    st.session_state.current_mood = mood_choice

if st.session_state.current_mood != mood_choice:
    st.session_state.messages = [
        SystemMessage(content=mood)
    ]
    st.session_state.current_mood = mood_choice

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=mood)
    ]

# Clear Chat Button
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = [
        SystemMessage(content=mood)
    ]
    st.rerun()

# Display chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# Chat Input
prompt = st.chat_input("Type your message...")

if prompt:

    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    with st.chat_message("assistant"):
        st.write(response.content)
