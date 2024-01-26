import tkinter as tk
from tkinter import Label, ttk
from PIL import Image,ImageTk

class CreateUITableClass:
    def __init__(self, master, table_name, columns, notebook):
        self.master = master
        self.notebook = notebook
        self.table_name = table_name
        self.create_Lexical_tab()
        self.create_table_view(table_name, columns)

    def create_Lexical_tab(self):
        self.TABLE = ttk.Frame(self.notebook)
        self.notebook.add(self.TABLE, text=self.table_name)

        
        pil_image = Image.open('background.jpg')
        pil_image.resize((800, 600), Image.Resampling.LANCZOS)

        # Convert the PIL image to a Tkinter PhotoImage
        tk_image = ImageTk.PhotoImage(pil_image)
        

        # Create a Label with the image as the background
        background_label = Label(self.TABLE, image=tk_image, width=800, height=600)
        background_label.img = tk_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
    

    def create_table_view(self, table_name, columns):
        
        self.result_tree = ttk.Treeview(self.TABLE, columns=columns, show="headings", yscrollcommand=self.treeview_yscroll)

        for col in columns:
            self.result_tree.heading(col, text=col)

        self.result_tree.grid(row=3, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
        self.scrollbar = ttk.Scrollbar(self.TABLE, orient="vertical", command=self.result_tree.yview)
        self.result_tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=3, column=2, sticky="ns")

    def treeview_yscroll(self, *args):
        self.result_tree.yview(*args)


# def run_create_ui_table(table_name, columns):
#     root = tk.Tk()
#     create_ui_table = CreateUITableClass(root)
#     create_ui_table.create_table_view(table_name, columns)
#     root.mainloop()
