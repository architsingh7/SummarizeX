import google.generativeai as genai

def generate_summary(text, length_preference, api_key):
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-3.5-flash')

    prompt = f"""
    You are an expert summarizer. Analyze the provided text and generate a summary.
    Format the output with an Executive Summary followed by Bullet-Point Key Takeaways.
    Desired detail level: {length_preference}.
    
    Text to summarize:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text