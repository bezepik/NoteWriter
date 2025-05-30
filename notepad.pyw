import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# i hate spelling this stupid font
actualfont = "Bahnschrift"

# this variable is useless now, but i don't give a fuck
fontsize = "16"

def aboutbox():
    messagebox.showinfo("About", "NoteWriter 1.0 rc1, 2022-2025 zTech");

# things for files
def opentxt():
    messagebox.showwarning("Warning!", "You'll lose your document if you had forgot to save.");
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path) as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
            print("opened file")

def savetxt():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path) as file:
            file.write(text_area.get(1.0, tk.END))
            print("saved file")

def newtxt():
    messagebox.showwarning("Warning!", f"You'll lose your document if you had forgot to save.");
    text_area.delete(1.0, tk.END)
    print("a new file has been born")

def arialfont():
    actualfont = "Arial"
    text_area.config(font=(actualfont, "16"))

def erasfont():
    actualfont = "Eras Demi ITC"
    text_area.config(font=(actualfont, "16"))

def frankfont():
    actualfont = "Franklin Gothic Medium"
    text_area.config(font=(actualfont, "16"))

def stupidfont():
    actualfont = "Comic Sans MS"
    text_area.config(font=(actualfont, "16"))

def bahnfont():
    actualfont = "Bahnschrift"
    text_area.config(font=(actualfont, "16"))

def lmode():
    actualbg = "white"
    text_area.config(bg=actualbg, fg="#191919")

def dmode():
    actualbg = "#191919"
    text_area.config(bg=actualbg, fg="white")

def bmode():
    actualbg = "#80aaff"
    text_area.config(bg=actualbg, fg="white")

root = tk.Tk()
root.title("NoteWriter")
root.geometry("1080x640")

text_area = tk.Text(root, font=(actualfont, fontsize), bg="#191919", fg="white",)
text_area.pack(expand=True, fill=tk.BOTH)

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0, bg="black", fg="white")
file_menu.add_command(label="New", command=newtxt)
file_menu.add_command(label="Save", command=savetxt)
file_menu.add_command(label="Open", command=opentxt)

other_menu = tk.Menu(menu_bar, tearoff=0, bg="black", fg="white")
other_menu.add_command(label="About", command=aboutbox)
other_menu.add_separator()
other_menu.add_command(label="Exit", command=root.quit)
# oh yeah add more fonts for 1.1 future me
font_menu = tk.Menu(menu_bar, tearoff=0, bg="black", fg="white")
font_menu.add_command(label="Default (Bahnschrift)", command=bahnfont)
font_menu.add_command(label="Arial", command=arialfont)
font_menu.add_command(label="Eras Demi ITC", command=erasfont)
font_menu.add_command(label="Franklin Gothic", command=frankfont)
font_menu.add_command(label="Comic Sans (worst font ever)", command=stupidfont)

theme_menu = tk.Menu(menu_bar, tearoff=0, bg="black", fg="white")
theme_menu.add_command(label="Brightness", command=lmode)
theme_menu.add_command(label="Darkness", command=dmode)
theme_menu.add_command(label="Sky", command=bmode)

root.config(menu=menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Fonts", menu=font_menu)
menu_bar.add_cascade(label="Themes", menu=theme_menu)
menu_bar.add_cascade(label="Other", menu=other_menu)

root.mainloop()
# you can also edit notewriter in notewriter because idfk
