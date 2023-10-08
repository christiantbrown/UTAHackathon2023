import speech_recognition as sr
from typing import Dict, List

r = sr.Recognizer()
mic = sr.Microphone()

def listen_to_mic(r: sr.Recognizer, mic: sr.Microphone) -> Dict:
    with sr.Microphone() as source:
        #print("say something")
        r.adjust_for_ambient_noise(source, duration=0.1)
        audio = r.listen(source, phrase_time_limit=1)
    result = {"success": True, "error": None, "transcript": None}

    try:
        #using google speec recog to translate voice to text
        result["transcript"] = r.recognize_google(audio).lower()
        #clean up audio
        result["transcript"] = result["transcript"].replace("-", " ")
        result["transcript"] = result["transcript"].replace("/", " ")
        result["transcript"] = result["transcript"].replace("\\", " ")
    
    except sr.RequestError:
        result["success"] = False
        result["error"] = "Error with voice recognition"
    except sr.WaitTimeoutError:
        result["success"] = False
        result["error"] = "Timeout error"
    except sr.UnknownValueError:
        result["success"] = False
        result["error"] = "Response not recognized"

    #returns the msg with either a transcript if successful, or errors if error happened
    return result
