from tkinter import *
import tkinter as tk
from LexicalAnalyzerDir.LexicalAnalyzer import LexicalAnalyzerClass
from tkinter import Label, ttk, scrolledtext
from PIL import Image, ImageTk
from .WorkBench import WorkBenchClass
from .GUITools import *

class LexicalAnalyzerGUIClass:
    def __init__(self, root:tk.Tk, notebook,workBench:WorkBenchClass):
        self.root = root
        self.notebook = notebook
        self.workBench = workBench
        self.create_Lexical_tab()
        self.set_dark_background()

    def create_Lexical_tab(self):
        self.Lexical = ttk.Frame(self.notebook)
        self.notebook.add(self.Lexical, text="Lexical")

    def create_lexical_widgets(self):
        self.text_label = ttk.Label(self.Lexical, text=" Enter Text : ")
        self.text_label.grid(row=0, column=0, sticky="w", padx=150, pady=15)

        self.text_entry = scrolledtext.ScrolledText(self.Lexical, width=50, height=5)
        self.text_entry.grid(row=1, column=0,columnspan=2, padx=150, pady=5, sticky="ew")

        self.analyze_button = ttk.Button(self.Lexical, text="Analyze ", command=self.analyze_text)
        self.analyze_button.grid(row=2, column=0, padx=(150,5), pady=5, sticky="ew")

        self.get_from_workbench_button = ttk.Button(self.Lexical, text="Get From WorkBench", command=self.get_text_from_workbench)
        self.get_from_workbench_button.grid(row=2, column=1, padx=(5,150), pady=5, sticky="ew")

        self.result_tree = ttk.Treeview(self.Lexical, columns=("Token", "Type"), show="headings")
        self.result_tree.heading("Token", text="Token")
        self.result_tree.heading("Type", text="Type")
        self.result_tree.grid(row=3, column=0,columnspan=2, padx=150, pady=5, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self.Lexical, orient="vertical", command=self.result_tree.yview)
        self.result_tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=3, column=2, padx=0 , sticky="nsew")

        self.Lexical.grid_rowconfigure(3, weight=1)
        self.Lexical.grid_columnconfigure(0, weight=1)

    def treeview_yscroll(self, *args):
        self.result_tree.yview(*args)

    def set_background(self):
        pil_image = Image.open('background.jpg')
        tk_image = ImageTk.PhotoImage(pil_image)
        self.background_label:Label = Label(self.Lexical, image=tk_image, width=800, height=600)
        self.background_label.img = tk_image
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        current_mode = 'light'
        self.create_lexical_widgets()

    def set_dark_background(self):
        pil_image = Image.open('dark_background.jpg')
        tk_image = ImageTk.PhotoImage(pil_image)
        self.background_label = Label(self.Lexical, image=tk_image, width=1024, height=1024)
        self.background_label.img = tk_image
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        current_mode = 'dark'
        self.create_lexical_widgets()  

    def get_text_from_workbench(self):
        self.text_entry.delete(1.0, tk.END)
        self.text_entry.insert(tk.END, self.workBench.query_text.get("1.0", tk.END))

    def analyze_text(self):
        text_to_analyze = self.text_entry.get("1.0", tk.END)
        lexical_analyzer = LexicalAnalyzerClass(text_to_analyze)
        tokens = lexical_analyzer.analyze_line()

        for item in self.result_tree.get_children():
            self.result_tree.delete(item)

        for token in tokens:
            token_type = lexical_analyzer.get_type(token)
            self.result_tree.insert("", "end", values=(token, token_type))
