   
from tkinter import *
import tkinter as tk
from tkinter import ttk, scrolledtext
import sys
sys.path.append('../')
sys.path.append('./')
sys.path.append('./Python-compiler')

class ShowTableClass:
    def __init__(self, notebook):
        self.notebook = notebook
        self.create_show_table_tab()

    def create_show_table_tab(self):
        self.show_table = ttk.Frame(self.notebook)
        self.notebook.add(self.show_table, text="Show Table")
        self.create_show_table_widgets()

    def create_show_table_widgets(self):
        self.tree = ttk.Treeview(self.show_table)
        self.tree["columns"] = ("1", "2")
        self.tree.column("#0", width=100, minwidth=100, anchor='w')
        self.tree.column("1", width=200, minwidth=200, anchor='w')
        self.tree.column("2", width=100, minwidth=100, anchor='w')
        self.tree.heading("#0", text="ID", anchor='w')
        self.tree.heading("1", text="Name", anchor='w')
        self.tree.heading("2", text="Value", anchor='w')
        self.tree.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
