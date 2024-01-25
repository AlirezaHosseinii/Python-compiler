import tkinter as tk
from tkinter import Label, ttk, scrolledtext
from .GUITools import *
import sys
from PIL import Image, ImageTk


sys.path.append('../')
sys.path.append('./')
sys.path.append('/')
sys.path.append('.')
sys.path.append('/.')
sys.path.append('/..')
sys.path.append('./Python-compiler')
from SyntaxAnalyzer.InsertCommandSyntaxAnalyzer import InsertCommandSyntaxAnalyzerClass
from SyntaxAnalyzer.CreateTableSyntaxAnalyzer import CreateTableSyntaxAnalyzerClass
from LexicalAnalyzerDir.LexicalAnalyzer import LexicalAnalyzerClass
from tests import get_tests


class WorkBenchClass:
    def __init__(self, notebook):
        self.notebook = notebook
        self.test_value = 0
        self.create_workbench_tab()

    def create_workbench_tab(self):
        self.WorkBench = ttk.Frame(self.notebook)
        self.notebook.add(self.WorkBench, text="WorkBench")
        self.create_widgets()

    def create_widgets(self):
        self.create_query_text()
        self.create_run_button()
        self.create_test_button()
        self.create_result_text()
        self.WorkBench.grid_rowconfigure(0, weight=1)
        self.WorkBench.grid_rowconfigure(1, weight=0)
        self.WorkBench.grid_rowconfigure(2, weight=0)
        self.WorkBench.grid_rowconfigure(3, weight=1)
        self.WorkBench.grid_columnconfigure(0, weight=1)
        self.WorkBench.grid_columnconfigure(1, weight=1)

    def create_query_text(self):

        
         #Load the PIL image

        pil_image = Image.open('background.jpg')
        print(self.WorkBench.winfo_reqwidth())
        pil_image.resize((800, 600), Image.Resampling.LANCZOS)

        # Convert the PIL image to a Tkinter PhotoImage
        tk_image = ImageTk.PhotoImage(pil_image)
        

        # Create a Label with the image as the background
        background_label = Label(self.WorkBench, image=tk_image, width=800, height=600)
        background_label.img = tk_image

        # Adjust relwidth to make the background stretch to the width of the query text box
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # query_text_width = self.WorkBench.winfo_reqwidth()
        # query_text_height = int(self.WorkBench.winfo_reqheight() * 0.3)

        self.query_text = scrolledtext.ScrolledText(self.WorkBench, wrap=tk.WORD, width=80, height=15, font=("Arial", 12))
        self.query_text.grid(row=0, column=0, padx=100, pady=100, columnspan=2, sticky="nsew")


        



    def create_run_button(self):
        self.execute_button = tk.Button(self.WorkBench, text="Run Code", command=self.runCode, bg=button_color,
                                        width = 25, height=2)
        self.execute_button.bind("<Enter>", on_execute_button_hover)
        self.execute_button.bind("<Leave>", on_excute_button_leave)
        self.execute_button.grid(row=1, column=0, columnspan=2, sticky="nsew")

    def create_test_button(self):
        self.test_button = tk.Button(self.WorkBench, text="Run TEST", command=self.runTests, bg=button_color,
                                     width=50, height=2)
        self.test_button.bind("<Enter>", on_test_button_hover)
        self.test_button.bind("<Leave>", on_test_button_leave)
        self.test_button.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=(5, 0))

    def create_result_text(self):
        self.result_text = scrolledtext.ScrolledText(self.WorkBench, wrap=tk.WORD, width=80, height=15,
                                                     font=("Arial", 12))
        self.result_text.grid(row=3, column=0, padx=100, pady=100, columnspan=2, sticky="nsew")

    def runCode(self, event=None):
        try:
            self.result_text.delete(1.0, tk.END)
            query = self.query_text.get("1.0", tk.END)
            lexicalAnalyzer = LexicalAnalyzerClass(query.strip())
            Lexicaltokens = list(lexicalAnalyzer.analyze_line())
            print("Lexicaltokens are : ", Lexicaltokens)
            result = ""
            if Lexicaltokens[0].lower() == "insert":
                self.result_text.insert(tk.END, "checking insert query   :  ")
                syntaxAnalyzer = InsertCommandSyntaxAnalyzerClass(Lexicaltokens)
                result = syntaxAnalyzer.parse()
            elif Lexicaltokens[0].lower() == "create":
                self.result_text.insert(tk.END, "checking create query   :  ")
                syntaxAnalyzer = CreateTableSyntaxAnalyzerClass(Lexicaltokens)
                result = syntaxAnalyzer.parse()
            else:
                self.show_error(f"The term '{Lexicaltokens[0]}' is not supported by this compiler.")

            print(f"result is {result}")
            self.result_text.insert(tk.END, result)
        except Exception as e:
            self.show_error(e)

    def runTests(self, event=None):
        self.query_text.delete(1.0, tk.END)
        self.result_text.delete(1.0, tk.END)
        try:
            tests = get_tests("insert")
            if self.test_value == len(tests):
                return
            query = tests[self.test_value]["TEST" + str(self.test_value + 1)]
            print("checking test", self.test_value, "  :  ", query)
            self.query_text.insert(tk.END, query.strip())
            self.runCode()
            self.test_value += 1
        except Exception as e:
            self.show_error(e)

    def show_error(self, error):
        print("i got error: ", error)
        self.result_text.insert(tk.END, f"Error: {str(error)}")