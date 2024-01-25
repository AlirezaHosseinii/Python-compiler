   
from tkinter import *
import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter.filedialog import askopenfilename, asksaveasfilename

import sys
sys.path.append('../')
sys.path.append('./')
sys.path.append('./Python-compiler')
import GUITools
from WorkBench import WorkBenchClass
from tkinter.colorchooser import askcolor

class MenuBarClass:
    def __init__(self, root):
        self.menuBar = Menu(root)
        self.mode = tk.StringVar()
        self.mode.set('light')
        self.createFileMenu()
        self.createEditMenu()
        self.createRunMenu()
        self.createModeMenu()
        root.config(menu=self.menuBar)


    def createRunMenu(self):
        self.runBar = Menu(self.menuBar, tearoff=0)
        self.runBar.add_command(label='Run Code', command=WorkBenchClass.runCode, accelerator='Ctrl+R')
        self.menuBar.add_cascade(label='Run', menu=self.runBar)

    def createEditMenu(self):
        editBar = Menu(self.menuBar, tearoff=0)
        editBar.add_command(label='Copy', command=self.copyText, accelerator='Ctrl+C')
        editBar.add_command(label='Paste', command=self.pasteText, accelerator='Ctrl+V')
        editBar.add_command(label='Cut', command=self.cutText, accelerator='Ctrl+X')
        editBar.add_separator()
        editBar.add_command(label='Undo', command=self.undoText, accelerator='Ctrl+Z')
        editBar.add_command(label='Redo', command=self.redoText, accelerator='Ctrl+Y')
        editBar.add_separator()
        editBar.add_command(label='Change Background Color', command=self.change_background)
        editBar.add_command(label='Horizontal Line', command=lambda: self.insertText('\n---\n'))
        editBar.add_command(label='Find', command=self.findText, accelerator='Ctrl+F')
        editBar.add_command(label='Find and Replace', command=self.findReplaceText, accelerator='Ctrl+H')
        self.menuBar.add_cascade(label='Edit', menu=editBar)

    def createFileMenu(self):
        fileBar = Menu(self.menuBar, tearoff=0)
        fileBar.add_command(label='Open', command=self.openSqlFile, accelerator='Ctrl+O')
        fileBar.add_command(label='Save', command=self.saveSqlFile, accelerator='Ctrl+S')
        fileBar.add_command(label='Save As', command=self.saveSqlFileAs, accelerator='Ctrl+Shift+S')
        fileBar.add_separator()
        fileBar.add_command(label='Exit', command=self.exitProgram, accelerator='Ctrl+Q')
        self.menuBar.add_cascade(label='File', menu=fileBar)
        
    def createModeMenu(self):
        modeBar = Menu(self.menuBar, tearoff=0)
        modeBar.add_radiobutton(label='Dark Mode', variable=self.mode, value='dark', command=self.toggle_mode)
        modeBar.add_radiobutton(label='Light Mode', variable=self.mode, value='light', command=self.toggle_mode)
        self.menuBar.add_cascade(label='Mode', menu=modeBar)

    def openSqlFile(self):
        path = askopenfilename(filetypes=[('SQL Files', '*.sql')])

        if path:
            with open(path, 'r') as file:
                sql_code = file.read()
                self.query_text.delete('1.0', END)
                self.query_text.insert('1.0', sql_code)

    def saveSqlFile(self):
        if not hasattr(self, 'current_file_path') or self.current_file_path is None:
            self.saveSqlFileAs()
        else:
            with open(self.current_file_path, 'w') as file:
                file.write(self.query_text.get("1.0", tk.END))

    def saveSqlFileAs(self):
        file_path = asksaveasfilename(defaultextension=".sql", filetypes=[('SQL Files', '*.sql')])

        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.query_text.get("1.0", tk.END))
            self.current_file_path = file_path

    def exitProgram(self):
        self.root.destroy()

    def copyText(self):
        self.query_text.clipboard_clear()
        selected_text = self.query_text.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.query_text.clipboard_append(selected_text)

    def pasteText(self):
        text_to_paste = self.query_text.clipboard_get()
        self.query_text.insert(tk.INSERT, text_to_paste)

    def cutText(self):
        self.copyText()
        self.query_text.delete(tk.SEL_FIRST, tk.SEL_LAST)

    def insertText(self, text):
        self.query_text.insert(tk.INSERT, text)

    def undoText(self):
        try:
            self.query_text.edit_undo()
        except Exception as e:
            pass

    def redoText(self):
        try:
            self.query_text.edit_redo()
        except Exception as e:
            pass

    def findText(self, event=None):
        pass

    def findReplaceText(self, event=None):
        pass

    def on_exit(self, event):
        self.conn.close()
        self.root.destroy()
        
    def change_background(self):
        color = askcolor()[1]
        if color:
            self.result_text.config(background=color)

    def toggle_mode(self):
        pass