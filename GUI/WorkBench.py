   
from tkinter import *
import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter.filedialog import askopenfilename, asksaveasfilename
import sqlite3
import sys
import GUITools

from tkinter.colorchooser import askcolor

class WorkBenchClass:

    def __init__(self, notebook):
        self.notebook = notebook
        self.create_workbench_tab()

    def create_workbench_tab(self):
        self.WorkBench = ttk.Frame(self.notebook)
        self.notebook.add(self.WorkBench, text="WorkBench")
        self.create_widgets(self.WorkBench)

    def create_widgets(self,WorkBench):
        query_text = scrolledtext.ScrolledText(WorkBench, wrap=tk.WORD, width=80, height=15, font=("Arial", 12))
        query_text.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")
        execute_button = tk.Button(WorkBench, text="Run Code", command=self.runCode, bg=GUITools.button_color,
                                        width=50, height=2)
        execute_button.bind("<Enter>", GUITools.on_execute_button_hover)
        execute_button.bind("<Leave>", GUITools.on_excute_button_leave)
        execute_button.grid(row=1, column=0, columnspan=2, sticky="nsew")

        test_button = tk.Button(WorkBench, text="Run TEST", command=self.runTests, bg=GUITools.button_color,
                                        width=50, height=2)
        test_button.bind("<Enter>", GUITools.on_test_button_hover)
        test_button.bind("<Leave>", GUITools.on_test_button_leave)
        test_button.grid(row=2, column=0, columnspan=2, sticky="nsew")

        result_text = scrolledtext.ScrolledText(WorkBench, wrap=tk.WORD, width=80, height=15, font=("Arial", 12))
        result_text.grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")
        WorkBench.grid_rowconfigure(0, weight=1)
        WorkBench.grid_rowconfigure(1, weight=0)
        WorkBench.grid_rowconfigure(2, weight=0)
        WorkBench.grid_rowconfigure(3, weight=1)
        WorkBench.grid_columnconfigure(0, weight=1)
        WorkBench.grid_columnconfigure(1, weight=1)
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()

    def runCode(self):
            # try:
            #     self.WorkBench.delete(1.0, tk.END)
            #     query = query_text.get("1.0", tk.END)
            #     lexicalAnalyzer = LexicalAnalyzer(query.strip())
            #     Lexicaltokens = list(lexicalAnalyzer.analyze_line())
            #     print("Lexicaltokens are : ", Lexicaltokens)
            #     result = ""
            #     if Lexicaltokens[0].lower() == "insert":
            #         result_text.insert(tk.END, "checking insert query   :  ")
            #         syntaxAnalyzer = InsertCommandSyntaxAnalyzer.InsertCommandSyntaxAnalyzer(Lexicaltokens)
            #         result = syntaxAnalyzer.parse()
            #     elif Lexicaltokens[0].lower() == "create":
            #         result_text.insert(tk.END, "checking create query   :  ")
            #         syntaxAnalyzer = CreateTableSyntaxAnalyzer.CreateTableSyntaxAnalyzer(Lexicaltokens)
            #         result = syntaxAnalyzer.parse()
            #     else:
            #         show_error(f"The term '{Lexicaltokens[0]}' is not supported by this compiler.")

            #     print(f"result is {result}")
            #     result_text.insert(tk.END, result)
            # except Exception as e:
            #     show_error(e)
        pass
    
    def runTests(self, event=None):
        pass
        # self.query_text.delete(1.0, tk.END)
        # self.result_text.delete(1.0, tk.END)
        # try:
        #     tests = get_tests("insert")
        #     if self.test_value == len(tests):
        #         return
        #     query = tests[self.test_value]["TEST" + str(self.test_value + 1)]
        #     print("checking test", self.test_value, "  :  ", query)
        #     self.query_text.insert(tk.END, query.strip())
        #     self.runCode()
        #     self.test_value += 1
        # except Exception as e:
        #     self.show_error(e)

    def show_error(self, error):
        pass
        # print("i got error: ", error)
        # self.result_text.insert(tk.END, f"Error: {str(error)}")
