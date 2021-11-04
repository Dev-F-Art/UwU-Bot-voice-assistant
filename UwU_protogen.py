import random
import nltk
import os
import BotConfig
import information_window
from gtts import gTTS
import speech_recognition as sr
import pygame as pg
import wx

BOT_CONFIG = BotConfig.BotConfigDictionary
failure_phrases = BotConfig.FailurePhases

mood_pp = BotConfig.povod_mood_plus
mood_pm = BotConfig.povod_mood_minus

import webbrowser

command_inet = 'найди'
command_exit = 'выход'
mood = 100
ab = ''

def mood_analiz(text):
    if text in mood_pp:
        return 1
   
    if text in mood_pm:
        return 2

        
def filter_bazara(text):
    text = text.lower()
    text = [c for c in text if c in 'абвгдеёжзийклмнопрстуфхцчшщъьэюя- ']
    text = ''.join(text)
    
    return text

def find_on_inet(text):
    webbrowser.open('https://yandex.ru/search/?lr=11196&clid=1923033&text=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&src=' + text)

def listen_command(text):
    if command_inet in text:
        text.lower()
        find_on_inet(text.replayce('бот найди', ' '))
    if command_exit in text:
        exit()

# ----------------------------------------------------------------------------

with open(u"dialogues.txt", 'r') as f:
    content = f.read()

dialogues = [dialogue_line.split('\n') for dialogue_line in content.split('\n\n')]

questions = set()
qa_dataset = []

for replicas in dialogues:
    if len(replicas) < 2:
        continue
    
    question, answer = replicas[:2]
    question = filter_bazara(question[2:])
    answer = answer[2:]
    
    if question and question not in questions:
        questions.add(question)
        qa_dataset.append([question, answer])
# ----------------------------------------------------------------------------

def get_intent(question):
    for intent, intent_data in BOT_CONFIG['intents'].items():
        for example in intent_data['examples']:
            dist = nltk.edit_distance(question, example)
            dist_percentage = dist / len(question)
            if dist_percentage < 0.2:
                return intent
            
def get_ansver_by_intent(intent):
    if intent in BOT_CONFIG['intents']:
        phrases = BOT_CONFIG['intents'][intent]['responses']
        
        return random.choice(phrases)

def get_ansver_by_text(text):
    text = filter_bazara(text)
    
    for question, answer in qa_dataset:
        dist = nltk.edit_distance(question, text)
        if dist / len(question) < 0.4:
            return answer

def get_failure_phrases():
    phrases = random.choice(failure_phrases)
    return phrases

def Bot(question):
       
   intent = get_intent(question)
    
   if intent:
       ansver = get_ansver_by_intent(intent)
       if ansver:
            return ansver
    
   ansver = get_ansver_by_text(question)
   if ansver:
        return ansver
    
   ansver = get_failure_phrases()
   return ansver

#-----------------------------------------------------------------------------------
class UwU_GUI(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(800, 620))

        panelka = wx.Panel(self)
        panelka.SetBackgroundColour('#474A51')

        self.dialog_text = wx.TextCtrl(panelka, style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.dialog_text.SetForegroundColour('#42F0F8')
        self.dialog_text.SetBackgroundColour('Black')

        self.ava = wx.StaticBitmap( panelka, 1, wx.Bitmap(u'C:\\Users\\123\\Desktop\\UwU_protogen_assisteant\\UwU_image\\ava_funny.bmp'),size=(200, 200) )

        bmp = wx.Image('C:\\Users\\123\\Desktop\\UwU_protogen_assisteant\\UwU_image\\microphone_active.bmp', wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        
        btn_listen = wx.BitmapButton(panelka, -1, bmp)
        btn_listen.SetBackgroundColour('#474A51')
        btn_listen.Bind(wx.EVT_BUTTON, self.uwu_listen)

        inf_btn = wx.Button(panelka, -1, label='About me')
        inf_btn.Bind(wx.EVT_BUTTON, information_window.create_inf_window)
        inf_btn.SetBackgroundColour('#42F0F8')
        
        lbl = wx.StaticText(panelka, 1, label='UwU Protogen Bot')
        lbl.SetForegroundColour('#42F0F8')

        hid_bs = wx.BoxSizer(wx.VERTICAL)
        hid_bs.Add(lbl)
        hid_bs.Add(inf_btn, flag= wx.EXPAND)

        title_bs = wx.BoxSizer()
        title_bs.Add(self.ava)
        title_bs.Add(hid_bs)
        
        bs = wx.BoxSizer(wx.VERTICAL)
        bs.Add(title_bs, proportion=1, flag= wx.EXPAND) 
        bs.Add(self.dialog_text, proportion=1, flag= wx.EXPAND)
        bs.Add(btn_listen, proportion=1, flag= wx.EXPAND)

        panelka.SetSizer(bs)
        panelka.Show()
        
    def uwu_listen(self, event ):
        #question = []
        print("Скажи чё нибудь")
        r = sr.Recognizer()
        with sr.Microphone() as sourse:
            audio = r.listen(sourse)
            try:
                question = r.recognize_google(audio, language='ru')
            except sr.UnknownValueError:
                    print( "error")
            except sr.RequestError:
                    print("error")
        listen_command(question)

       # if command.lower() in question:
            #find_on_inet(question.replace(command.lower(),' '))
          #  dialog_t.insert_text('Поиск по запросу: ' + question.replace('Уву найди',' ' ))
           # return 0
            
        global mood
        m = mood_analiz(question)
        if m == 1:
            mood = mood + 1
            if mood > 98:
                self.ava = wx.StaticBitmap( panelka, 1, wx.Bitmap(u'C:\\Users\\123\\Desktop\\UwU_protogen_assisteant\\UwU_image\\ava_funny.bmp'),size=(200, 200) )
        if m == 2:
            mood = mood - 1
            if mood < 98:
                self.ava = wx.StaticBitmap( panelka, 1, wx.Bitmap(u'C:\\Users\\123\\Desktop\\UwU_protogen_assisteant\\UwU_image\\ava_sad.bmp'),size=(200, 200) )
        
        message = Bot(question)
        print(message)
        
        voice = gTTS(message, lang='ru')
        file_voice_name = "audio" + str(random.randint(0, 100)) + ".mp3"
        voice.save(file_voice_name)
        
        pg.mixer.init()
        pg.mixer.music.load(file_voice_name)
        pg.mixer.music.play()
        print('UwU: ' + message)
        ab = message
        self.dialog_text.AppendText('User:   ' + question + '\n')
        self.dialog_text.AppendText('UwU:    ' + message + '\n')
        self.dialog_text.AppendText('\n\n')

#----------------------------------------------------------------------------------
        
app = wx.App()

frame = UwU_GUI(None, title='UwU Protogen Bot')
frame.Show()

app.MainLoop()
