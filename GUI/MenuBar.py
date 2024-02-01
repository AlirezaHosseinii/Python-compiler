   
from tkinter import *
import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk

import sys
sys.path.append('../')
sys.path.append('./')
sys.path.append('./Python-compiler')
# from .GUITools import *
from .WorkBench import WorkBenchClass
from .LexicalAnalyzerGUI import LexicalAnalyzerGUIClass
from tkinter.colorchooser import askcolor

class MenuBarClass:
    def __init__(self, root:tk.Tk,workBench:WorkBenchClass,lexical:LexicalAnalyzerGUIClass):
        self.root = root
        self.workBench = workBench
        self.lexical = lexical
        self.menuBar = Menu(self.root)
        self.mode = tk.StringVar()
        self.mode.set('light')
        self.root.bind('<Control-r>', self.workBench.runCode)
        self.root.bind('<Control-f>', self.findText)
        self.root.bind('<Control-h>', self.findReplaceText)
        self.root.bind('<Control-o>',self.openFile)
        self.root.bind('<Control-s>',self.saveSqlFile)
        self.root.bind('<Control-Shift-S>',self.saveSqlFileAs)
        self.root.bind('<Control-q>',self.exitProgram)
        self.createFileMenu()
        self.createEditMenu()
        self.createRunMenu()
        self.createModeMenu()
        self.root.config(menu=self.menuBar)




    def createRunMenu(self):
        self.runBar = Menu(self.menuBar, tearoff=0)
        self.runBar.add_command(label='Run Code', command=self.workBench.runCode, accelerator='Ctrl+R')
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
        editBar.add_command(label='Horizontal Line', command=lambda: self.insertText('\n---\n'))
        editBar.add_command(label='Find', command=self.findText, accelerator='Ctrl+F')
        editBar.add_command(label='Find and Replace', command=self.findReplaceText, accelerator='Ctrl+H')
        self.menuBar.add_cascade(label='Edit', menu=editBar)

    def createFileMenu(self):
        fileBar = Menu(self.menuBar, tearoff=0)
        fileBar.add_command(label='Open', command=self.openFile, accelerator='Ctrl+O')
        fileBar.add_command(label='Save', command=self.saveSqlFile, accelerator='Ctrl+S')
        fileBar.add_command(label='Save As', command=self.saveSqlFileAs, accelerator='Ctrl+Shift+S')
        fileBar.add_separator()
        fileBar.add_command(label='Exit', command=self.exitProgram, accelerator='Ctrl+Q')
        self.menuBar.add_cascade(label='File', menu=fileBar)
        
    def createModeMenu(self):
        modeBar = Menu(self.menuBar, tearoff=0)
        modeBar.add_radiobutton(label='Dark Mode', variable=self.mode, value='dark', command=self.toggle_mode)
        modeBar.add_radiobutton(label='Light Mode', variable=self.mode, value='light', command=self.toggle_mode)
        modeBar.add_command(label='Change Background Color', command=self.change_background)
        self.menuBar.add_cascade(label='Mode', menu=modeBar)

    def openFile(self,event=None):
        path = askopenfilename(filetypes=[('text Files','*.txt'),('SQL Files', '*.sql')])
        if path:
            with open(path, 'r') as file:
                sql_code = file.read()
                self.workBench.query_text.delete('1.0', END)
                self.workBench.query_text.insert('1.0', sql_code)

    def saveSqlFile(self,event=None):
        if not hasattr(self, 'current_file_path') or self.current_file_path is None:
            self.saveSqlFileAs()
        else:
            with open(self.current_file_path, 'w') as file:
                file.write(self.workBench.query_text.get("1.0", tk.END))

    def saveSqlFileAs(self,event=None):
        file_path = asksaveasfilename(defaultextension=".txt",filetypes=[('text Files','*.txt'),('SQL Files', '*.sql')])

        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.workBench.query_text.get("1.0", tk.END))
            self.current_file_path = file_path

    def exitProgram(self,event=None):
        self.root.destroy()

    def copyText(self):
        self.workBench.query_text.clipboard_clear()
        selected_text = self.workBench.query_text.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.workBench.query_text.clipboard_append(selected_text)

    def pasteText(self):
        text_to_paste = self.workBench.query_text.clipboard_get()
        self.workBench.query_text.insert(tk.INSERT, text_to_paste)

    def cutText(self):
        self.copyText()
        self.workBench.query_text.delete(tk.SEL_FIRST, tk.SEL_LAST)

    def insertText(self, text):
        self.workBench.query_text.insert(tk.INSERT, text)

    def undoText(self):
        try:
            self.workBench.query_text.edit_undo()
        except :
            pass

    def redoText(self):
        try:
            self.workBench.query_text.edit_redo()
        except:
            pass
    
    def findText(self, event=None):
        self.find_window = tk.Toplevel(self.root)
        self.find_window.title("Find Text")
        self.find_window.geometry("300x60")
        tk.Label(self.find_window, text="Find:").pack(side=tk.LEFT, padx=10)
        self.find_entry = tk.Entry(self.find_window)
        self.find_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        self.find_entry.focus_set()
        find_button = tk.Button(self.find_window, text="Find", command=self.on_find)
        find_button.pack(side=tk.RIGHT, padx=10)
       
    def on_find(self):
        search_text = self.find_entry.get()
        if search_text:
            self.workBench.find_in_query_text(search_text)

    def findReplaceText(self, event=None):
        self.find_replace_window = tk.Toplevel(self.root)
        self.find_replace_window.title("Find and Replace")
        self.find_replace_window.geometry("300x100")
        tk.Label(self.find_replace_window, text="Find:").grid(row=0, column=0, padx=10, pady=5)
        self.find_text_entry = tk.Entry(self.find_replace_window)
        self.find_text_entry.grid(row=0, column=1, padx=5, pady=5)
        self.find_text_entry.focus_set()
        tk.Label(self.find_replace_window, text="Replace:").grid(row=1, column=0, padx=10, pady=5)
        self.replace_text_entry = tk.Entry(self.find_replace_window)
        self.replace_text_entry.grid(row=1, column=1, padx=5, pady=5)
        replace_button = tk.Button(self.find_replace_window, text="Replace", command=self.on_replace)
        replace_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)

    def on_replace(self):
        find_text = self.find_text_entry.get()
        replace_text = self.replace_text_entry.get()
        if find_text:
            self.workBench.replace_in_query_text(find_text, replace_text)

    def on_exit(self, event):
        #note
        self.conn.close()
        self.root.destroy()
        
    def change_background(self):
        color = askcolor()[1]
        if color:
            self.workBench.result_text.config(background=color)
            self.workBench.query_text.config(background=color)

    def toggle_mode(self):
        current_mode = self.mode.get()
        if current_mode == 'dark':
            self.apply_dark_mode()
        else:
            self.apply_light_mode()

    def apply_dark_mode(self):
        self.workBench.set_dark_background()
        self.lexical.set_dark_background()
        tables = self.workBench.tables
        for table in tables:
            table.set_dark_background()
        dark_bg = '#1e1e1e' 
        light_fg = '#d4d4d4'
        self.root.configure(bg=dark_bg)
        self.workBench.query_text.configure(bg=dark_bg, fg=light_fg, insertbackground=light_fg)
        self.workBench.result_text.configure(bg=dark_bg, fg=light_fg, insertbackground=light_fg)
        self.mode.set('dark')
 
    def apply_light_mode(self):
        self.workBench.set_background()
        self.lexical.set_background()
        tables = self.workBench.tables
        for table in tables:
            table.set_background()
        self.root.configure(bg='white')
        self.workBench.query_text.configure(bg='white', fg='black')
        self.workBench.result_text.configure(bg='white', fg='black')


        
