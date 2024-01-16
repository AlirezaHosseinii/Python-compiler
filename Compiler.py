from GUI import SqlIdleGUI
import tkinter as tk

#text type

#fails with Price DECIMAL(10, 2)

#check numeric for decimal and float and ...

#if primary should not be unique and .... (constraint conflict)

#if table exists

#we can use is.arange for suggestion like :
#craete is not found : do you mean create ?

#ready buttons for ready query like create insert alter (idea from phpmyAdmin)

#should sync self.reserved_keywords in classes

def main():
    root = tk.Tk()
    ide = SqlIdleGUI(root)
    root.mainloop()

main()
