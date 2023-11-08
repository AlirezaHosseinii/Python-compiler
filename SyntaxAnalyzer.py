class SyntaxAnalyzer:
    def __init__(self, tokens):
        self.words = list(tokens.keys())
        self.types = list(tokens.values())
        self.currentToken = None
        self.tokenIndex = 0

    def parse(self):    
        if(self.words[self.tokenIndex] == "+"):
            print("Saw a +")    
        else:
            print("not a +")    
