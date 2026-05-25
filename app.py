import streamlit as st
from pdf_handler import extract_text_from_pdf
from youtube_handler import extract_youtube_transcript
from llm_handler import generate_summary

st.set_page_config(page_title="SummarizeX", layout="wide")

st.title("SummarizeX - Multi-Source AI Summarizer")

api_key = st.sidebar.text_input("Enter Google Gemini API Key", type="password")
length_preference = st.sidebar.radio("Summary Length", ["Short", "Medium", "Detailed"])

tab1, tab2, tab3 = st.tabs(["Plain Text", "PDF Document", "YouTube URL"])

with tab1:
    text_input = st.text_area("Paste your text here:", height=200)

    if st.button("Summarize Text"):
        if not api_key:
            st.error("Please enter your API Key in the sidebar.")
        elif text_input:
            with st.spinner("Processing text..."):
                try:
                    result = generate_summary(text_input, length_preference, api_key)
                    st.markdown(result)

                    st.download_button(
                        label="Download Summary",
                        data=result,
                        file_name="SummarizeX_Text_Summary.txt",
                        mime="text/plain"
                    )
                except Exception as e:
                    st.error(f"API Error: {str(e)}")

with tab2:
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if st.button("Summarize PDF"):
        if not api_key:
            st.error("Please enter your API Key in the sidebar.")
        elif uploaded_file is not None:
            with st.spinner("Extracting and Processing..."):
                try:
                    pdf_text = extract_text_from_pdf(uploaded_file)

                    if "Error" in pdf_text:
                        st.error(pdf_text)
                    else:
                        result = generate_summary(pdf_text, length_preference, api_key)
                        st.markdown(result)

                        st.download_button(
                            label="Download Summary",
                            data=result,
                            file_name="SummarizeX_PDF_Summary.txt",
                            mime="text/plain"
                        )
                except Exception as e:
                    st.error(f"API Error: {str(e)}")

with tab3:
    yt_url = st.text_input("Enter YouTube Video URL:")

    if st.button("Summarize Video"):
        if not api_key:
            st.error("Please enter your API Key in the sidebar.")
        elif yt_url:
            with st.spinner("Fetching transcript and Processing..."):
                try:
                    transcript = extract_youtube_transcript(yt_url)

                    if "Error" in transcript:
                        st.error(transcript)
                    else:
                        result = generate_summary(transcript, length_preference, api_key)
                        st.markdown(result)

                        st.download_button(
                            label="Download Summary",
                            data=result,
                            file_name="SummarizeX_YouTube_Summary.txt",
                            mime="text/plain"
                        )
                except Exception as e:
                    st.error(f"API Error: {str(e)}")