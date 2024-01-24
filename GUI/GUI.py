from tkinter import *
import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter.filedialog import askopenfilename, asksaveasfilename
import sqlite3
import sys
from WorkBench import WorkBenchClass
from LexicalAnalyzerGUI import LexicalAnalyzerClass

# sys.path.insert(1, 'LexicalAnalyzer')
# from LexicalAnalyzer import LexicalAnalyzer

# sys.path.insert(1, 'SyntaxAnalyzer')
# sys.path.insert(1, 'InsertCommandSyntaxAnalyzer')
# from SyntaxAnalyzer import InsertCommandSyntaxAnalyzer

# from SyntaxAnalyzer import CreateTableSyntaxAnalyzer
# from tests import get_tests
from tkinter.colorchooser import askcolor



class SqlIdleWithLexicalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SQL COMPILER")
        self.root.geometry('800x600')
        self.test_value = 0
        self.mode = tk.StringVar()
        self.mode.set('light')

        self.dark_bg_color = 'black'
        self.light_bg_color = 'white'
        self.button_color = 'light blue'
        self.hover_color = 'yellow'
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, side='left') 
        menuBar = Menu(self.root)
        workBenchTab = WorkBenchClass(self.notebook,menuBar)
        lexicalAnalyzer = LexicalAnalyzerClass(self.root,self.notebook,menuBar)

        self.tree_page = ttk.Frame(self.notebook)
        self.lex_out_put = ttk.Frame(self.notebook)
        self.notebook.add(self.tree_page, text="OutPut")


        self.create_widgets(self.tree_page,menuBar)


    def create_widgets(self, tree_page,menuBar):
        self.tree = ttk.Treeview(tree_page)
        self.tree["columns"] = ("1", "2")
        self.tree.column("#0", width=100, minwidth=100, anchor='w')
        self.tree.column("1", width=200, minwidth=200, anchor='w')
        self.tree.column("2", width=100, minwidth=100, anchor='w')
        self.tree.heading("#0", text="ID", anchor='w')
        self.tree.heading("1", text="Name", anchor='w')
        self.tree.heading("2", text="Value", anchor='w')
        self.tree.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

        self.root.bind('<Control-c>', self.on_exit)



        fileBar = Menu(menuBar, tearoff=0)
        fileBar.add_command(label='Open', command=self.openSqlFile)
        fileBar.add_command(label='Save', command=self.saveSqlFile, accelerator='Ctrl+S')
        fileBar.add_command(label='Save As', command=self.saveSqlFileAs, accelerator='Ctrl+Shift+S')
        fileBar.add_separator()
        fileBar.add_command(label='Exit', command=self.exitProgram)
        menuBar.add_cascade(label='File', menu=fileBar)




        editBar = Menu(menuBar, tearoff=0)
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
        menuBar.add_cascade(label='Edit', menu=editBar)
        self.root.bind('<Control-f>', self.findText)
        self.root.bind('<Control-h>', self.findReplaceText)




        modeBar = Menu(menuBar, tearoff=0)
        # modeBar.add_radiobutton(label='Dark Mode', variable=self.mode, value='dark', command=self.toggle_mode)
        # modeBar.add_radiobutton(label='Light Mode', variable=self.mode, value='light', command=self.toggle_mode)
        menuBar.add_cascade(label='Mode', menu=modeBar)

        self.root.config(menu=menuBar)

        # self.toggle_mode()



    def change_background(self):
        color = askcolor()[1]
        if color:
            self.result_text.config(background=color)



    def execute_query(self):
        query = self.query_text.get("1.0", tk.END)
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, str(result))
        except Exception as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Error: {str(e)}")



    def on_exit(self, event):
        self.conn.close()
        self.root.destroy()

 
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

    # def runCode(self, event=None):
    #     try:
    #         self.result_text.delete(1.0, tk.END)
    #         query = self.query_text.get("1.0", tk.END)
    #         lexicalAnalyzer = LexicalAnalyzer(query.strip())
    #         Lexicaltokens = list(lexicalAnalyzer.analyze_line())
    #         print("Lexicaltokens are : ", Lexicaltokens)
    #         result = ""
    #         if Lexicaltokens[0].lower() == "insert":
    #             self.result_text.insert(tk.END, "checking insert query   :  ")
    #             syntaxAnalyzer = InsertCommandSyntaxAnalyzer.InsertCommandSyntaxAnalyzer(Lexicaltokens)
    #             result = syntaxAnalyzer.parse()
    #         elif Lexicaltokens[0].lower() == "create":
    #             self.result_text.insert(tk.END, "checking create query   :  ")
    #             syntaxAnalyzer = CreateTableSyntaxAnalyzer.CreateTableSyntaxAnalyzer(Lexicaltokens)
    #             result = syntaxAnalyzer.parse()
    #         else:
    #             self.show_error(f"The term '{Lexicaltokens[0]}' is not supported by this compiler.")

    #         print(f"result is {result}")
    #         self.result_text.insert(tk.END, result)
    #     except Exception as e:
    #         self.show_error(e)

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

    def on_execute_button_hover(self, event):
        self.execute_button.configure(bg=self.hover_color)

    def on_excute_button_leave(self, event):
        self.execute_button.configure(bg=self.button_color)

    def on_test_button_hover(self, event):
        self.test_button.configure(bg=self.hover_color)

    def on_test_button_leave(self, event):
        self.test_button.configure(bg=self.button_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = SqlIdleWithLexicalGUI(root)
    root.mainloop()
