import streamlit as st
from utils.api import summarize_text

st.set_page_config(
    page_title ="LLM Text Summarizer",
    layout= "centered"
)

st.title("LLM Text Summarizer")
st.markdown("Summarize text using an AI-powered model with different levels of detail.")
st.markdown("---")

#Text Area
user_input = st.text_area("Enter your text here:", height=250, placeholder="Paste your paragraph here...")

summary_type = st.selectbox(
    "Select Summary Type",
    ["Short", "Medium", "Detailed"]
)

if st.button("Generate Summary"):
    if user_input.strip()=="":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating summary..."):
            summary = summarize_text(user_input, summary_type)
            st.markdown("---")
            st.success("Summary Generated")

            st.subheader("Summary:")
            st.write(summary)

            
