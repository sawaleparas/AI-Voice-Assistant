# AI Voice Assistant (Jarvis-like) by Paras Sawale

import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import openai
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # Speed of speech
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Female voice (optional)

# Function to make the assistant speak
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Function to listen to user input using microphone
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
    except Exception as e:
        speak("Sorry, I didn't catch that. Please say it again.")
        return ""
    return query.lower()

# Function to get smart replies from OpenAI
def ask_openai(question):
    openai.api_key = "[09:27, 04/04/2025] Paras Sawale: sawaleparas
[09:44, 04/04/2025] Paras Sawale: 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"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message["content"]
        return answer.strip()
    except Exception as e:
        return "Sorry, I couldn't reach OpenAI right now."

# Main function that runs the assistant
def run_jarvis():
    speak("Hello, I am your assistant. How can I help you today?")
    
    while True:
        query = take_command()

        if "exit" in query or "quit" in query or "stop" in query:
            speak("Goodbye! Have a great day.")
            break

        elif "open youtube" in query:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")

        elif "open notepad" in query:
            speak("Opening Notepad...")
            os.system("notepad.exe")

        elif "time" in query:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {now}")

        elif "date" in query:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")

        elif query:
            # Fallback to OpenAI for smart replies
            speak("Let me think...")
            response = ask_openai(query)
            speak(response)

if __name__ == "__main__":
    run_jarvis()
