import whisper
import torch
from config import WHISPER_MODEL

def load_whisper_model():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = whisper.load_model(WHISPER_MODEL, device=device)
    return model
