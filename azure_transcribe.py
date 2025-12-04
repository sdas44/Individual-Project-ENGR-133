"""
Course Number: ENGR 13300
Semester: e.g. Fall 2025

Description:
   This code contains functions to transcribe audio using Azure's Speech services. 
    

Assignment Information:
    Assignment:     Individual Project
    Team ID:        LC05 Team 5
    Author:         Samarth Das
    Date:           12/3/2025

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [X] understand the assignment expectations without
        telling me how they will approach it.
    [X] understand different ways to think about a solution
        without helping me plan my solution.
    [X] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""
import azure.cognitiveservices.speech as speechsdk
import time
from dotenv import load_dotenv
import os

load_dotenv() # used to load the environment variables

# ---- ENTER YOUR INFO HERE ----
SPEECH_KEY = os.getenv("SPEECH_KEY")
REGION = os.getenv("REGION" )  # ex: "eastus" or "westus2"
AUDIO_FILE = os.getenv("AUDIO_PATH") # path to your audio file
# ------------------------------

def transcribe_continuous_with_timeout(audio_file, timeout_seconds=20):
    """  
    This transcribes the audio file to text. It also can take a timeout.
    """
    # speech configurations
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
