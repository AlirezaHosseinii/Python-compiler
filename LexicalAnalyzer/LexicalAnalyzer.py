from enum import Enum
import re


class LexicalKind(Enum):
    COMMA = ","
    OPEN_PARANTHESIS = "("
    CLOSE_PARANTHESIS = ")"
    NUMBER = "Number"
    WHITESPACE = "WhiteSpace"
    STRING = "String"
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

class LexicalAnalyzer:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def get_type(word):
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
        elif word == ";":
            return LexicalKind.SEMI_COLON
        elif word == ",":
            print("here")
            return LexicalKind.COMMA
        elif word == "(":
            return LexicalKind.OPEN_PARANTHESIS
        elif word == ")":
            return LexicalKind.CLOSE_PARANTHESIS
        elif re.match(r'^[a-zA-Z_]\w*(\d* | [a-zA-Z_]*)?$', word): 
            return LexicalKind.STRING
        elif word == "==":
            return LexicalKind.EQUAL_OPERATION
        elif word == "=":
            return LexicalKind.ASSIGNMENT_OPERATION
        elif word == "!=":
            return LexicalKind.UNEQUAL_OPERATION
        elif word == "<":
            return LexicalKind.LESS_OPERATION
        elif word == ">":
            return LexicalKind.MORE_OPERATION
        elif word == ">=":
            return LexicalKind.MORE_EQUAL_OPERATION
        elif word == "<=":
            return LexicalKind.LESS_EQUAL_OPERATION    
        else:
            return LexicalKind.UNDEFINED

    def analyze_line(self):
        #read, more test and meanwhile go for syntax analayzer
        #tokens_tuples = re.findall(r'(\d+(\.\d+)?)|([a-zA-Z_]\w*(\d*|[a-zA-Z_]*)?)|([\+\-\*/:]=?|==|=|!=|<=|>=|<|>)|\s', self.text)
        #tokens_tuples = re.findall(r'(\d+(\.\d+)?)|([a-zA-Z_]\w*(\d*|[a-zA-Z_]*)?)|([\+\-\*/:]=?|==|=|!=|<=|>=|<|>)|\s|(\()|(\))', self.text)

        print("text is: " , self.text)
        tokens_tuples = re.findall( r'(\d+(\.\d+)?)|([a-zA-Z_]\w*(\d*|[a-zA-Z_]*)?)|([\+\-\*/:]=?|==|=|!=|<=|>=|<|>)|\s|(\()|(\))|(,)|(;)', self.text)

        tokens = []
        
        token_types = {}
        i = 0
        print("token tuples is ", tokens_tuples)
        for token_tuples in tokens_tuples:
            for token in token_tuples:
                if token:
                    type_of_token = LexicalAnalyzer.get_type(token)
                    print(f"token is {token} and type of token is {type_of_token}")
                    tokens.append(token)
                    token_types[token] = type_of_token
                    i += 1


        return tokens