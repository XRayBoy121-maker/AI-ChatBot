from google import genai
import speech_recognition as sr
recognizer = sr.Recognizer()
def listen(timeout_seconds=5):
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Adjusting for ambient noise... Please wait.")
                print("Please say something")
                print(f"(Waiting up to {timeout_seconds} s for speech to start )")
                audio = recognizer.listen(source, timeout=timeout_seconds)
                print("Got It Thank You")
                text=recognizer.recognize_google(audio)
                print(text)
listen()