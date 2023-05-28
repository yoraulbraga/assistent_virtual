import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()
velocidade = 210
engine.setProperty('rate', velocidade)
r = sr.Recognizer()

with sr.Microphone() as source:
    engine.say("Olá, sou a Kat, em que posso ajudar?")
    engine.runAndWait()
    audio = r.listen(source)
try:
    texto = r.recognize_google(audio, language='pt-BR')
    # print(f'Você disse {texto}')
    if "Quem é você".capitalize():
        engine.say("Como uma IA pessoal desenvolvida por Raul Lopes, minha função principal"
                   " é auxiliar na execução de tarefas e fornecer informações relevantes. "
                   "Estou aqui para responder suas perguntas, fornecer suporte e ajudar no que for possível. "
                   "Sinta-se à vontade para me fazer qualquer pergunta ou solicitar assistência com as tarefas que "
                   "precisar realizar. Estou aqui para ajudar!")
        engine.runAndWait()
except sr.UnknownValueError:
    print("Não foi possivel reconhecer o audio.")
except sr.RequestError as e:
    print("Erro ao fazer a solicitação ao serviço de reconhecimento de fala: {0}".format(e))
