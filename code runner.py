import os
import tkinter
from tkinter import *
from tkinter import ttk
import subprocess

root=Tk()

root.title("CODE RUNNER")

#opening a new file

all_langs={
    "C":["ccode.c","gcc ccode.c -o ccode.exe","ccode"],
    "Python":["pycode.py","python","pycode.py"],
    "Go":["godemo.go"]
}

#Language codes for selecting file path

codes_path={
    "C":"ccode",
    "Python":"python pycode.py",
    "Go":"go run godemo.go"
}

#defaultly language is 'C'

which_lang=all_langs["C"]

def select_lang(event):
    global which_lang
    which_lang=all_langs[selected_lang.get()]

def Run():
    global which_lang

    #Clear all in a output box
    outputbox.delete("1.0",END)
    f=open(which_lang[0],"w+")    #file creating or opening for write and read operation
    code=editor.get("1.0",END)

    f.write(code)   #Writing code in a file
    f.read()    #for saving a file

    #Compiling part
    if selected_lang.get()=="C":
        os.system("gcc ccode.c -o ccode.exe")

    output_process=subprocess.Popen(codes_path[selected_lang.get()],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)

    #Converting input string to bytes
    output_process.stdin.write(bytes(inputbox.get("1.0",END),"utf-8"))

    output,error=output_process.communicate()

    #Printing output or any error to the output box
    outputbox.insert(END,output)
    outputbox.insert(END,error)

def saveit():
    pass

def save_it_as():
    pass

#creating menu bar
menubar=Menu(root)

file=Menu(menubar,tearoff=0)

#Adding options to the file menu item
file.add_command(label="save",command=saveit)
file.add_command(label="save as",command=save_it_as)
file.add_command(label="undo",command=save_it_as)
file.add_command(label="redo",command=save_it_as)
file.add_command(label="delete",command=save_it_as)
file.add_separator()
file.add_command(label="Quit",command=root.quit,activebackground="red",activeforeground="white")

menubar.add_cascade(label="File",menu=file)
#for selected value
selected_lang=StringVar()
selected_lang.set("C")
cbox=ttk.Combobox(root,values=["C","Python","Go"],textvariable=selected_lang)

#Code editor
editor=Text(root,height=10,bg="black",fg="white")

#input box
inputbox=Text(root,bg="black",fg="white")

#Run button
runit=Button(root,text="RUN",command=Run)

#Output box
outputbox=Text(root)

#Select a programming language from combobox
cbox.bind("<<ComboboxSelected>>",select_lang)

cbox.pack()
editor.pack()
inputbox.pack()
runit.pack()
outputbox.pack()

#Adding menubar
root.config(menu=menubar)
root.mainloop()