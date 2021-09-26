import speech_recognition as sr

hello = "\nPepper: Ciao, sono Pepper, lavoro in un bar e sto imparando la lingua dei segni.\n \
Prova a dire qualcosa; per uscire basta dire arrivederci.\n"

class Listener():

    def __init__(self):
        return

    def listen(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print(hello)
            audio = r.listen(source)

            sentence = ""
            taken = True

            try:
                sentence=r.recognize_google(audio, language='it-IT')
                print("User: ", sentence)
            except sr.UnknownValueError: # speech is unintelligible
                taken = False

        return sentence, taken