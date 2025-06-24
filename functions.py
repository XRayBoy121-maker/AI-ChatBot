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
                return text


def type():
        print("What can I help you with?")
        text=input("Enter Your Question:")
        return text

client = genai.Client(api_key="AIzaSyCmNV85KlEdqiS-w-23H9RQSikfJfMFZDo")

def generate(input):
    
        response = client.models.generate_content(model="gemini-2.0-flash",contents= input)   

        print("User:",input)
        print("AI_BOT:",response.text)