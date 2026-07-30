import streamlit as st
import google.generativeai as genai


# ---------------- CONFIG ----------------

st.set_page_config(
    page_title="AI Career Navigator",
    page_icon="🚀",
    layout="centered"
)


# ---------------- DARK THEME CSS ----------------

st.markdown("""
<style>

.stApp {
    background-color: #0e1117;
    color: white;
}

h1 {
    color: #58a6ff;
    text-align: center;
}

.subtitle {
    text-align:center;
    color:#9da7b3;
    font-size:18px;
}

.chat-box {
    background-color:#161b22;
    padding:20px;
    border-radius:15px;
    margin-bottom:15px;
    border:1px solid #30363d;
}

.user {
    color:#58a6ff;
    font-weight:bold;
}

.ai {
    color:#3fb950;
    font-weight:bold;
}

textarea {
    background-color:#161b22 !important;
    color:white !important;
}

</style>
""", unsafe_allow_html=True)



# ---------------- API KEY ----------------

API_KEY = "your_api_key_here"  # Replace with your actual API key

genai.configure(api_key=API_KEY)


# ---------------- SYSTEM PROMPT ----------------

SYSTEM_PROMPT = """
You are CareerAI, an expert technology career mentor specializing in
Artificial Intelligence, Software Engineering, and emerging technologies.

Your responsibilities:
- Analyze user's skills and career goals.
- Create personalized career roadmaps.
- Identify skill gaps.
- Recommend AI projects and technologies.
- Guide students toward AI Engineering careers.

Rules:
- Give realistic and practical advice.
- Do not guarantee jobs.
- Avoid generic advice.
- Maintain a professional and supportive tone.
- For unrelated questions, politely redirect users toward career guidance.
"""


model = genai.GenerativeModel(
    model_name="gemini-2.5-flash-lite",
    system_instruction=SYSTEM_PROMPT
)



# ---------------- UI ----------------


st.markdown(
"""
<h1>🚀 AI Career Navigator</h1>
<p class="subtitle">
Personalized AI Career Guidance Assistant
</p>
""",
unsafe_allow_html=True
)


st.divider()


if "messages" not in st.session_state:
    st.session_state.messages = []



# Display previous messages

for message in st.session_state.messages:

    if message["role"] == "user":
        st.markdown(
        f"""
        <div class="chat-box">
        <span class="user">You:</span><br>
        {message["content"]}
        </div>
        """,
        unsafe_allow_html=True
        )

    else:
        st.markdown(
        f"""
        <div class="chat-box">
        <span class="ai">CareerAI:</span><br>
        {message["content"]}
        </div>
        """,
        unsafe_allow_html=True
        )



# Input box

user_input = st.chat_input(
    "Ask CareerAI about your career roadmap..."
)



if user_input:


    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )


    with st.spinner("CareerAI is thinking... 🚀"):

        response = model.generate_content(user_input)

        answer = response.text



    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )


    st.rerun()