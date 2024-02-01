import tkinter as tk
from tkinter import Label, ttk, scrolledtext
from .GUITools import GUIToolsCLass
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
from SyntaxAnalyzer.AlterTableSyntaxAnlyzer import AlterTableSyntaxAnalyzerClass
from tests import get_tests
from createUItable import CreateUITableClass


class WorkBenchClass:
    sql_idle_gui_instance = None
    def __init__(self, notebook, sql_idle_gui_instance):
        WorkBenchClass.sql_idle_gui_instance = sql_idle_gui_instance
        self.notebook = notebook
        self.test_value = 0
        self.guiTools = GUIToolsCLass(self)
        self.create_workbench_tab()
        self.tables = []

    def create_workbench_tab(self):
        self.WorkBench = ttk.Frame(self.notebook)
        self.notebook.add(self.WorkBench, text="WorkBench")
        self.set_background()

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

    def set_background(self):
        pil_image = Image.open('background.jpg')
        print(self.WorkBench.winfo_reqwidth())
        tk_image = ImageTk.PhotoImage(pil_image)
        self.background_label:Label = Label(self.WorkBench, image=tk_image, width=800, height=600)
        self.background_label.img = tk_image
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_widgets()

    def set_dark_background(self):
        pil_image = Image.open('dark_background.jpg')
        tk_image = ImageTk.PhotoImage(pil_image)
        self.background_label = Label(self.WorkBench, image=tk_image, width=800, height=600)
        self.background_label.img = tk_image
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_widgets()
        
    def create_query_text(self):
        self.query_text = scrolledtext.ScrolledText(self.WorkBench, width=200, height=200, font=("Arial", 11),undo=True)
        self.query_text.grid(row=0, column=0, padx=80, pady=50, columnspan=2, sticky="nsew")
    
    def create_run_button(self):
        self.execute_button = tk.Button(self.WorkBench, text="Run Code", command=self.runCode, bg=self.guiTools.button_color,
                                        width = 25, height=2)
        self.execute_button.bind("<Enter>",self.guiTools.on_execute_button_hover)
        self.execute_button.bind("<Leave>", self.guiTools.on_excute_button_leave)
        self.execute_button.grid(row=1, column=0, columnspan=2, sticky="nsew")

    def create_test_button(self):
        self.test_button = tk.Button(self.WorkBench, text="Run TEST", command=self.runTests, bg=self.guiTools.button_color,
                                     width=50, height=2)
        self.test_button.bind("<Enter>", self.guiTools.on_test_button_hover)
        self.test_button.bind("<Leave>", self.guiTools.on_test_button_leave)
        self.test_button.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=(5, 0))

    def create_result_text(self):
        self.result_text = scrolledtext.ScrolledText(self.WorkBench, width=200, height=200,
                                                     font=("Arial", 11),undo=True)
        self.result_text.grid(row=3, column=0, padx=80, pady=50, columnspan=2, sticky="nsew")

    def runCode(self, event=None):
        try:
            self.result_text.delete(1.0, tk.END)
            query = self.query_text.get("1.0", tk.END)
            lexicalAnalyzer = LexicalAnalyzerClass(query.strip())
            Lexicaltokens:list[str] = list(lexicalAnalyzer.analyze_line())
            print("Lexicaltokens are : ", Lexicaltokens)
            result = ""
            if Lexicaltokens[0].lower() == "insert":
                self.result_text.insert(tk.END, "checking insert query   :  ")
                syntaxAnalyzer = InsertCommandSyntaxAnalyzerClass(Lexicaltokens)
                result, column_list , values_list = syntaxAnalyzer.parse()
                if(result == "Accepted."):
                    for table in self.tables:
                        table.insert_data(table.table_name,values_list) #INSERT INTO Books(BookID, Title) VALUES (a , e);        

            elif Lexicaltokens[0].lower() == "create":
                self.result_text.insert(tk.END, "checking create query   :  ")
                syntaxAnalyzer = CreateTableSyntaxAnalyzerClass(Lexicaltokens)
                result, table_name, columns = syntaxAnalyzer.parse()
                if(result == "Accepted."):
                    print(table_name)
                    print(columns)
                    create_ui_table = CreateUITableClass(self.sql_idle_gui_instance.root, table_name, columns, self.sql_idle_gui_instance.notebook)
                    self.tables.append(create_ui_table)
            elif Lexicaltokens[0].lower() == "alter":
                self.result_text.insert(tk.END, "checking alter query   :  ")
                syntaxAnalyzer = AlterTableSyntaxAnalyzerClass(Lexicaltokens)
                result = syntaxAnalyzer.parse()
            else:
                self.show_error(f"The term '{Lexicaltokens[0]}' is not supported by this compiler.")

            print(f"result is {result}")
            self.result_text.insert(tk.END, result)
        except Exception as e:
            self.show_error(e)

    def find_in_query_text(self, search_text:str):
            self.query_text.tag_remove('found', '1.0', tk.END)
            start_pos = '1.0'
            while True:
                start_pos = self.query_text.search(search_text.lower(), start_pos,nocase=True,exact=False, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(search_text)}c"
                self.query_text.tag_add('found', start_pos, end_pos)
                start_pos = end_pos
            self.query_text.tag_config('found', foreground='black', background='yellow')

    def replace_in_query_text(self, find_text, replace_text):
        start_pos = '1.0'
        while True:
            start_pos = self.query_text.search(find_text.lower(), start_pos,nocase=True,exact=False, stopindex=tk.END)
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(find_text)}c"
            self.query_text.delete(start_pos, end_pos)
            self.query_text.insert(start_pos, replace_text)
            start_pos = f"{start_pos}+{len(replace_text)}c"

    def runTests(self, event=None):
        self.query_text.delete(1.0, tk.END)
        self.result_text.delete(1.0, tk.END)
        try:
            tests = get_tests("insert")
            if self.test_value == len(tests):
                return
            query:str = tests[self.test_value]["TEST" + str(self.test_value + 1)]
            print("checking test", self.test_value, "  :  ", query)
            self.query_text.insert(tk.END, query.strip())
            self.runCode()
            self.test_value += 1
        except Exception as e:
            self.show_error(e)

    def show_error(self, error):
        print("i got error: ", error)
        self.result_text.insert(tk.END, f"Error: {str(error)}")