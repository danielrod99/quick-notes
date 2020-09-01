from tkinter import *
mainWindow = Tk()
mainWindow.geometry("500x500")
mainWindow.title("Quick Notes with Tkinter")
mainWindow.resizable(0,0)

topMenu=Menu(mainWindow)
topMenu.add_command(label="Exit", command=mainWindow.quit)
mainWindow.config(menu=topMenu)


mainWindow.mainloop()