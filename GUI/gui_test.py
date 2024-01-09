from tkinter import *
import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter.filedialog import askopenfilename, asksaveasfilename
import sqlite3

class SqlIdleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SQL IDE")
        self.root.geometry('800x600')

        self.mode = tk.StringVar()
        self.mode.set('light')  # Initial mode: light

        # Color settings for dark and light modes
        self.dark_bg_color = 'black'
        self.light_bg_color = 'white'
        self.button_color = 'light blue'
        self.hover_color = 'yellow'

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, side='left')  # Placing the notebook on the left side

        self.tree_page = ttk.Frame(self.notebook)
        self.result_page = ttk.Frame(self.notebook)

        self.notebook.add(self.result_page, text="WorkBench")
        self.notebook.add(self.tree_page, text="OutPut")

        self.create_widgets(self.tree_page, self.result_page)

    def create_widgets(self, tree_page, result_page):
        # Tree page widgets
        self.tree = ttk.Treeview(tree_page)
        self.tree["columns"] = ("1", "2")
        self.tree.column("#0", width=100, minwidth=100, anchor='w')
        self.tree.column("1", width=200, minwidth=200, anchor='w')
        self.tree.column("2", width=100, minwidth=100, anchor='w')
        self.tree.heading("#0", text="ID", anchor='w')
        self.tree.heading("1", text="Name", anchor='w')
        self.tree.heading("2", text="Value", anchor='w')
        self.tree.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Result page widgets
        self.query_text = scrolledtext.ScrolledText(result_page, wrap=tk.WORD, width=80, height=15, font=("Arial", 12))
        self.query_text.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.execute_button = tk.Button(result_page, text="Run Code", command=self.runCode, bg=self.button_color, width=100, height=2)
        self.execute_button.grid(row=1, column=0, pady=10)
        self.execute_button.bind("<Enter>", self.on_button_hover)
        self.execute_button.bind("<Leave>", self.on_button_leave)

        self.result_text = scrolledtext.ScrolledText(result_page, wrap=tk.WORD, width=80, height=15, font=("Arial", 12))
        self.result_text.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        # Error text widget
        self.error_text = scrolledtext.ScrolledText(result_page, wrap=tk.WORD, width=80, height=15, font=("Arial", 12))
        self.error_text.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        # SQLite database connection
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

        # Bind the exit event to handle KeyboardInterrupt
        self.root.bind('<Control-c>', self.on_exit)

        # Add File menu
        menuBar = Menu(self.root)
        fileBar = Menu(menuBar, tearoff=0)
        fileBar.add_command(label='Open', command=self.openSqlFile)
        fileBar.add_command(label='Save', command=self.saveSqlFileAs)
        fileBar.add_command(label='SaveAs', command=self.saveSqlFileAs)
        fileBar.add_separator()
        fileBar.add_command(label='Exit', command=self.exitProgram)
        menuBar.add_cascade(label='File', menu=fileBar)

        # Add Edit menu
        editBar = Menu(menuBar, tearoff=0)
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
        menuBar.add_cascade(label='Edit', menu=editBar)
        self.root.bind('<Control-f>', self.findText)  # Adding shortcut Ctrl + F for find text
        self.root.bind('<Control-h>', self.findReplaceText)  # Adding shortcut Ctrl + H for find and replace text

        # Add Run menu
        runBar = Menu(menuBar, tearoff=0)
        runBar.add_command(label='Run Code', command=self.runCode, accelerator='Ctrl+R')
        menuBar.add_cascade(label='Run', menu=runBar)
        self.root.bind('<Control-r>', self.runCode)  # Adding shortcut Ctrl + R for run code

        # Add Mode menu
        modeBar = Menu(menuBar, tearoff=0)
        modeBar.add_radiobutton(label='Dark Mode', variable=self.mode, value='dark', command=self.toggle_mode)
        modeBar.add_radiobutton(label='Light Mode', variable=self.mode, value='light', command=self.toggle_mode)
        menuBar.add_cascade(label='Mode', menu=modeBar)

        self.root.config(menu=menuBar)

        # Default color settings
        self.toggle_mode()

    def toggle_mode(self):
        current_mode = self.mode.get()
        if current_mode == 'dark':
            # Settings for dark mode
            self.root.configure(bg=self.dark_bg_color)
            self.tree.configure(style='Dark.Treeview')  # Setting style for Treeview
            self.query_text.configure(bg=self.dark_bg_color, fg='white')  # Setting background color and text color for ScrolledText
            self.result_text.configure(bg=self.dark_bg_color, fg='white')  # Setting background color and text color for ScrolledText
        else:
            # Settings for light mode
            self.root.configure(bg=self.light_bg_color)
            self.tree.configure(style='Light.Treeview')  # Setting style for Treeview
            self.query_text.configure(bg=self.light_bg_color, fg='black')  # Setting background color and text color for ScrolledText
            self.result_text.configure(bg=self.light_bg_color, fg='black')  # Setting background color and text color for ScrolledText

    def execute_query(self):
        query = self.query_text.get("1.0", tk.END)
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, str(result))
        except Exception as e:
            self.error_text.delete(1.0, tk.END)
            self.error_text.insert(tk.END, f"Error: {str(e)}")

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
                global gpath
                gpath = path

    def saveSqlFileAs(self):
        global gpath
        if gpath == '':
            path = asksaveasfilename(filetypes=[('SQL Files', '*.sql')])
        else:
            path = gpath

        with open(path, 'w', encoding='utf-8') as file:
            sql_code = self.query_text.get('1.0', END)
            file.write(sql_code)

    def exitProgram(self):
        self.root.destroy()

    def runCode(self, event=None):
        query = self.query_text.get("1.0", tk.END)
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, str(result))
        except Exception as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Error: {str(e)}")

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
        # Your find text implementation here
        pass

    def findReplaceText(self, event=None):
        # Your find and replace text implementation here
        pass

    def on_button_hover(self, event):
        self.execute_button.configure(bg=self.hover_color)

    def on_button_leave(self, event):
        self.execute_button.configure(bg=self.button_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = SqlIdleGUI(root)
    root.mainloop()
