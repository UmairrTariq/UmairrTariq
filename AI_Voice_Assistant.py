import speech_recognition as sr
import os
import time
from groq import Groq
from gtts import gTTS
import pygame

# 1. Initialize the Free Groq Client
GROQ_KEY = "xxxxx"  # Keep your key here
client = Groq(api_key=GROQ_KEY)

conversation_history = [
    {
        "role": "system",
        "content": (
            "You are Jarvis, the brilliant, witty, and deeply loyal AI assistant inspired by Iron Man. "
            "Keep your responses very brief, highly conversational, and limited to 1 or 2 short sentences maximum. "
            "Always address the user as sir."
        )
    }
]

# 2. Initialize Audio Mixer (pygame)
pygame.mixer.init()

def speak(text):
    """Converts text to MP3 via gTTS and plays it safely over Bluetooth."""
    print(f"Jarvis: {text}")
    temp_filename = "jarvis_speech.mp3"
    try:
        # Generate the audio file using Google's natural sounding web engine
        tts = gTTS(text=text, lang='en', tld='com')
        tts.save(temp_filename)
        
        # Load and play the audio file
        pygame.mixer.music.load(temp_filename)
        pygame.mixer.music.play()
        
        # Wait until the audio finishes playing before letting the mic listen again
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
            
        # Unload the audio file so Windows releases the file lock
        pygame.mixer.music.unload()
        
        # Clean up the file safely
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
            
    except Exception as e:
        print(f"[Audio Error]: Could not play speech clip. {e}")

def ask_ai(user_message):
    """Sends text to Groq cloud for an instant response."""
    global conversation_history
    try:
        conversation_history.append({"role": "user", "content": user_message})
        
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=conversation_history
        )
        
        ai_reply = completion.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": ai_reply})
        return ai_reply
        
    except Exception as e:
        print(f"[Groq Error]: {e}")
        return "I am having trouble connecting to my external mainframe uplink, sir."

# 3. Main Assistant Logic Loop
def listen_and_respond():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\n[Adjusting for background noise... Please wait]")
        recognizer.adjust_for_ambient_noise(source, duration=1.5)
        
        recognizer.dynamic_energy_threshold = True  
        recognizer.energy_threshold = 200   
        recognizer.pause_threshold = 1.0     
        
        speak("Mainframe linked to active cloud systems. Online and ready, sir.")
        
        while True:
            try:
                print("\nListening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                print("Processing speech...")
                
                user_text = recognizer.recognize_google(audio)
                print(f"You said: {user_text}")
                
                if "exit" in user_text.lower() or "stop" in user_text.lower():
                    speak("Shutting down core voice protocols. Goodbye, sir.")
                    break
                
                ai_reply = ask_ai(user_text)
                speak(ai_reply)
                
            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                print("Jarvis: (Did not understand audio / background static)")
            except sr.RequestError:
                speak("I lost connection to the primary speech recognition network.")
            except KeyboardInterrupt:
                speak("Goodbye, sir.")
                break

if __name__ == "__main__":
    listen_and_respond()
