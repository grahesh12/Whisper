
from googletrans import Translator

translator = Translator()

def translate_text(text):
    try:
        translated = translator.translate(text, dest='en')
        return {
            'status': 'success',
            'original_text': text,
            'translation': translated.text,
            'source_language': translated.src,
            'target_language': 'en'
        }
    except Exception as e:
        return {'status': 'error', 'message': str(e), 'original_text': text}
    