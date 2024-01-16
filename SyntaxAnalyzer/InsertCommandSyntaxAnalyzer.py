class InsertCommandSyntaxAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token : str = ""
        self.index = 0
        self.error_messages = []
        self.reserved_keywords = [
            "INSERT", "INTO", "VALUES", "SELECT", "FROM", "WHERE", "GROUP BY",
            "ORDER BY", "HAVING", "UNION", "ALL", "AND", "OR", "NOT", "NULL",
            "TRUE", "FALSE", "BETWEEN", "LIKE", "AS", "ON", "IS", "IN", "EXISTS",
            "CASE", "WHEN", "THEN", "ELSE", "END", "DISTINCT", "TOP", "LIMIT",
            "AUTO_INCREMENT", "SERIAL", "ROWNUM", "SYSDATE", "CURRENT_TIMESTAMP",
            "IDENTITY", "NOCHECK", "CASCADE", "FOR"
        ]

    def consume(self):
        try:
            self.current_token = str(self.tokens[self.index]).upper()
            print("current token: ", self.current_token , "index: ", self.index)
            self.index += 1
        except IndexError:
            raise SyntaxError(f"Unexpected end of input")

    def previous(self):
        try :
            return f'After  "{self.tokens[self.index - 2]}" '   
        except IndexError:
            return None

    def match(self, expected_token):    
        if self.current_token.upper() == str(expected_token).upper():
            self.consume()
        else:
               raise SyntaxError(f'{self.previous()} Expected  "{expected_token}"  but found  "{self.current_token}" ')    

    def match_identifier(self):
        if self.current_token.isidentifier():
            if self.current_token not in self.reserved_keywords:
                self.consume()
            else:
                raise SyntaxError(f'{self.previous()} given  "{self.current_token}"  is a keyword')
        else:
                raise SyntaxError(f'{self.previous()} Expected identifier but found  "{self.current_token}" ')

    def column_list(self):
        column_count = 0
        if self.current_token == "(":
            self.consume()
            self.match_identifier()
            column_count += 1
            while self.current_token == ",":
                self.consume()
                self.match_identifier()
                column_count += 1
            self.match(")")
        return column_count

    def values_list(self,column_count):
        counter = 0
        while self.current_token == "(":
            self.consume()
            self.match_identifier()
            counter +=1
            while self.current_token != ")":
                self.match(",")
                self.match_identifier()
                counter +=1
            if counter != column_count:
                raise SyntaxError(f"Expected {column_count} values but found {counter} .LOC : {self.previous()} ")
            self.match(")")
            if self.current_token == ",":
                self.consume()
                counter = 0
            elif self.current_token == ";":
                return 
        else:
            raise SyntaxError(f"{self.previous()} Expected ( but found {self.current_token}")

    def insert_statement(self):
        self.match("INSERT")
        self.match("INTO")
        self.match_identifier()
        column_count = self.column_list()
        self.match("VALUES")
        self.values_list(column_count)
        if self.current_token == ";":
            return "Accepted."
        else:
            raise SyntaxError(f"{self.previous()} Not finishing with ; and finished with {self.current_token}")

    def parse(self):
        self.consume()
        if self.insert_statement() == "Accepted.":
            return "Accepted."
        else:
            raise SyntaxError(f"Error : Not accepted , Why ? ")
