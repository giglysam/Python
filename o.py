import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()


while True:
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=0.2)
        pyttsx3.speak('Listening')
        audio2 = r.listen(source2)
        MyText = r.recognize_google(audio2)
        ope = ["+", "-", "*", "/"]

        inp = MyText

        for i in inp:
            try:
                if i in ope:
                    a, b = inp.split(i)
                    a, b = int(a), int(b)

                    if i == "+":
                        pyttsx3.speak(str(a + b))
                    elif i == "-":
                        pyttsx3.speak(str(a - b))
                    elif i == "*":
                        pyttsx3.speak(str(a * b))
                    elif i == "/":
                        pyttsx3.speak(str(a / b))
            except Exception:
                pass

        if inp.__contains__('exit'):
            quit()
            break
