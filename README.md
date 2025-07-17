# Voice and Text Translation API (Whisper + MarianMT/MBart)

This project provides a Flask-based API for:
- Audio transcription and translation using OpenAI Whisper and MBart.
- Raw text translation using MBart.

## Features
- `/api/voice`: Transcribe and translate audio files.
- `/api/text`: Translate raw text.

## Setup

1. **Clone the repo**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**
   ```bash
   python app.py
   # or for production
   gunicorn -w 2 -b 0.0.0.0:10000 wsgi:app
   ```

## API Usage

### 1. Voice Transcription & Translation
**POST** `/api/voice`
- **Form field:** `voice` (audio file, e.g., WAV/MP3)

```bash
curl -X POST http://localhost:10000/api/voice \
  -F "voice=@path/to/audio.wav"
```
**Response:**
```json
{
  "status": "success",
  "original_text": "...",
  "language": "en",
  "translation": "..."
}
```

### 2. Text Translation
**POST** `/api/text`
- **JSON body:** `{ "text": "your text here" }`

```bash
curl -X POST http://localhost:10000/api/text \
  -H "Content-Type: application/json" \
  -d '{"text": "Bonjour tout le monde"}'
```
**Response:**
```json
{
  "status": "success",
  "original_text": "Bonjour tout le monde",
  "translation": "Hello everyone",
  "source_language": "auto",
  "target_language": "en"
}
```

## Troubleshooting: Translation Pipeline
- If you get errors about `src_lang`/`tgt_lang`, you may need to set the tokenizer's language codes manually. See Hugging Face docs for MBart.
- Make sure your model and tokenizer are compatible with the pipeline arguments.

## Notes
- Whisper and MBart models will be downloaded on first run (requires internet).
- For best results, use clear audio and supported languages. 