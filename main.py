from tkinter import *
from tkinter import messagebox
from controllers import logInController
from controllers import notesController


def home():
    homeLabel = Label(mainWindow, text="Home")
    homeLabel.grid(row=0, column=0, columnspan=4)


def signUpFields():
    regLabel = Label(mainWindow, text="Sign Up")
    labelName = Label(mainWindow, text="Name:")
    entryName = Entry(mainWindow, textvariable=name)
    labelLast = Label(mainWindow, text="Last name:")
    entryLast = Entry(mainWindow, textvariable=lastname)
    labelEmail = Label(mainWindow, text="Email:")
    entryEmail = Entry(mainWindow, textvariable=email)
    labelPass = Label(mainWindow, text="Password:")
    entryPass = Entry(mainWindow, textvariable=password)

    regLabel.grid(row=1, column=0, padx=5, pady=5)
    labelName.grid(row=2, column=0, padx=5, pady=5)
    entryName.grid(row=2, column=1, padx=5, pady=5)
    labelLast.grid(row=3, column=0, padx=5, pady=5)
    entryLast.grid(row=3, column=1, padx=5, pady=5)
    labelEmail.grid(row=4, column=0, padx=5, pady=5)
    entryEmail.grid(row=4, column=1, padx=5, pady=5)
    labelPass.grid(row=5, column=0, padx=5, pady=5)
    entryPass.grid(row=5, column=1, padx=5, pady=5)

    registerButton = Button(mainWindow, text="Sign Up", command=getAndRegister)
    registerButton.grid(row=6, column=0, padx=5, pady=5)


def logInFields():
    logLab = Label(mainWindow, text="Log In")
    logEmail = Label(mainWindow, text="Email:")
    lEntryEmail = Entry(mainWindow, textvariable=logInEmail)
    logPass = Label(mainWindow, text="Password:")
    lEntryPass = Entry(mainWindow, textvariable=logInPass)

    logLab.grid(row=1, column=8, padx=5, pady=5)
    logEmail.grid(row=2, column=8, padx=5, pady=5)
    lEntryEmail.grid(row=2, column=9, padx=5, pady=5)
    logPass.grid(row=3, column=8, padx=5, pady=5)
    lEntryPass.grid(row=3, column=9, padx=5, pady=5)

    registerButton = Button(mainWindow, text="Log In", command=getAndLog)
    registerButton.grid(row=4, column=8, padx=5, pady=5)


def register(name, lastname, email, password):
    theUser = logInController.insertUser(name, lastname, email, password)
    if theUser == True:
        messagebox.showinfo("Success", "The user was registered successfully!")
    else:
        messagebox.showerror("Error", "There was an error, please try again")


def getAndRegister():
    name1 = name.get()
    last1 = lastname.get()
    email1 = email.get()
    password1 = password.get()
    register(name1, last1, email1, password1)


def logIn(email, password):
    theUser = logInController.logIn(email, password)
    if theUser == False:
        messagebox.showerror("Error", "The user does not exist")
    else:
        mainWindow.destroy()
        secondWindow(theUser)


def getAndLog():
    email1 = logInEmail.get()
    password1 = logInPass.get()
    logIn(email1, password1)


def getNotes(theUser):
    myNotes = notesController.allNotes(theUser.id)
    fullText = ""
    for nota in myNotes:
        fullText += '------------------------------\n'
        fullText += f"{nota[2]}\n{nota[3]}\n"
    fullText += "--------------------------------"
    allNotes = Label(notes, text=fullText)
    allNotes.config(state="disabled")
    allNotes.grid(row=1, column=0, columnspan=6)


def submitNote(theUser, title, body):
    if(title != "" and body != ""):
        notesController.createNote(theUser.id, title, body)
        messagebox.showinfo("Success","Note Created")
        getNotes(theUser)
    else:
        messagebox.showwarning("Error", "Fill all the values")

def deleteNote(theUser):
    title=deleteTitle.get()
    if title!="":
        notesController.deleteNote(theUser.id,title)
        messagebox.showinfo("Success","Note Deleted")
        getNotes(theUser)
    else:
        messagebox.showwarning("Error", "Fill all the values")

def secondWindow(theUser):
    notes=Tk()
    notes.geometry("500x500")
    notes.title("Quick Notes with Tkinter")
    notes.resizable(0, 0)
    topMenu = Menu(notes)
    topMenu.add_command(label="Exit", command=notes.quit)
    notes.config(menu=topMenu)
    getNotes(theUser)

    noteTitle = Label(notes, text="Title:")
    noteTitleEntry = Entry(notes, textvariable=noteTitleVar)
    noteBodyL = Label(notes, text="Note:")
    noteBodyEntry = Entry(notes, textvariable=noteBody)
    noteTitle.grid(row=10, column=0)
    noteTitleEntry.grid(row=10, column=1)
    noteBodyL.grid(row=11, column=0)
    noteBodyEntry.grid(row=11, column=1)
    title = noteTitleVar.get()
    body = noteBody.get()
    submitButton = Button(notes, text="Submit Note",
                          command=lambda: submitNote(theUser, title, body))
    submitButton.grid(row=12, column=0)

    Label(notes).grid(row=13, column=0)
    deleteLabel = Label(notes, text="Title of the note to delete:")
    noteTitleEntry = Entry(notes, textvariable=deleteTitle)
    deleteButton = Button(notes, text="Delete",command=lambda: deleteNote(theUser))
    deleteLabel.grid(row=14, column=0)
    noteTitleEntry.grid(row=14, column=1)
    deleteButton.grid(row=15, column=0)

    notes.mainloop()


mainWindow = Tk()
mainWindow.geometry("500x500")
mainWindow.title("Quick Notes with Tkinter")
mainWindow.resizable(0, 0)
notes = None
name = StringVar()
lastname = StringVar()
email = StringVar()
password = StringVar()

logInEmail = StringVar()
logInPass = StringVar()

noteTitleVar = StringVar()
noteBody = StringVar()
deleteTitle = StringVar()

home()
signUpFields()
logInFields()

topMenu = Menu(mainWindow)
topMenu.add_command(label="Exit", command=mainWindow.quit)
mainWindow.config(menu=topMenu)


mainWindow.mainloop()
