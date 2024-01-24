   
from tkinter import *
import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter.filedialog import askopenfilename, asksaveasfilename
import sqlite3
import sys
import GUITools

from tkinter.colorchooser import askcolor

class LexicalAnalyzerClass:

    def __init__(self, root, notebook,menuBar):
        self.root = root
        self.notebook = notebook
        self.menuBar =menuBar
        self.create_Lexical_tab()

    def create_Lexical_tab(self):
        self.Lexical = ttk.Frame(self.notebook)
        self.notebook.add(self.Lexical, text="Lexical")
        self.create_widgets(self.Lexical)

    def create_widgets(self,Lexical):
        self.result_tree = ttk.Treeview(self.root, columns=("Token", "Type"), show="headings", yscrollcommand=self.treeview_yscroll)
        self.result_tree.heading("Token", text="Token")
        self.result_tree.heading("Type", text="Type")
        #self.result_tree.grid(row=0, column=1, rowspan=3, padx=5, pady=5, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.result_tree.yview)
        self.result_tree.configure(yscrollcommand=self.scrollbar.set)
        #self.scrollbar.grid(row=0, column=2, rowspan=3, sticky="ns")

    def treeview_yscroll(self, *args):
        self.result_tree.yview(*args)
"""""
    def analyze_text(self):
        text_to_analyze = self.text_entry.get()
        lexical_analyzer = LexicalAnalyzer(text_to_analyze)
        tokens = lexical_analyzer.analyze_line()

        for item in self.result_tree.get_children():
            self.result_tree.delete(item)

        for token in tokens:
            token_type = LexicalAnalyzer.get_type(token)
            self.result_tree.insert("", "end", values=(token, token_type))
"""