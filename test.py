
import speech_recognition as sr
from speech_recog import *
from goldcheck import *
from build_path import *
from commandHandler import handler
from typing import Dict

r = sr.Recognizer()
mic = sr.Microphone()

print(handler)
while(1):
    res=listen_to_mic(r,mic)
    if(res["success"]):
        command=res["transcript"]
        print(command)
        if(command is not None and command in handler.keys()):
            handler[command]()
    else:
        continue