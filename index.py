from tkinter import
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Text Editor")
window.geometry("600x500")

window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", ".txt"), ("All Files"), "."]
    )
    if not filepath:
        return
   
    txt_edit.delete(1.0, END)
   
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
        txt_edit.insert(END, text)
       
    window.title(f"Text Editor-{filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", ".txt"), ("All Files", ".*")]      
    )
    if not filepath:
        return
   
    with open(filepath, "w", encoding="utf-8") as file:
        text = txt_edit.get(1.0, END)
        file.write(text)
       
    window.title(f"Text Editor - {filepath}")

txt_edit = Text(window, bg="light green", fg = "black")


scrollbar = Scrollbar(txt_edit)
scrollbar.pack(side=RIGHT, fill=Y)

txt_edit.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=txt_edit.yview)

fr_buttons = Frame(window, relief=RAISED, bd=2)

btn_open = Button(fr_buttons, text="📂 Open", command=open_file)
btn_save = Button(fr_buttons, text="🗃️Save as", command=save_file)
