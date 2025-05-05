import tkinter as tk
import getpass
from tkinter import messagebox
from tkinter import filedialog

actualfont = "Rubik Regular"
fontsize = "16"

username = getpass.getuser()
print(username)

def aboutbox():
    messagebox.showinfo("About NoteWriter", f"NoteWriter 1.0b, 2022-2025 zTech");

def opentxt():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def savetxt():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

def newtxt():
    messagebox.showwarning("Warning", f"You will lose your text document if you had forgot to save.");
    text_area.delete(1.0, tk.END)

def rubikfont():
    actualfont = "Rubik Regular"
    text_area.config(font=(actualfont, fontsize))

def arialfont():
    actualfont = "Arial"
    text_area.config(font=(actualfont, fontsize))

def erasfont():
    actualfont = "Eras Demi ITC"
    text_area.config(font=(actualfont, fontsize))

def frankfont():
    actualfont = "Franklin Gothic Medium"
    text_area.config(font=(actualfont, fontsize))

def lmode():
    actualbg = "white"
    text_area.config(bg=actualbg, fg="#000000")

def dmode():
    actualbg = "#191919"
    text_area.config(bg=actualbg, fg="#FFFFFF")

root = tk.Tk()
root.title("zTech NoteWriter")
root.geometry("1280x640")

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

font_menu = tk.Menu(menu_bar, tearoff=0, bg="black", fg="white")
font_menu.add_command(label="Rubik", command=rubikfont)
font_menu.add_command(label="Arial", command=arialfont)
font_menu.add_command(label="Eras Demi ITC", command=erasfont)
font_menu.add_command(label="Franklin Gothic", command=frankfont)

theme_menu = tk.Menu(menu_bar, tearoff=0, bg="black", fg="white")
theme_menu.add_command(label="Brightness (Light)", command=lmode)
theme_menu.add_command(label="Darkness (Dark)", command=dmode)

root.config(menu=menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Other", menu=other_menu)
menu_bar.add_cascade(label="Fonts", menu=font_menu)
menu_bar.add_cascade(label="Themes", menu=theme_menu)

root.mainloop()

