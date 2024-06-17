import speech_recognition as sr
import pyttsx3
import wikipediaapi
import wolframalpha
import requests

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# WolframAlpha API key
wolfram_api_key = 'YOUR_WOLFRAM_API_KEY'  # Replace with your WolframAlpha API key
wolfram_client = wolframalpha.Client(wolfram_api_key)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture audio and recognize speech."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return None

def query_wikipedia(query):
    """Search Wikipedia for a query."""
    results = wikipedia.search(query)
    if results:
        try:
            page = wikipedia.page(results[0])
            return page.summary
        except wikipedia.DisambiguationError as e:
            return wikipedia.page(e.options[0]).summary
    return "No results found on Wikipedia."

def query_wolframalpha(query):
    """Query WolframAlpha for a response."""
    try:
        res = wolfram_client.query(query)
        return next(res.results).text
    except:
        return "No results found on WolframAlpha."

def main():
    """Main function to run the voice assistant."""
    speak("Hello Neha! How can I assist you today?")
    while True:
        query = listen()
        if query is None:
            continue
        if "exit" in query or "bye" in query:
            speak("Goodbye!")
            break
        elif "wikipedia" in query:
            query = query.replace("wikipedia", "")
            summary = query_wikipedia(query)
            speak(summary)
        elif "wolframalpha" in query:
            query = query.replace("wolframalpha", "")
            answer = query_wolframalpha(query)
            speak(answer)
        else:
            speak("I can search Wikipedia and WolframAlpha. Please ask something related to those services.")

if __name__ == "__main__":
    main()
