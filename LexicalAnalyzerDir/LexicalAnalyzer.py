from enum import Enum
import re
import tkinter as tk
from tkinter import ttk

class LexicalKind(Enum):
    COMMA = ","
    OPEN_PARANTHESIS = "("
    CLOSE_PARANTHESIS = ")"
    INT = "Int"
    FLOAT = "Float"
    DOT = "."
    WHITESPACE = "WhiteSpace"
    IDENTIFIER = "Identifier"
    KEYWORD = "Keyword"
    SEMI_COLON = "SemiColon"
    PLUS_OPERATION = "PlusOperation"
    EQUAL_OPERATION = "EqualOperation"
    UNEQUAL_OPERATION = "UnequalOperation"
    LESS_OPERATION = "LessOperation"
    MORE_OPERATION = "MoreOperation"
    LESS_EQUAL_OPERATION = "LESSEQUALOperation"
    MORE_EQUAL_OPERATION = "MOREEQUALOperation"
    MINUS_OPERATION = "MinusOperation" 
    DIVIDE_OPERATION = "DivideOperation"
    MULTIPLE_OPERATION = "MultipleOperation" 
    COLON = "Colon"
    ASSIGNMENT_OPERATION = "AssignmentOperation" 
    UNDEFINED = "Undefined"
    SPACE = "Space"

class LexicalAnalyzerClass:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def get_type(word):
        if re.match(r'\d+(\.\d+)?$' ,word):
            if re.match(r'\d+\.\d+?$', word):
                return LexicalKind.FLOAT.name
            else:    
                return LexicalKind.INT.name
        elif word == "+":
            return LexicalKind.PLUS_OPERATION.name
        elif word == "-":
            return LexicalKind.MINUS_OPERATION.name
        elif word == "/":
            return LexicalKind.DIVIDE_OPERATION.name
        elif word == "*":
            return LexicalKind.MULTIPLE_OPERATION.name
        elif word == ":":
            return LexicalKind.COLON.name
        elif word == ";":
            return LexicalKind.SEMI_COLON.name
        elif word == ",":
            return LexicalKind.COMMA.name
        elif word == "(":
            return LexicalKind.OPEN_PARANTHESIS.name
        elif word == ")":
            return LexicalKind.CLOSE_PARANTHESIS.name
        elif re.match(r'^[a-zA-Z_]\w*(\d* | [a-zA-Z_]*)?$', word): 
            keywords = ["SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER",
            "JOIN", "INNER", "LEFT", "RIGHT", "FULL", "WHERE", "GROUP BY", "ORDER BY",
            "HAVING", "UNION", "ALL", "AND", "OR", "NOT", "NULL","INTO" ,"TRUE", "FALSE",
            "BETWEEN", "LIKE", "AS", "ON", "IS", "IN", "EXISTS", "CASE", "WHEN",
            "THEN", "ELSE", "END", "DISTINCT", "TOP", "LIMIT", "AUTO_INCREMENT", "SERIAL", "ROWNUM", "SYSDATE", "CURRENT_TIMESTAMP",
            "IDENTITY", "NOCHECK", "CASCADE", "FOR"]
            if word.upper() in keywords:
                return LexicalKind.KEYWORD.name
            else:
                return LexicalKind.IDENTIFIER.name
            
        elif word == "==":
            return LexicalKind.EQUAL_OPERATION.name
        elif word == "=":
            return LexicalKind.ASSIGNMENT_OPERATION.name
        elif word == "!=":
            return LexicalKind.UNEQUAL_OPERATION.name
        elif word == "<":
            return LexicalKind.LESS_OPERATION.name
        elif word == ">":
            return LexicalKind.MORE_OPERATION.name
        elif word == ">=":
            return LexicalKind.MORE_EQUAL_OPERATION.name
        elif word == "<=":
            return LexicalKind.LESS_EQUAL_OPERATION.name    
        elif word == ".":
            return LexicalKind.DOT.name
        else:
            return LexicalKind.UNDEFINED.name

    def analyze_line(self):
        print("text is: " , self.text)
        tokens_tuples = re.findall(r'(\d+(\.\d+)?)|([a-zA-Z_]\w*(\d*|[a-zA-Z_]*)?)|([\+\-\*/:]=?|==|=|!=|<=|>=|<|>)|\s|(\()|(\))|(,)|(;)|(.)', self.text)

        tokens = []
        for token_tuples in tokens_tuples:
            for token in token_tuples:
                if token:
                    tokens.append(token)
                   
        return tokens
    

class LexicalAnalyzerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lexical Analyzer")
        self.create_widgets()

    def create_widgets(self):
        self.text_label = tk.Label(self.master, text="Enter Text:")
        self.text_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.text_entry = tk.Entry(self.master, width=50)
        self.text_entry.grid(row=1, column=0, padx=5, pady=5)

        self.analyze_button = tk.Button(self.master, text="Analyze", command=self.analyze_text)
        self.analyze_button.grid(row=2, column=0, pady=5)

        # Create the Treeview widget with the yscroll option
        self.result_tree = ttk.Treeview(self.master, columns=("Token", "Type"), show="headings", yscrollcommand=self.treeview_yscroll)
        self.result_tree.heading("Token", text="Token")
        self.result_tree.heading("Type", text="Type")
        self.result_tree.grid(row=0, column=1, rowspan=3, padx=5, pady=5, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self.master, orient="vertical", command=self.result_tree.yview)
        self.result_tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=2, rowspan=3, sticky="ns")

    def treeview_yscroll(self, *args):
        self.result_tree.yview(*args)

    def analyze_text(self):
        text_to_analyze = self.text_entry.get()
        lexical_analyzer = LexicalAnalyzer(text_to_analyze)
        tokens = lexical_analyzer.analyze_line()

        for item in self.result_tree.get_children():
            self.result_tree.delete(item)

        for token in tokens:
            token_type = LexicalAnalyzer.get_type(token)
            self.result_tree.insert("", "end", values=(token, token_type))


    def analyze_text(self):
        text_to_analyze = self.text_entry.get()
        lexical_analyzer = LexicalAnalyzer(text_to_analyze)
        tokens = lexical_analyzer.analyze_line()

        for item in self.result_tree.get_children():
            self.result_tree.delete(item)

        for token in tokens:
            token_type = LexicalAnalyzer.get_type(token)
            self.result_tree.insert("", "end", values=(token, token_type))

def main():
    root = tk.Tk()
    app = LexicalAnalyzerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()





