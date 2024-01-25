from PIL import ImageTk, Image as img
from tkinter import *
from tkinter import ttk, scrolledtext
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.colorchooser import askcolor
from .GUITools import *
from LexicalAnalyzerDir.LexicalAnalyzer import LexicalAnalyzerClass

class LexicalAnalyzerGUIClass:

    def __init__(self, root, notebook):
        self.root = root
        self.notebook = notebook
        self.create_Lexical_tab()
        self.create_widgets()

    def create_Lexical_tab(self):
        self.Lexical = ttk.Frame(self.notebook)
        self.notebook.add(self.Lexical, text="Lexical")

    def create_widgets(self):
        pil_image = img.open('background.jpg')
        pil_image.resize((800, 600), img.Resampling.LANCZOS)
        tk_image = ImageTk.PhotoImage(pil_image)

        background_label = Label(self.Lexical, image=tk_image, width=800, height=600)
        background_label.img = tk_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.text_label = ttk.Label(self.Lexical, text="Enter Text:")
        self.text_label.grid(row=0, column=0,sticky="w", padx=150, pady=15)

        self.text_entry = ttk.Entry(self.Lexical, width=50)
        self.text_entry.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
        self.text_entry.grid_configure(sticky="ew")  # Center the entry widget

        self.analyze_button = ttk.Button(self.Lexical, text="Analyze", command=self.analyze_text)
        self.analyze_button.grid(row=2, column=0, pady=5, columnspan=2)
        self.analyze_button.grid_configure(sticky="ew")  # Center the button widget

        self.result_tree = ttk.Treeview(self.Lexical, columns=("Token", "Type"), show="headings", yscrollcommand=self.treeview_yscroll)
        self.result_tree.heading("Token", text="Token")
        self.result_tree.heading("Type", text="Type")
        self.result_tree.grid(row=3, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)

        self.scrollbar = ttk.Scrollbar(self.Lexical, orient="vertical", command=self.result_tree.yview)
        self.result_tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=3, column=2, sticky="ns")

    def treeview_yscroll(self, *args):
        self.result_tree.yview(*args)

    def analyze_text(self):
        text_to_analyze = self.text_entry.get()
        lexical_analyzer = LexicalAnalyzerClass(text_to_analyze)
        tokens = lexical_analyzer.analyze_line()

        for item in self.result_tree.get_children():
            self.result_tree.delete(item)

        for token in tokens:
            token_type = lexical_analyzer.get_type(token)
            self.result_tree.insert("", "end", values=(token, token_type))
