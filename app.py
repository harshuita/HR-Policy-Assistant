import streamlit as st
from hr_assistant.pipeline import build_hr_assistant


st.set_page_config(
    page_title="HR Policy Assistant",
    page_icon="🤖",
    layout="centered"
)


# -----------------------------
# LOAD ASSISTANT
# -----------------------------

@st.cache_resource
def load_assistant():
    return build_hr_assistant()


if "messages" not in st.session_state:
    st.session_state.messages = []

if "assistant" not in st.session_state:
    with st.spinner("Loading HR Assistant..."):
        st.session_state.assistant = load_assistant()


# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:
    st.title("🤖 HR Assistant")

    st.write("Ask questions about company HR policies.")

    st.divider()

    st.subheader("Topics")
    st.write("""
    - 🏖️ Annual leave
    - 🏠 Work from home
    - 📅 Notice periods
    - 🕐 Working hours
    - 🏥 Benefits
    - 💰 Compensation
""")

    st.divider()

    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()


# -----------------------------
# MAIN PAGE
# -----------------------------

st.title("🤖 HR Policy Assistant")

st.write(
    "Ask questions about company policies and get answers "
    "based on your HR documents."
)

st.divider()


# -----------------------------
# CHAT HISTORY
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# -----------------------------
# INPUT
# -----------------------------

question = st.chat_input("Ask about HR policies...")


# -----------------------------
# PROCESS QUESTION
# -----------------------------

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching HR policies..."):

            try:
                answer = st.session_state.assistant.invoke(
                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": question
                            }
                        ]
                    }
                )

                if isinstance(answer, dict) and "messages" in answer:

                    final_message = answer["messages"][-1]

                    if hasattr(final_message, "content"):
                        response = final_message.content
                    else:
                        response = str(final_message)

                else:
                    response = str(answer)

                st.write(response)

            except Exception as e:

                response = "Sorry, I encountered an error."

                st.error(response)
                st.caption(f"Error: {e}")

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })