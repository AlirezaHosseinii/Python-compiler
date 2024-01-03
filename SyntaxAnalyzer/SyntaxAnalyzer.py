class SyntaxAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = 0
        self.reserved_keywords = ["CREATE", "TABLE", "INT", "VARCHAR", 
                                  "DATE", "FLOAT", "PRIMARY", "KEY", "FOREIGN",
                                    "REFERENCES", "NOT", "UNIQUE"]

    def consume(self):
        self.current_token = self.tokens[self.index]   
        self.index += 1

    def match(self, expected_token):    
        if self.current_token == expected_token:
            self.consume()
        else:
               raise SyntaxError(f"Expected {expected_token} but found {self.current_token}")    

    def match_identifier(self):
        if self.current_token.isidentifier():
            if self.current_token not in self.reserved_keywords:
                self.consume()
            else:
                raise SyntaxError(f"{self.current_token} is a keyword")
        else:
                raise SyntaxError(f"Expected identifier but found {self.current_token}")

    def constraint(self):
        print("here checking constraint: " + self.current_token)
        if self.current_token == "PRIMARY":
            self.match("PRIMARY")
            self.match("KEY")
            self.match("(")
            self.match_identifier()
            self.match(")")
            if self.current_token == ",":
                self.consume()
                if not self.current_token.upper() in ["PRIMARY", "FOREIGN", "NOT", "UNIQUE"]:
                    print("here1")
                    self.column_list()
                else:
                    print("here2")
                    self.constraint_list()  

        elif self.current_token == "FOREIGN":
            self.match("FOREIGN")
            self.match("KEY")
            self.match("(")
            self.match_identifier()
            self.match(")")
            self.match("REFERENCES")
            self.match_identifier()
            self.match("(")
            self.match_identifier()
            self.match(")")
            if self.current_token == ",":
                self.consume()
                if not self.current_token.upper() in ["PRIMARY", "FOREIGN", "NOT", "UNIQUE"]:
                    print("here1")
                    self.column_list()
                else:
                    print("here2")
                    self.constraint_list()  

        elif self.current_token in ["NOT", "UNIQUE"]:
            self.consume()
            if self.current_token == ",":
                self.consume()
                if not self.current_token.upper() in ["PRIMARY", "FOREIGN", "NOT", "UNIQUE"]:
                    print("here1")
                    self.column_list()
                else:
                    print("here2")
                    self.constraint_list()   

        else:
            raise SyntaxError(f"Unexpected token: {self.current_token}")


    def constraint_list(self):
        if self.current_token.upper() in ["PRIMARY", "FOREIGN", "NOT", "UNIQUE"]: # more constraints? 
            self.constraint()
            while self.current_token == ",":
                self.constraint()
                self.consume() 

    def check_numeric(self):
        try:
            float_token = float(self.current_token)
        except ValueError:
            raise SyntaxError(f"{self.current_token} is not numeric")
        self.consume()


    def data_type(self):
        if self.current_token.upper() in ["INT", "VARCHAR", "DATE", "FLOAT"]:  # more data types? #test of date and float
            self.consume()
            if self.current_token == "(":
                self.match("(")
                self.check_numeric()
                self.match(")")
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token}")


    def column_def(self):
        self.match_identifier()
        self.data_type()
        self.constraint_list()

    def column_list(self):
        self.column_def()
        while self.current_token == ",":
            self.consume()
            if not self.current_token.upper() in ["PRIMARY", "FOREIGN", "NOT", "UNIQUE"]:
                self.column_def()
            else:
                self.constraint_list()    

    def statement(self):
        self.match("CREATE")
        self.match("TABLE")
        self.match_identifier()
        self.match("(")
        self.column_list()
        self.match(")")
        if self.current_token == ";":
            print("Accepted.")
        else:
            raise SyntaxError(f"Not finishing with ; and finished with {self.current_token}" )    

    def parse(self):
        self.consume() 
        self.statement()
    