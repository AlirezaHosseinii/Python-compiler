from GUI.GUI import SqlIdleGUI
from PIL import ImageTk
import tkinter as tk
from tkinter import Label, ttk
from PIL import Image,ImageTk
import sys

class WelcomeApp:
    def __init__(self, master):
        self.master = master
        master.title("Welcome")
        width = int(self.master.winfo_screenwidth() * 1) 
        height = int(self.master.winfo_screenheight() * 0.95)
        self.master.geometry(f"{width}x{height}+0+0")

        pil_image = Image.open('dark_background.jpg')
        tk_image = ImageTk.PhotoImage(pil_image)
        self.background_label:Label = Label(self.master, image=tk_image, width=800, height=600)
        self.background_label.img = tk_image
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame = tk.Frame(master)
        frame.pack(expand=True)

        click_here = tk.Button(frame, text="Click here to start!", command=self.open_sql_idle_gui,width=100, height=6)
        click_here.pack(side="top", anchor="center") 

    def exit_full_screen(self, event):
    # Exit full-screen mode when the Escape key is pressed
        self.master.attributes("-fullscreen", False)

    def open_sql_idle_gui(self):
        ide = SqlIdleGUI(self.master)
        self.master.destroy()
        
        root = tk.Tk()
        ide = SqlIdleGUI(root)
        self.root.mainloop()
        
def main():
    root = tk.Tk()
    app = WelcomeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

