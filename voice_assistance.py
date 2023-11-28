import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser

def greet():
    response = "Hello! I'm your voice assistant. How can I help you today?"
    speak(response)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you repeat?")
        return get_command()

def perform_action(command):
    if "hello" in command:
        speak("Hello there!")

    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")

    elif "search" in command:
        query = command.replace("search", "").strip()
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
        speak(f"Searching the web for {query}")

    else:
        speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    greet()

    while True:
        command = get_command()
        perform_action(command)
