import streamlit as st
from PIL import Image

st.set_page_config(page_title="ali's AI Portfolio", layout="wide")

st.title("👋 Hi, I'm ali  — AI & Chatbot Developer")

st.markdown("""
I’m a student of Artificial Intelligence with hands-on experience building real AI chatbot apps using Streamlit,chainlit, Python, and APIs like groq , gemini , openai , OpenRouter & ChatGPT.

Here are some of my projects you can try out:
""")

st.header("📌 Projects")

# --- Project 1 ---
st.subheader("🤖 FAQ Chatbot for Websites")
st.write("A chatbot that answers frequently asked questions using OpenRouter API. Hosted on Streamlit Cloud.")
st.markdown("[🔗 Live Demo](https://faqschatbotpy-dhsl59aluzpf4t98xsybqr.streamlit.app/)")
st.markdown("[💻 GitHub Repo](https://github.com/aliomershah/)")


# Add thumbnail
from PIL import Image
image = Image.open("A_thumbnail_graphic_for_an_AI_FAQ_Chatbot_project_.png")
st.image(image, caption="AI FAQ Chatbot Thumbnail", use_container_width=True)


st.divider()

# --- Add more projects here ---
# st.subheader("🧠 PDF Chatbot")
# ...

st.header("🙋 About Me")
st.markdown("""
- 🎓 Artificial Intelligence student
- 🧠 Passionate about real-world AI tools
- 💬 Chatbot developer using Python + APIs
- 🚀 Available for freelance work (Fiverr & Upwork)
""")

st.header("📬 Contact")
st.markdown("""
- 📧 Email: alihamzaoficall@gmail.com
- 💼 [Fiverr Profile](https://www.fiverr.com/alihamzaoficall)
- 🧑‍💻 [Upwork Profile](https://www.upwork.com/freelancers/alihamzaoficall)
""")
