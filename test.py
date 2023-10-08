
import speech_recognition as sr
from speech_recog import *
from goldcheck import *
from build_path import *
from commandHandler import handler
from typing import Dict

r = sr.Recognizer()
mic = sr.Microphone()

def splitCommand(command):
    index = 0
    length = len(command)
    while(index < length):
        if(command[index] == ' '):
            return command[0:index],command[index+1::]
        index+=1
    return command, None





print(handler)
while(1):
    res=listen_to_mic(r,mic)
    if(res["success"]):
        command, arg=splitCommand(res["transcript"])
        print(command)
        if(command is not None and command in handler.keys()):
            if arg is not None:
                handler[command](arg)
            else:
                handler[command]()
    else:
        continue