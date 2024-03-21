import tkinter as tk

root1 = tk.Tk()
root1.iconbitmap("mark.ico")
root1.title("Grid")
root1.config(bg="#B266FF")
tk.Label(root1,text="2x2",font=("Times New Roman",100),fg="#ffffff",bg="royal blue").grid(row=0,column=0,columnspan=2,rowspan=2)
tk.Label(root1,text="1x1",font=("Times New Roman",50),fg="#ffffff",bg="royal blue").grid(row=2,column=2)
tk.Label(root1,text="1",font=("Times New Roman",50),fg="#ffffff",bg="red").grid(row=0,column=2)
tk.Label(root1,text="1",font=("Times New Roman",50),fg="#ffffff",bg="red").grid(row=1,column=2)
tk.Label(root1,text="1",font=("Times New Roman",50),fg="#ffffff",bg="red").grid(row=2,column=0)
tk.Label(root1,text="1",font=("Times New Roman",50),fg="#ffffff",bg="red").grid(row=2,column=1)
# to close this window you can use: root1.destroy()

root2 = tk.Tk()
root2.iconbitmap("mark.ico")
root2.title("Frame")
down_frame = tk.Frame(root2)
down_frame.pack(side="bottom")   #  side = "top"  "bottom"  "left"  "right"
up_frame = tk.Frame(root2)
up_frame.pack(side="top")   #  side = "top"  "bottom"  "left"  "right"
MyEntry = tk.Entry(down_frame,font=("Times New Roman",40),width=12,border=10)#colors: fg= ,bg=
MyEntry.pack()
MyButton = tk.Button(up_frame,text="Print The Entry",font=("Times New Roman",35) #colors: activebackground= ,activeforeground= ,bg= ,fg=
                    ,border=10,command=lambda:prnt(MyEntry.get()))
MyButton.pack()
def prnt(a): print(a);


root1.mainloop()
root2.mainloop()