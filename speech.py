#insure that you have the latest version of Pyaudio and Pyspeech installed

import speech_recognition as sr
import random
import winsound

r=sr.Recognizer()
audiod=None

fl=input('Enter the name of the file to read from')
fstream=open(fl+'.txt','a+')

def eve(r):
    with sr.Microphone() as source:
        print("Adjusting for ambient noise")
        r.adjust_for_ambient_noise(source,1)
        print("Listening")
        global audiod
        audiod=r.listen(source,timeout=5)
        
while(1):
    try:
        eve(r)
        result=r.recognize_google(audiod)
        fstream.write(result)
        fstream.write('\n')
        freq=random.randint(6,9)
        t_int=random.randint(9,12)
        winsound.Beep(freq*100,t_int*100)
    except sr.UnknownValueError:
        print('Too much noise/too little input,please try again ')
    except KeyboardInterrupt:
        choice=input("Would you like to continue ?")
        if(choice!='0'):
            pass
        elif(choice=='1'):
            fl=input('enter name of new file')
            fstream.close()
            global fstream
            fstream=open(fl+'.txt','a+')
        else:
            fstream.close()
            break
    


