from enum import Enum
import re


class SyntaxKind(Enum):
    NUMBER = "Number"
    WHITESPACE = "WhiteSpace"
    STRING = "String"
    PLUS_OPERATION = "PlusOperation"
    MINUS_OPERATION = "MinusOperation" 
    DIVIDE_OPERATION = "DivideOperation"
    MULTIPLE_OPERATION = "MultipleOperation" 

class SyntaxToken:
    def __init__(self, type, text):
        self.type = type
        self.text = text

    def getType(word):
        if re.match(r'\d+(\.\d+)?$' ,word):
            return SyntaxKind.NUMBER
        elif re.match(r'\s+$' ,word):
            return SyntaxKind.WHITESPACE
        elif word == "+":
            return SyntaxKind.PLUS_OPERATION
        elif word == "-":
            return SyntaxKind.MINUS_OPERATION
        elif word == "/":
            return SyntaxKind.DIVIDE_OPERATION
        elif word == "*":
            return SyntaxKind.MULTIPLE_OPERATION
        elif re.match(r'^[a-zA-Z_]\w+(\d* | [a-zA-Z_]*)?$', word): 
            return SyntaxKind.STRING

    def syntaxToken(self):
        words = self.text.split(" ")

        for word in words:
            token_type = SyntaxToken.getType(word)
            print(word, ":", token_type)