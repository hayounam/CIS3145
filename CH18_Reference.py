# Hayoung Nama
# Preferences
# Create a GUI program that stores a user’s preferences for a program.
# July 26 2020

from tkinter import *

def load():
    name_txt=""
    language="English"
    auto_save=5
    try:
        file=open("preferences.txt")
        name_txt=file.readline().strip()
        language=file.readline().strip()
        auto_save=int(file.readline().strip())
    except:
        pass
    
    name.set(name_txt)
    lang.set(language)
    auto_save_mins.set(str(auto_save))


def save():
    error=False
    if len(name.get())==0:
        err_name.set("Required.")
        error=True
    if len(lang.get())==0:
        err_lang.set("Required.")
        error = True
    try:
        minutes=int(auto_save_mins.get())
    except:
        err_auto_save.set("Must be valid integer.")
        error = True
    if not error:
        file=open("preferences.txt","w")
        file.write(name.get()+'\n')
        file.write(lang.get()+'\n')
        file.write(auto_save_mins.get()+'\n')
        file.close()
        exit(0)

root=Tk()
root.title("Preferences")

name=StringVar()
lang=StringVar()
auto_save_mins=StringVar()
err_name=StringVar()
err_lang=StringVar()
err_auto_save=StringVar()


def ui():
    
    Label(master=root,text="Name: ").grid(row=0, column=0)
    Entry(root,textvariable=name).grid(row=0, column=1,columnspan=2)
    Label(master=root,text=' ',textvariable=err_name).grid(row=0, column=3)

    Label(master=root,text="Language: ").grid(row=1, column=0)
    Entry(root,textvariable=lang).grid(row=1, column=1,columnspan=2)
    Label(master=root,text=' ',textvariable=err_lang).grid(row=1, column=3)

    Label(master=root,text="Auto Save Every X Minutes: ").grid(row=2, column=0)
    Entry(root,textvariable=auto_save_mins).grid(row=2, column=1,columnspan=2)
    Label(master=root,text=' ',textvariable=err_auto_save).grid(row=2, column=3)

    Button(text="Save",command=lambda: save()).grid(row=3,column=1,sticky='ew')
    Button(text="Cancel",command=lambda: exit(0)).grid(row=3,column=2,sticky='ew')
    
    load()
    root.mainloop()
    
def main():
    ui()

if __name__ == "__main__":
    main()
