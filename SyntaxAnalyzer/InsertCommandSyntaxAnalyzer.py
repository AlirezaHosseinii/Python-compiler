class InsertCommandSyntaxAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = ""
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
        self.current_token = str(self.tokens[self.index]).upper()
        print("Current token:", self.current_token, "Index:", self.index)
        self.index += 1

    def previous(self):
        return self.tokens[self.index - 2]

    def match(self, expected_token):
        if self.current_token.upper() == str(expected_token).upper():
            self.consume()
        else:
            self.error_messages.append(f"After {self.previous()} Expected {expected_token} but found {self.current_token}")

    def match_identifier(self):
        if self.current_token.isidentifier():
            if self.current_token not in self.reserved_keywords:
                self.consume()
            else:
                self.error_messages.append(f"After {self.previous()} {self.current_token} is a reserved keyword")
        else:
            self.error_messages.append(f"After {self.previous()} Expected identifier but found {self.current_token}")

    def values_list(self):
        if self.current_token == "(":
            self.consume()
            while self.current_token != ")":
                self.match_identifier()  # Assuming that values will be identifiers
                if self.current_token == ",":
                    self.consume()
            self.match(")")
        else:
            self.error_messages.append(f"After {self.previous()} Expected ( but found {self.current_token}")

    def insert_statement(self):
        self.match("INSERT")
        self.match("INTO")
        self.match_identifier()
        self.match("(")
        self.match_identifier()  # Assuming the first identifier corresponds to a column name
        while self.current_token == ",":
            self.consume()
            self.match_identifier()
        self.match(")")
        self.match("VALUES")
        self.values_list()
        if self.current_token == ";":
            return "Accepted."
        else:
            self.error_messages.append(f"After {self.previous()} Not finishing with ; and finished with {self.current_token}")

    def parse(self):
        self.consume()
        if self.insert_statement() == "Accepted.":
            return "Accepted."
        else:
            return self.error_messages[0]
