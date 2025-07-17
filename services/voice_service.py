
import tempfile
import torch
import librosa
import soundfile as sf
import traceback
from core.whisper_loader import load_whisper_model
from services.text_service import translate_text

model = load_whisper_model()

def transcribe_audio(file):
    try:
        # Save uploaded file to a temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            file.seek(0)  # Ensure pointer is at start
            tmp.write(file.read())
            tmp.flush()
            # Now load and process the saved file
            y, sr = librosa.load(tmp.name, sr=16000)
            sf.write(tmp.name, y, sr)
            result = model.transcribe(tmp.name)
        text = result["text"].strip()
        language = result.get("language", "unknown")
        translation = translate_text(text)
        print("[TRANSLATION]", translation.get("translation", ""))
        return {
            "status": "success",
            "original_text": text,
            "language": language,
            "translation": translation.get("translation", "")
        }
    except Exception as e:
        traceback.print_exc()
        return {"status": "error", "message": str(e)}
