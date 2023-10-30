from enum import Enum


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
        if word.isdigit():
            return SyntaxKind.NUMBER
        elif word.isspace():
            return SyntaxKind.WHITESPACE
        elif word == "+":
            return SyntaxKind.PLUS_OPERATION
        elif word == "-":
            return SyntaxKind.MINUS_OPERATION
        elif word == "/":
            return SyntaxKind.DIVIDE_OPERATION
        elif word == "*":
            return SyntaxKind.MULTIPLE_OPERATION
        elif word.isalpha(): 
            return SyntaxKind.STRING

    def syntaxToken(self):
        words = self.text.split(" ")

        for word in words:
            token_type = SyntaxToken.getType(word)
            print(word, ":", token_type)