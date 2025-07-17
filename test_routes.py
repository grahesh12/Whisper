import requests

# URL of your deployed or local server
BASE_URL = "http://192.168.224.141:10000"

def test_voice_transcription(file_path):
    print("\n🔊 Testing /api/voice")
    with open(file_path, "rb") as audio:
        response = requests.post(
            f"{BASE_URL}/api/voice",
            files={"voice": audio}
        )
    print("Status Code:", response.status_code)
    print("Response:", response.json())

def test_text_translation(text):
    print("\n📝 Testing /api/text")
    response = requests.post(
        f"{BASE_URL}/api/text",
        json={"text": text}
    )
    print("Status Code:", response.status_code)
    print("Response:", response.json())

if __name__ == "__main__":
    # ✅ Replace with the path to your test audio file (e.g., 'sample.wav')
    test_voice_transcription(r"C:\Users\Grahesh\Downloads\ttsmaker-file-2025-7-11-15-7-41.mp3")

    # ✅ Replace with the text you want to translate
    test_text_translation("Bonjour, comment allez-vous ?")
