def open_bot_page():
    import webbrowser
    webbrowser.open('')

def create_inf_window(event):
    from tkinter import Tk, Label, Text, Button

    root = Tk()
    root.title('About')
    root.configure(bg='darkCyan')

    title_text= "UwU Protogen Bot"

    inf_text = '''Привет, я UwU [читается ка 'Уву'] - ваш цифровой ассистент. Меня создали совсем недавно и я пока немного тупой,
                  но уже могу общаться и выполнять простые команды(поиск в интернете и выход из програмы(и то не факт) ).
                  Чтобы узнать больше важной информации читайте ниже
                  '''
    
    other_text = '''Команды UwU Бота:
 "ВЫХОД" - закрытие программы
 "НАЙДИ"+ваш запрос - открытие браузера и поиск вашего запроса
 
License:
  UwU Protogen Bot - бесплатное ПО с открытым исходным кодом,
  выможете использовать его по своему усмотрению,
  но не забывайте, что ни создатель(и), ни сам UwU Protogen Bot не несут
  за это никакой ответсветнности. Lol.
  Если вы хотите распространить данное ПО, пожалуйста укажите автора(ов).
  
Вы обнаружили баги:
   Если данное ПО лагает, не работает или работает,
   но не правильно посетите страницу UwU Бота и сообщите о проблеме


                               03.11.21'''

    t_area = Text()
    t_area.insert(1.0, other_text)
    t_area.config(state='disabled')

    title_lbl = Label(text=title_text, bg='darkCyan', fg='cyan')
    title_lbl.pack()

    btn = Button(text='Страница UwU Бота', command=open_bot_page, bg='grey', fg='cyan')

    avtor_lbl = Label(text='Автор: ', bg='darkCyan', fg='cyan')

    inf_lbl = Label(text=inf_text, bg='darkCyan', fg='cyan')
    inf_lbl.pack()
    t_area.pack()
    btn.pack()
    avtor_lbl.pack()

    root.mainloop()
