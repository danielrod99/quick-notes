from tkinter import *
from tkinter import messagebox
from controllers import logInController

def home():
    homeLabel = Label(mainWindow, text="Home")
    homeLabel.grid(row=0, column=0,columnspan=4)
def signUpFields():
    regLabel=Label(mainWindow,text="Sign Up")
    labelName=Label(mainWindow,text="Name:")
    entryName=Entry(mainWindow, textvariable=name)
    labelLast=Label(mainWindow,text="Last name:")
    entryLast=Entry(mainWindow, textvariable=lastname)
    labelEmail=Label(mainWindow,text="Email:")
    entryEmail=Entry(mainWindow, textvariable=email)
    labelPass=Label(mainWindow,text="Password:")
    entryPass=Entry(mainWindow, textvariable=password)

    regLabel.grid(row=1,column=0,padx=5,pady=5)
    labelName.grid(row=2,column=0,padx=5,pady=5)
    entryName.grid(row=2,column=1,padx=5,pady=5)
    labelLast.grid(row=3,column=0,padx=5,pady=5)
    entryLast.grid(row=3,column=1,padx=5,pady=5)
    labelEmail.grid(row=4,column=0,padx=5,pady=5)
    entryEmail.grid(row=4,column=1,padx=5,pady=5)
    labelPass.grid(row=5,column=0,padx=5,pady=5)
    entryPass.grid(row=5,column=1,padx=5,pady=5)

    registerButton=Button(mainWindow,text="Sign Up",command=getAndRegister)
    registerButton.grid(row=6,column=0,padx=5,pady=5)

def logInFields():
    logLab=Label(mainWindow,text="Log In")
    logEmail=Label(mainWindow,text="Email:")
    lEntryEmail=Entry(mainWindow, textvariable=logInEmail)
    logPass=Label(mainWindow,text="Password:")
    lEntryPass=Entry(mainWindow, textvariable=logInPass)

    logLab.grid(row=1,column=8,padx=5,pady=5)
    logEmail.grid(row=2,column=8,padx=5,pady=5)
    lEntryEmail.grid(row=2,column=9,padx=5,pady=5)
    logPass.grid(row=3,column=8,padx=5,pady=5)
    lEntryPass.grid(row=3,column=9,padx=5,pady=5)

    registerButton=Button(mainWindow,text="Log In",command=getAndLog)
    registerButton.grid(row=4,column=8,padx=5,pady=5)
def register(name, lastname, email, password):
    theUser = logInController.insertUser(name, lastname, email, password)
    if theUser == True:
        messagebox.showinfo("Success", "The user was registered successfully!")
    else:
        messagebox.showerror("Error", "There was an error, please try again")

def getAndRegister():
    name1=name.get()
    last1=lastname.get()
    email1=email.get()
    password1=password.get()
    register(name1,last1,email1,password1)

def logIn(email, password):
    theUser = logInController.logIn(email, password)
    print(theUser)
    if theUser == False:
        messagebox.showerror("Error", "The user does not exist")
    else:
        return theUser

def getAndLog():
    email1=logInEmail.get()
    password1=logInPass.get()
    logIn(email1,password1)

mainWindow = Tk()
mainWindow.geometry("500x500")
mainWindow.title("Quick Notes with Tkinter")
mainWindow.resizable(0, 0)

name = StringVar()
lastname = StringVar()
email = StringVar()
password = StringVar()

logInEmail= StringVar()
logInPass=StringVar()

home()
signUpFields()
logInFields()

topMenu = Menu(mainWindow)
topMenu.add_command(label="Exit", command=mainWindow.quit)
mainWindow.config(menu=topMenu)


mainWindow.mainloop()
