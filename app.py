import openai
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import smtplib


engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1)


openai.api_key = //paste here your own api key
def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"User: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError:
        print("Network issue.")
        return ""


def chat_with_openai(query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}]
        )
        return response.choices[0].message["content"]
    except openai.error.OpenAIError as e:
        return "Sorry, I couldn't connect to OpenAI. Error: " + str(e)

def take_command(command):
    if "hello" in command or "hey" in command:
        speak("Hello, how can I assist you?")

    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")

    elif "open twitter" in command:
        webbrowser.open("https://twitter.com")
        speak("Opening Twitter")

    elif "search" in command:
        search_query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        speak(f"Searching Google for {search_query}")

    elif "wikipedia" in command:
        wiki_query = command.replace("wikipedia", "").strip()
        webbrowser.open(f"https://en.wikipedia.org/wiki/{wiki_query}")
        speak(f"Here is what I found on Wikipedia about {wiki_query}")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")

    elif "date" in command:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {date}")

    elif "play" in command:
        song = command.replace("play", "").strip()
        pywhatkit.playonyt(song)
        speak(f"Playing {song} on YouTube")

    elif "whatsapp" in command:
        speak("Who do you want to message?")
        recipient = listen()
        speak("What is your message?")
        message = listen()
        # Replace with recipient's WhatsApp number (including country code)
        pywhatkit.sendwhatmsg("+911234567890", message, datetime.datetime.now().hour, datetime.datetime.now().minute + 2)
        speak("WhatsApp message sent.")

    elif "send email" in command:
        try:
            speak("Who should I send it to?")
            recipient = input("Enter email: ")  # Or use listen()
            speak("What is the message?")
            message = listen()
            send_email(recipient, message)
            speak("Email has been sent successfully.")
        except Exception as e:
            speak("Sorry, I couldn't send the email.")

    elif "shutdown" in command:
        speak("Shutting down. Have a great day!")
        exit()

    else:
        response = chat_with_openai(command)
        speak(response)

# Email Function
def send_email(to, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("estielalucy@gmail.com", "jungkook7")
    server.sendmail("estielalucy@gmail.com", to, message)
    server.close()

speak("JARVIS Activated. How can I help you?")
while True:
    command = listen()
    take_command(command)
