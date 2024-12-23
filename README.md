# TranscriptYT

**TranscriptYT** is a Flask-based web application that extracts YouTube video transcripts, summarizes them using Google Gemini AI, and provides downloadable text and audio summaries. It utilizes the YouTube Transcript API, gTTS for text-to-speech, and a user-friendly interface to simplify video content processing.

## Features
- Extract transcripts from YouTube videos.
- Summarize video content using Google Gemini AI.
- Provide downloadable text and audio summaries.
- User-friendly interface for easy video content processing.

---

## How to Implement This Project

### 1. Clone the Repository
Clone the project repository to your local machine:

```bash
git clone https://github.com/MokshithaDara/TranscriptYT.git
cd TranscriptYT
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment to isolate dependencies:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Set Up the `.env` File

Create a `.env` file in the project root directory and add the following content:

```
GOOGLE_API_KEY=your_actual_google_api_key
```

Replace `your_actual_google_api_key` with your actual Google Gemini API key.

### 5. Run the Application

Start the Flask application:

```bash
python app.py
```

The application will run on `http://127.0.0.1:5000/`.

### 6. Using the Application

- Open your web browser and navigate to `http://127.0.0.1:5000/`.
- Enter the YouTube video URL and the desired settings.
- Generate and download the transcript, summary, or audio file as needed.

### 7. Static Files and Templates

- **Static Files**: All static assets like CSS, JS, and audio files are stored in the `static/` directory.
- **Templates**: HTML files for the app's frontend are in the `templates/` directory.

### 8. Notes

- Ensure that the `GOOGLE_API_KEY` is valid and has the required permissions for Google Gemini AI.
- If issues arise with the YouTube Transcript API, ensure that the video has transcripts available.

---

## How to Update and Push Changes to GitHub

### 1. Stage Changes

Make the required changes to the project files. After editing, add the changes to the staging area:

```bash
git add .
```

### 2. Commit Changes

Commit the changes with an appropriate message:

```bash
git commit -m "Description of changes made"
```

### 3. Push Changes

Push the changes to the repository:

```bash
git push origin main  # Replace 'main' with the branch name if it's different
```

---

## Contributing

Feel free to submit pull requests or report issues to help improve this project.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For questions or feedback, please contact the project owner.
