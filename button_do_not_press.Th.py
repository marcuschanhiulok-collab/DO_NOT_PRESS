import tkinter as tk

window = tk.Tk()
window.title("Do Not Press")

clickcount = 0

def onClick(event):
    global clickcount
    clickcount += 1
    
    if clickcount == 1:
        button.config(text="Seriously? Do. Not. Press. It.")
    elif clickcount == 2:
        button.config(text="Gah! Next time, no more button!")
    else:
        button.pack_forget()

button = tk.Button(window, text="Do NOT press this button", width=40)
button.pack(padx=10, pady=10)

button.bind("<ButtonRelease-1>", onClick)

window.mainloop()
