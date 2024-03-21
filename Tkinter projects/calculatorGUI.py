import tkinter as tk
root= tk.Tk()
root.iconbitmap("mark.ico")
root.title("calculator")

top_label=tk.Label(root,text="Enter The Operations:",font=("Times New Roman",30))
top_label.grid(row=0,column=0,columnspan=4)

num_entry=tk.Entry(root,font=("Times New Roman",30),width=18)
num_entry.grid(row=1,column=0,columnspan=4)

tk.Button(root,text=" 1 ",font=("Times New Roman",30),border=5,command=lambda:add("1")).grid(row=2,column=0)
tk.Button(root,text=" 2 ",font=("Times New Roman",30),border=5,command=lambda:add("2")).grid(row=2,column=1)
tk.Button(root,text=" 3 ",font=("Times New Roman",30),border=5,command=lambda:add("3")).grid(row=2,column=2)
tk.Button(root,text=" 4 ",font=("Times New Roman",30),border=5,command=lambda:add("4")).grid(row=3,column=0)
tk.Button(root,text=" 5 ",font=("Times New Roman",30),border=5,command=lambda:add("5")).grid(row=3,column=1)
tk.Button(root,text=" 6 ",font=("Times New Roman",30),border=5,command=lambda:add("6")).grid(row=3,column=2)
tk.Button(root,text=" 7 ",font=("Times New Roman",30),border=5,command=lambda:add("7")).grid(row=4,column=0)
tk.Button(root,text=" 8 ",font=("Times New Roman",30),border=5,command=lambda:add("8")).grid(row=4,column=1)
tk.Button(root,text=" 9 ",font=("Times New Roman",30),border=5,command=lambda:add("9")).grid(row=4,column=2)
tk.Button(root,text=" 0 ",font=("Times New Roman",30),border=5,command=lambda:add("0")).grid(row=5,column=0)

tk.Button(root,text=" X ",font=("Times New Roman",30),border=5,command=lambda:clear()).grid(row=5,column=1)
tk.Button(root,text=" = ",font=("Times New Roman",30),border=5,command=lambda:calculate()).grid(row=5,column=2)

tk.Button(root,text=" + ",font=("Times New Roman",30),border=5,command=lambda:add("+")).grid(row=2,column=3)
tk.Button(root,text=" - ",font=("Times New Roman",30),border=5,command=lambda:add("-")).grid(row=3,column=3)
tk.Button(root,text=" * ",font=("Times New Roman",30),border=5,command=lambda:add("*")).grid(row=4,column=3)
tk.Button(root,text=" / ",font=("Times New Roman",30),border=5,command=lambda:add("/")).grid(row=5,column=3)

def calculate():
    result=str(eval(num_entry.get()))
    top_label.config(text=num_entry.get())
    num_entry.delete(0,tk.END)
    num_entry.insert(0,result)

def clear():
    top_label.config(text="Enter The Operations:")
    num_entry.delete(0,tk.END)

def add(a):
    num_entry.insert(tk.END,a)

root.mainloop()