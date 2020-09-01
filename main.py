from tkinter import *
from tkinter import messagebox
from controllers import logInController
from models import user

def home():
    homeLabel = Label(mainWindow, text="Home")
    homeLabel.grid(row=0, column=0,columnspan=4)


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
    if theUser == False:
        messagebox.showerror("Error", "The user does not exist")
    else:
        return theUser


mainWindow = Tk()
mainWindow.geometry("500x500")
mainWindow.title("Quick Notes with Tkinter")
mainWindow.resizable(0, 0)

name = StringVar()
lastname = StringVar()
email = StringVar()
password = StringVar()

home()

register = Frame(mainWindow,width=250,height=250)
regLabel=Label(register,text="Sign Up")
labelName=Label(register,text="Name:")
entryName=Entry(register, textvariable=name)
labelLast=Label(register,text="Last name:")
entryLast=Entry(register, textvariable=lastname)
labelEmail=Label(register,text="Email:")
entryEmail=Entry(register, textvariable=email)
labelPass=Label(register,text="Password:")
entryPass=Entry(register, textvariable=password)

regLabel.grid(row=0,column=0,padx=5,pady=5)
labelName.grid(row=1,column=0,padx=5,pady=5)
entryName.grid(row=1,column=1,padx=5,pady=5)
labelLast.grid(row=2,column=0,padx=5,pady=5)
entryLast.grid(row=2,column=1,padx=5,pady=5)
labelEmail.grid(row=3,column=0,padx=5,pady=5)
entryEmail.grid(row=3,column=1,padx=5,pady=5)
labelPass.grid(row=4,column=0,padx=5,pady=5)
entryPass.grid(row=4,column=1,padx=5,pady=5)

registerButton=Button(register,command=getAndRegister,text="Sign Up")
registerButton.grid(row=5,column=0,padx=5,pady=5)

register.grid(row=1,column=0,columnspan=6)

topMenu = Menu(mainWindow)
topMenu.add_command(label="Exit", command=mainWindow.quit)
mainWindow.config(menu=topMenu)


mainWindow.mainloop()
