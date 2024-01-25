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
        tokens_tuples = re.findall(r'(\b\d+\.\d+|\b\d+\b)|([a-zA-Z_]\w*(\d*|[a-zA-Z_]*)?)|([\+\-\*/:]=?|==|=|!=|<=|>=|<|>)|\s|(\()|(\))|(,)|(;)|(.)', self.text)

        tokens = []
        for token_tuples in tokens_tuples:
            for token in token_tuples:
                if token:
                    tokens.append(token)                  
        return tokens
    





