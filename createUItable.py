import tkinter as tk
from tkinter import Label, ttk
from PIL import Image,ImageTk
# from GUI.MenuBar import MenuBarClass

class CreateUITableClass:
    def __init__(self, master, table_name, columns, notebook):
        self.master = master
        self.notebook = notebook
        self.columns = columns
        self.table_name = table_name
        self.create_Lexical_tab()
        self.create_table_view(table_name, columns)
        self.set_background()
        # if menubarclass.mode == "light" else dark background
        
    def set_background(self):
        pil_image = Image.open('background.jpg')
        print(self.TABLE.winfo_reqwidth())
        tk_image = ImageTk.PhotoImage(pil_image)
        self.background_label:Label = Label(self.TABLE, image=tk_image, width=800, height=600)
        self.background_label.img = tk_image
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_table_view(self.table_name, self.columns)

    def set_dark_background(self):
        pil_image = Image.open('dark_background.jpg')
        tk_image = ImageTk.PhotoImage(pil_image)
        self.background_label = Label(self.TABLE, image=tk_image, width=800, height=600)
        self.background_label.img = tk_image
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_table_view(self.table_name, self.columns)

    def create_Lexical_tab(self):
        self.TABLE = ttk.Frame(self.notebook)
        self.notebook.add(self.TABLE, text=self.table_name)

        
        pil_image = Image.open('background.jpg')
        pil_image.resize((800, 600), Image.Resampling.LANCZOS)

        tk_image = ImageTk.PhotoImage(pil_image)
        
        background_label = Label(self.TABLE, image=tk_image, width=800, height=600)
        background_label.img = tk_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.TABLE.grid_rowconfigure(3, weight=1)
        self.TABLE.grid_columnconfigure(0, weight=1)


    def create_table_view(self, table_name, columns):
        self.result_tree = ttk.Treeview(self.TABLE, columns=columns, show="headings", yscrollcommand=self.treeview_yscroll)

        for col in columns:
            self.result_tree.heading(col, text=col)
            self.result_tree.column(col, anchor="center")

        self.result_tree.grid(row=3, column=0,columnspan=2, padx=150, pady=5, sticky="nsew")
        
        self.scrollbar = ttk.Scrollbar(self.TABLE, orient="vertical", command=self.result_tree.yview)
        self.result_tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=3, column=2, padx=0 , sticky="nsew")

        self.TABLE.grid_rowconfigure(3, weight=1)
        self.TABLE.grid_columnconfigure(0, weight=1)

    def treeview_yscroll(self, *args):
        self.result_tree.yview(*args)


    def change_columns(self, columns) :
        self.result_tree = ttk.Treeview(self.TABLE, columns=columns, show="headings", yscrollcommand=self.treeview_yscroll)

        for col in columns:
            self.result_tree.heading(col, text=col)        

    def insert_data(self, column_name, values):
        self.result_tree.insert("", "end", values=values)        


    def treeview_yscroll(self, *args):
        self.result_tree.yview(*args)

