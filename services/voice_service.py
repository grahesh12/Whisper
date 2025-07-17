
import tempfile
import torch
import librosa
import soundfile as sf
from core.whisper_loader import load_whisper_model
from services.text_service import translate_text

model = load_whisper_model()

def transcribe_audio(file):
    try:
        # Save uploaded file to temp WAV file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            y, sr = librosa.load(file, sr=16000)
            sf.write(tmp.name, y, sr)
            # Use whisper's transcribe method
            result = model.transcribe(tmp.name)
        text = result["text"].strip()
        language = result.get("language", "unknown")
        # Translate to English
        translation = translate_text(text)
        return {
            "status": "success",
            "original_text": text,
            "language": language,
            "translation": translation.get("translation", "")
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
