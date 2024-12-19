# TranscriptYT

A Flask-based web app that extracts YouTube video transcripts, summarizes them using Google Gemini AI, and provides downloadable text and audio summaries. Utilized YouTube Transcript API, gTTS for text-to-speech, and a user-friendly interface to simplify video content processing.

---

## How to Implement This Project

Follow these steps to set up and run the **TranscriptYT** project locally:

### 1. Clone the Repository
Clone the project repository to your local machine:
```bash
git clone https://github.com/MokshithaDara/TranscriptYT.git
cd TranscriptYT

2. Set Up a Virtual Environment 

Create and activate a virtual environment to isolate dependencies:

python -m venv venv
venv\Scripts\activate

3. Install Dependencies

Install the required Python packages using pip:

pip install -r requirments.txt

4. Set Up the .env File

Create a .env file in the project root directory.
Add the following content:

GOOGLE_API_KEY=your_actual_google_api_key

Replace your_actual_google_api_key with your Google Gemini API key.

5. Run the Application

Start the Flask application:

python app.py

The application will run on http://127.0.0.1:5000/.

6. Using the Application

Open your web browser and navigate to http://127.0.0.1:5000/.
Enter the YouTube video URL and the desired settings.
Generate and download the transcript, summary, or audio file as needed.

7. Static Files and Templates

Static Files: All static assets like CSS, JS, and audio files are stored in the static/ directory.
Templates: HTML files for the app's frontend are in the templates/ directory.

8. Notes

Ensure that the GOOGLE_API_KEY is valid and has the required permissions for Google Gemini AI.
If issues arise with the YouTube Transcript API, ensure that the video has transcripts available.