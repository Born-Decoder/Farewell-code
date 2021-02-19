import random
import tkinter as tk
import PIL.Image
from PIL import ImageTk
from tkinter import font
import pandas as pd
from os import startfile
import os
from tkinter import *
file = pd.read_excel('values.xlsx')
path1 = "C:\\Users\\manoj.prabhakaran\\Downloads\\and-fact.png"
path2 = "C:\\Users\\manoj.prabhakaran\\Downloads\\lion-king.jpg"
path3 = "C:\\Users\\manoj.prabhakaran\\Downloads\\shrawan.jpg"
path4 = "C:\\Users\\manoj.prabhakaran\\Downloads\\chandra.mp4"
intro = ['Well','How are you Peeps?','Doing good?','I hope so.',
         'Yeah, you all know.','Do I need to say?','It has been a ride!',
         'and today is the time','we gotta say bye','to a guy.',
         'So Let us begin!','Oh wait.','It is bland to start abrupt.',
         'so how do we do it?','oh yeah!','I got an idea!','How about a ...',
         'COUNTDOWN?','30','29','28','No! stop it is taking long!',
         'No kidding!','here we go!','For real this time.','Oh Did I forget...',
         'To say something?','No I dont think so','NO WAIT!',
         'I forgot the intro!',
         'No worries, I will print it!','Here is a compilation',
         "of people's says", 'from what we have collected...',
         'of course there will be...', 'special talks', 'on the spot as well!',
         'so let us start', 'yeah! Finally!', 'Hope you like it ;-)']

names = file["Name"].tolist()
says = file["Say"].tolist()
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Last code")        
        self.configure(background='black')
        self.columnconfigure(0, minsize=1250)
        self.rowconfigure([0, 1, 2], minsize=210)
        self.lbl1 = tk.Label(text="Come on Here we go!",bg="black", fg="green",
                             font=("Terminal", 25))
        self.lbl1.grid(row=0, column=0)
        self.lbl2 = tk.Label(text="",bg="black", fg="green2",
                             font=("Times New Roman",18) ,wraplength=1250,justify="center")
        self.lbl2.grid(row=1, column=0)
        self.remaining = 45
        self.specials = 4
        self.starts = 40

        self.btn1 = tk.Button(text="START",bg="black", fg="green",
                              font=("Terminal", 15),
                              command=lambda:self.countdown(self.remaining))
        self.btn1.grid(row=2, column=0)

        

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining
        

        if self.remaining <= 0:
            self.lbl1.configure(text="Thanks a lot!")
            self.btn1.configure(text="Next")
            if len(names) == 0:
                if self.specials == 2:
                    self.lbl1.configure(text="And I gotta agree!")
                    fp = open(path2,"rb")
                    img = PIL.Image.open(fp)
                    img = img.resize((500,300))
                    self.lbl2.img = ImageTk.PhotoImage(img)
                    self.lbl2['image']=self.lbl2.img
                    self.specials = 1
                    
                elif self.specials == 1:
                    self.lbl1.configure(text="It is a fact!")
                    fp = open(path1,"rb")
                    img = PIL.Image.open(fp)
                    img = img.resize((500,300))
                    self.lbl2.img = ImageTk.PhotoImage(img)
                    self.lbl2['image']=self.lbl2.img
                    self.btn1.configure(text="The End")
                    self.specials = 0
                    
                elif self.specials == 3:
                    self.lbl1.configure(text="We made a few memes too!!")
                    fp = open(path3,"rb")
                    img = PIL.Image.open(fp)
                    img = img.resize((500,300))
                    self.lbl2.img = ImageTk.PhotoImage(img)
                    self.lbl2['image']=self.lbl2.img
                    self.specials = 2
                elif self.specials == 4:
                    self.lbl1.configure(text="Thanks a lot for your contributions!")
                    startfile(path4)
                    self.lbl2.configure(text="Well that's nice video!")
                    self.specials = 3
                elif self.specials == 0:
                    self.lbl1.configure(text="Thanks a lot!")
                    self.lbl2['image']=''
                    self.lbl2.configure(text="It's been a wonderful journey, we wish you all the best for the good times ahead!")
                    self.btn1.configure(text="The End")
                else:
                    return
            else:
                selection = random.randint(0,len(names)-1)
                self.lbl1.configure(text=names[selection]+str(" (")+str(len(names)-1)+str(")"))
                self.lbl2.configure(text=says[selection])
                names.remove(names[selection])
                says.remove(says[selection])
        else:
            if self.starts > 0:
                self.lbl1.configure(text=intro[40-self.starts])
                self.starts = self.starts - 1
            elif self.remaining<=5:
                self.lbl1.configure(text="%d" % self.remaining)
                self.lbl2.configure(text="Let's hear what people say!")
            
            self.remaining = self.remaining - 1
            self.after(100, self.countdown)

if __name__ == "__main__":
    app = App()
    app.mainloop()

