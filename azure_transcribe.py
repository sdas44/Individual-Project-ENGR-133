import azure.cognitiveservices.speech as speechsdk
import time
from dotenv import load_dotenv
import os

load_dotenv()

# ---- ENTER YOUR INFO HERE ----
SPEECH_KEY = os.getenv("SPEECH_KEY")
REGION = os.getenv("REGION" )  # ex: "eastus" or "westus2"
AUDIO_FILE = os.getenv("AUDIO_PATH") # path to your audio file
# ------------------------------

def transcribe_continuous_with_timeout(audio_file, timeout_seconds=20):
    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        region=REGION
    )
    audio_config = speechsdk.AudioConfig(filename=audio_file)

    recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config
    )

    full_transcript = []

    # When text is recognized, add it to the list
    def recognized(evt):
        if evt.result.text:
            full_transcript.append(evt.result.text)

    recognizer.recognized.connect(recognized)

    # Start recognition
    recognizer.start_continuous_recognition()
    print("Transcribing... (will stop after 20 seconds)")

    # Run for the given timeout
    start_time = time.time()
    while time.time() - start_time < timeout_seconds:
        time.sleep(0.1)

    # Stop recognition
    recognizer.stop_continuous_recognition()
    print("Stopped transcription.")

    # Join all segments into one string
    final_text = " ".join(full_transcript)
    return final_text


# ---- Run it ----
