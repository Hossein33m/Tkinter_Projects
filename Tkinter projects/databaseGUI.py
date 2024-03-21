import tkinter as tk
root= tk.Tk()
root.iconbitmap("mark.ico")
root.title("database")
top=[1,2,3,4]
for i in range(4): a=tk.Frame(root); a.pack(side="top"); top[i] = a; 

tk.Label(top[0],text=" USER: ",font=("Times New Roman",30)).pack(side="left")
user_entry=tk.Entry(top[0],font=("Times New Roman",30))
user_entry.pack(side="left")

tk.Label(top[1],text=" PASS: ",font=("Times New Roman",30)).pack(side="left")
pass_entry=tk.Entry(top[1],font=("Times New Roman",30))
pass_entry.pack(side="left")

tk.Label(top[2],text=" MAIL: ",font=("Times New Roman",30)).pack(side="left")
mail_entry=tk.Entry(top[2],font=("Times New Roman",30))
mail_entry.pack(side="left")

tk.Button(top[3],text="UserName",font=("Times New Roman",30),border=5,command=lambda:printU()).pack(side="left")
tk.Button(top[3],text="Password",font=("Times New Roman",30),border=5,command=lambda:printP()).pack(side="left")
tk.Button(top[3],text="Email",font=("Times New Roman",30),border=5,command=lambda:printM()).pack(side="left")

def printU():
    print(user_entry.get())

def printP():
    print(pass_entry.get())

def printM():
    print(mail_entry.get())


root.mainloop()