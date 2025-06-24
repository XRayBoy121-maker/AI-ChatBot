from google import genai
import speech_recognition as sr
import functions as fun
while True:
    print("1.Text")
    print("2.Audio")
    print("3.End")
    choice=input("Enter choice:")
    if(choice=="Text"):
        text=fun.type()
        fun.generate(text)
    elif(choice=="Audio"):
        text=fun.listen()
        fun.generate(text)
    elif(choice=="End"):
        break