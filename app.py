from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import os
from gtts import gTTS
import re

# Load environment variables
load_dotenv()

# Configure Google Gemini Pro API key
genai.configure(api_key="AIzaSyD84go_2MuTSk6Hgzg-XnmfHf_Sh-vG7TM")
# Initialize Flask app
app = Flask(__name__)

# Prompt for summarization
prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """

def extract_transcript_details(youtube_video_url, language="en"):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        transcript_text = " ".join([item["text"].replace('\n', ' ') for item in transcript_list])
        transcript_paragraphs = " ".join([item["text"].replace('\n', ' ') for item in transcript_list])
        return transcript_text, transcript_paragraphs
    except Exception as e:
        raise e

def generate_gemini_content(transcript_text, prompt, max_length):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    summary = response.text
    return " ".join(summary.split()[:max_length])

def clean_text_for_tts(text):
    clean_text = re.sub(r'\*', '', text)
    clean_text = re.sub(r'\s*[,;:.]\s*', ', ', clean_text)
    return clean_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        youtube_url = request.form['youtube_url']
        language = request.form['language']
        max_length = int(request.form['max_length'])

        try:
            transcript_text, transcript_paragraphs = extract_transcript_details(youtube_url, language)
            summary = generate_gemini_content(transcript_text, prompt, max_length)

            # Ensure the static directory exists
            if not os.path.exists('static'):
                os.makedirs('static')

            # Save the summary and transcript to files
            with open('static/summary.txt', 'w') as file:
                file.write(summary)
            
            with open('static/transcript.txt', 'w') as file:
                file.write(transcript_paragraphs)

            clean_summary = clean_text_for_tts(summary)
            tts = gTTS(clean_summary, lang=language)
            tts.save('static/summary.mp3')

            return render_template('result.html', summary=summary)
        except Exception as e:
            return str(e)
    else:
        try:
            with open('static/summary.txt', 'r') as file:
                summary = file.read()
            return render_template('result.html', summary=summary)
        except Exception as e:
            return str(e)

@app.route('/transcript')
def transcript():
    try:
        with open('static/transcript.txt', 'r') as file:
            transcript = file.read().replace('\n', ' ')  # Remove line breaks
        return render_template('transcript.html', transcript=transcript)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
