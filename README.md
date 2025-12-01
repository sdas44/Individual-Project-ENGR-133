# Individual-Project-ENGR-133: DONNA AI
My Individual Project for ENGR 133: DONNA AI below are instructions to run the program.

## Known Web Browser Support:
Check to make sure your chosen web browser will support this program
| Web Browser 🌀 | Support Status ☑️ |
| :-----------: | :--------------: |
| Chrome 🌐 | ✅ |
| Edge 🔵 | ✅ |

## Program Installation
**Disclaimer: This Program was run on Python 3.10.11. Its recommended to use a virtual environment when running this program.**
1. Clone the repository into your directory
``` 
git clone https://github.com/sdas44/Individual-Project-ENGR-133.git 
```
2. Install required packages listed on the requirements.txt
```
pip install -r requirements.txt
```
3. Its important to create a Huggingface Inference Model Token in order for this to work. Ensure that the huggingface inference token is created then run the following command in the terminal.
```
hf auth login #enter created token here
```

4. Finally we must create a Microsoft Azure Speech Service. Once created create a .env file and within it write:
```
SPEECH_KEY="KEY HERE"
REGION="REGION HERE"
AUDIO_PATH="user_audio_task.wav"
```
5. Now we can run the program.

```
streamlit run 1_App.py
```

# YOU ARE DONE !