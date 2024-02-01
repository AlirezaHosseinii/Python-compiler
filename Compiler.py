from GUI.GUI import SqlIdleGUI
import tkinter as tk
import sys

#we can use is.arange for suggestion like :
#craete is not found : do you mean create ?

def main():
    root = tk.Tk()
    ide = SqlIdleGUI(root)
    root.mainloop()

main()

