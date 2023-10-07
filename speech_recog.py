import speech_recognition as sr
from typing import Dict, List

def listen_to_mic(r: sr.Recognizer, mic: sr.Microphone) -> Dict:
    with sr.Microphone() as source:
        print("say something")
        r.adjust_for_ambient_noise(source,timeout = 5, phrase_time_limit = 0.3)
        audio = r.listen(source)

    #initialize return value
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
