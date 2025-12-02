# Individual-Project-ENGR-133: DONNA
![Python](https://img.shields.io/badge/python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Inference-yellow)
![Azure](https://img.shields.io/badge/Azure-Speech-blue)

My Individual Project for ENGR 133: DONNA below are instructions to run the program.

## Known Web Browser Support:
Check to make sure your chosen web browser will support this program
| Web Browser 🌀 | Support Status ☑️ |
| :-----------: | :--------------: |
| Chrome 🌐 | ✅ |
| Edge 🔵 | ✅ |
---

## 🚀 Features
- 🎤 **Record audio** directly in the browser  
- 🔊 **Azure Speech-to-Text Transcription**  
- 🧠 **LLM-powered task extraction** via HuggingFace  
- 📄 **Auto-generated to-do list JSON**  
- 🗂 **Automatic task file saving**  
- 🎨 **Modern Streamlit UI**

---

## 📥 Installation & Setup

### **Prerequisites**
- Python **3.10.11**
- HuggingFace Inference Token  
- Microsoft Azure Speech Resource  
- *(Recommended)* Virtual environment

### **Setup**
---
1. Clone the repository into your directory
``` bash
git clone https://github.com/sdas44/Individual-Project-ENGR-133.git 
```
2. Install required packages listed on the requirements.txt
```bash
pip install -r requirements.txt
```
3. Generate a HuggingFace Inference API token first, then run:
```bash
hf auth login
```

4. Create a ```.env``` file in the project root:
```python
SPEECH_KEY="KEY HERE"
REGION="REGION HERE"
AUDIO_PATH="user_audio_task.wav"
```
5. Now we can run the program.

```bash
streamlit run 1_App.py
```
## 🛠 Technologies Used

* **Python 3.10** 🐍

* **Microsoft Azure Speech Services** 💬

* **HuggingFace Inference API** 🤗

* **Streamlit** 👑

* **Pydantic** 🌊

* **Git + GitHub** 😺

## 🙌 Author

**Samarth Das**

ENGR 133 – Purdue University

GitHub: https://github.com/sdas44