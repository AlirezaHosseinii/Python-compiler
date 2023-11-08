from enum import Enum
import re


class LexicalKind(Enum):
    NUMBER = "Number"
    WHITESPACE = "WhiteSpace"
    STRING = "String"
    PLUS_OPERATION = "PlusOperation"
    MINUS_OPERATION = "MinusOperation" 
    DIVIDE_OPERATION = "DivideOperation"
    MULTIPLE_OPERATION = "MultipleOperation" 
    COLON = "Colon"
    UNDEFINED = "Undefined"
    SPACE = "Space"

class LexicalAnalyzer:
    def __init__(self, text):
        self.text = text

    def getType(word):
        if re.match(r'\d+(\.\d+)?$' ,word):
            return LexicalKind.NUMBER
        elif re.match(r'\s+$' ,word):
            return LexicalKind.WHITESPACE
        elif word == "+":
            return LexicalKind.PLUS_OPERATION
        elif word == "-":
            return LexicalKind.MINUS_OPERATION
        elif word == "/":
            return LexicalKind.DIVIDE_OPERATION
        elif word == "*":
            return LexicalKind.MULTIPLE_OPERATION
        elif word == ":":
            return LexicalKind.COLON
        elif re.match(r'^[a-zA-Z_]\w+(\d* | [a-zA-Z_]*)?$', word): 
            return LexicalKind.STRING
        else:
            return LexicalKind.UNDEFINED

    def analyzeLine(self):
        words = self.text.split(" ")
        tokens = {}

        for word in words:
            typeOfWord = LexicalAnalyzer.getType(word)
            tokens[word] = typeOfWord
        
        return tokens    