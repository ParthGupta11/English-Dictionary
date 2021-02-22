from tkinter import * # For building GUI
import json # For file handling
from difflib import get_close_matches # For finding similar words


window = Tk()

data = json.load(open("data.json",'r'))


def display(word):
    meanings = data[word]
    i = 1
    if len(meanings) < 2:
        msg_box.insert(END,"The meaning of %s is: \n" %word )
    else :
        msg_box.insert(END,"The meanings of %s are: \n"%word)
    while i <= len(meanings):
        msg_box.insert(END,"{} : {}\n".format(i,meanings[i-1]))
        i += 1


def meaning(): ##Through difflib library
    msg_box.delete(1.0,END)
    word = word_entry.get().lower()
    if word in data.keys() :
        display(word)
    elif len(get_close_matches(word,data.keys(),1,cutoff=0.8)) > 0:
        new_word = get_close_matches(word,data.keys(),1,cutoff=0.8)
        msg_box.insert(END,"Did you mean %s ?\n" %new_word[0])
        display(new_word[0])
    else:
        msg_box.insert(END,"Word not in dictionary")


l1 = Label(window,text="Enter query:")
l1.grid(row=0,column=0)

word_entry = StringVar()
word_box = Entry(window,textvariable=word_entry)
word_box.grid(row=1,column=0)
#word = word_entry.get()

b1 = Button(window,text="Search",command=meaning)
b1.grid(row=1,column=1)

msg_box = Text(window,height=10,width=100)
msg_box.grid(row=2,column=0,columnspan=3,padx=5,pady=5)

window.mainloop()
