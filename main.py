from tkinter import *
root = Tk()
root.geometry ("400x300")
root. title("main")
 

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("topleve]")
    l2 = Label(top, text = "This is toplevel window")
    l2.pack()
    top.mainloop()
l1=Label(root, text="This is root window")
btn=Button(root, text="Click here te open another window",command=topwin)
l1.pack()
btn.pack()
root.mainloop()