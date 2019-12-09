import speech_recognition as sr
string = ""

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say smt:")
        audio = r.listen(source)    
    try:
        string = r.recognize_google(audio, language="ru-RU")
        print(string)
    except sr.UnknownValueError:
        print("Dont understand")
    except sr.RequestError as e:
        print("Error; {0}".format(e))
