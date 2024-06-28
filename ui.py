import os
import streamlit as st
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "api")
api_port = int(os.environ.get("PORT", 8080))

# Streamlit UI elements
st.title("Ask Gen AI Research Papers")

st.subheader("This application refers to the following three papers - ")
st.text("1. [Attention Is All You Need!](https://arxiv.org/abs/1706.03762)")
st.text("2. [A Mathematical Theory of Communication](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)")
st.text("3. [A Neural Probabilistic Language Model](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf)")


question = st.text_input(
    "Ask questions to the research papers that built Gen-AI",
    placeholder="What are transformers in Gen-AI and why are they so important?"
)


if question:
    url = f'http://{api_host}:{api_port}/'
    data = {"query": question}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.write("### Answer")
        st.write(response.json())
    else:
        st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")


