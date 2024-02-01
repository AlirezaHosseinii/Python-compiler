from tkinter import *
import tkinter as tk
from tkinter import ttk
import sys
sys.path.append('../')
sys.path.append('./')
sys.path.append('/')
sys.path.append('.')
sys.path.append('/.')
sys.path.append('/..')
sys.path.append('./Python-compiler')
from .WorkBench import WorkBenchClass
from .LexicalAnalyzerGUI import LexicalAnalyzerGUIClass
from .MenuBar import *
from .showTable import ShowTableClass
from createUItable import CreateUITableClass


class SqlIdleGUI:
    def __init__(self, root):
        self.root = root
        label = tk.Label(self.root, text="SQL COMPILER")
        label.pack()
        self.root.title("SQL COMPILER")
        self.root.geometry('800x600')
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, side='left') 
        self.workBenchTab = WorkBenchClass(self.notebook, self)
        self.lexicalAnalyzerTab = LexicalAnalyzerGUIClass(self.root,self.notebook,self.workBenchTab)
        #(self, root,query_text,result_text):
        self.menuBar = MenuBarClass(self.root,self.workBenchTab,self.lexicalAnalyzerTab)

# def main():
#     root = tk.Tk()
#     ide = SqlIdleGUI(root)
#     root.mainloop()

# main()
