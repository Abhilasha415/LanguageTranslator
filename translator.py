from tkinter import ttk, messagebox
import googletrans
import textblob
from tkinter import*

def label_change():
    c = comb1.get()
    c1 = comb2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)


def translate_now():
    global language
    try:
        text_ = text1.get(1.0, END)
        c2 = comb1.get()
        c3 = comb2.get()
        if(text_):
            words = textblob.TextBlob(text_)
            lan = words.detect_language()
            for i, j in language.items():
                if(j == c3):
                    lan_ = i
            words = words.translate(from_lang=lan, to=str(lan_))
            text2.delete(1.0, END)
            text2.insert(END, words)
    except Exception as e:
        messagebox.showerror('Transcript', 'Please try again')


root = Tk()
root.title('TRANSCRIPT')
root.geometry('1500x500')

image_icon = PhotoImage(file='language-translation-1-692570.png')
root.iconphoto(False, image_icon)

arrow_image = PhotoImage(file='arrow.png')
arrow_image = arrow_image.subsample(9, 9)

language = googletrans.LANGUAGES
language_ = list(language.values())
lang1 = language.keys()

############################## First Combo Box ####################

comb1 = ttk.Combobox(root, values=language_, font='times 10 bold', state='r')
comb1.place(x=150, y=20)
comb1.set('English')

label1 = Label(root, text='English', font='segoe 20 bold',
               bg='pink', width=30, bd=6, relief=GROOVE)
label1.place(x=0, y=50)

# Frame

f = Frame(root, bg='black', bd=5)
f.place(x=14, y=118, width=410, height=210)

# text area
text1 = Text(f, font='times 20 bold', bg='white', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=400, height=200)

# scroll bar
scroll_bar1 = Scrollbar(f)
scroll_bar1.pack(side='right', fill='y')
scroll_bar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scroll_bar1.set)


############################## Second Combo box ####################################

comb2 = ttk.Combobox(root, values=language_, font='times 10 bold', state='r')
comb2.place(x=785, y=20)
comb2.set('English')

label2 = Label(root, text='English', font='segoe 20 bold',
               bg='pink', width=30, bd=6, relief=GROOVE)
label2.place(x=500, y=50)

f1 = Frame(root, bg='black', bd=5)
f1.place(x=600, y=118, width=410, height=210)

# text area
text2 = Text(f1, font='times 20 bold', bg='white',
             relief=GROOVE, wrap=WORD, fg='green')
text2.place(x=0, y=0, width=400, height=200)

# scroll bar
scroll_bar2 = Scrollbar(f1)
scroll_bar2.pack(side='right', fill='y')
scroll_bar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scroll_bar2.set)

image_label = Label(root, image=arrow_image, width=150)
image_label.place(x=445, y=50)

trans_btn = Button(root, text='TRANSLATE', font='Impact 16',
                   activebackground='purple', cursor='hand2', bd=5, bg='blue', fg='white', command=translate_now)
trans_btn.place(x=450, y=250)
label_change()

root.mainloop()