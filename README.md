# 📚 SummarizeX – Multi-Source AI Summarizer

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg?style=flat&logo=Streamlit&logoColor=white)](https://archit-summarizex.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![Gemini API](https://img.shields.io/badge/Google-Gemini_API-orange.svg)](https://ai.google.dev/)
[![YouTube API](https://img.shields.io/badge/YouTube-Transcript_API-red.svg)](https://pypi.org/project/youtube-transcript-api/)

**SummarizeX** is a unified, multi-modal summarization tool designed to extract and synthesize information from various data sources. Built with Python and Streamlit, it leverages the Google Gemini LLM to generate structured, professional summaries from plain text, PDF documents, and YouTube videos.

## ✨ Key Features
- **Multi-Modal Inputs:** Seamlessly switch between processing raw text, uploading PDF files, or pasting YouTube URLs via a tabbed interface.
- **YouTube Integration:** Bypasses manual transcription by programmatically fetching video subtitles using the `youtube-transcript-api`, complete with robust error handling for disabled or missing captions.
- **Document Processing:** Extracts raw text strings from uploaded PDF buffers using `PyPDF2`, including checks for encryption and file corruption.
- **Modular Prompt Engineering:** Dynamically constructs LLM prompts to ensure outputs follow a strict structure: an **Executive Summary** followed by **Bullet-Point Key Takeaways**.
- **Customizable Granularity:** Users can dictate the verbosity of the AI's output by selecting Short, Medium, or Detailed lengths.

---

## 🛠️ Tech Stack
* **Frontend/UI:** Streamlit
* **LLM Engine:** Google Gemini API (`gemini-3.5-flash`)
* **Data Extraction:** PyPDF2, YouTube Transcript API
* **Language:** Python 3

---

## 🚀 Live Demo
Try the application live here: **[SummarizeX on Streamlit Cloud](https://archit-summarizex.streamlit.app)**

---

## 💻 Local Setup & Installation

To run this project locally, you will need a Google Gemini API Key. Get one from [Google AI Studio](https://aistudio.google.com/).

### 1. Clone the Repository
```bash
git clone https://github.com/architsingh7/SummarizeX.git
cd SummarizeX
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Launch the Streamlit server:
```bash
streamlit run app.py
```
*The application will launch automatically in your default web browser at `http://localhost:8501`.*

---

## 📂 File Structure

* `app.py`: The main Streamlit application and UI routing.
* `llm_handler.py`: Configures the Gemini API and constructs the dynamic prompt architecture.
* `pdf_handler.py`: Utility functions for securely extracting text from PDF buffers.
* `youtube_handler.py`: Utility functions for validating URLs and fetching video transcripts.
* `requirements.txt`: Project dependencies for local development and cloud deployment.

---

## 👨‍💻 Author
**Archit Singh**
* [GitHub](https://github.com/architsingh7)
* [LinkedIn](https://www.linkedin.com/in/architdeveloper/)
