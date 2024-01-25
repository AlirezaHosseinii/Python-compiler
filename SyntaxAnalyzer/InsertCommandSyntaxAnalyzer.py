class InsertCommandSyntaxAnalyzerClass:
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
            "AUTO_INCREMENT", "SERIAL", "ROWNUM", "SYSDATE",
            "IDENTITY", "NOCHECK", "CASCADE", "FOR"
            ]
        self.one_word_keywords = ['DEFAULT','UUID','USER','SYSDATE','RAND','AUTO_INCREMENT','NULL','TRUE','FALSE'
            ]
        self.no_input_keywords = ['NOW','UNIX_TIMESTAMP','CURDATE','CURTIME','UTC_DATE','UTC_TIME','UTC_TIMESTAMP','LAST_INSERT_ID','ROW_COUNT',
            ]
        self.one_input_keywords = ['MD5','SHA1','SHA256','SHA512','AES_ENCRYPT','AES_DECRYPT',
            'PASSWORD','ENCRYPT','DECRYPT','COMPRESS','UNCOMPRESS','GREATEST','LEAST','CONV',
            'COUNT','AVG','SUM','MIN','MAX','STD','STDDEV','STDDEV_POP','STDDEV_SAMP','VAR_POP',     
            ]
        self.two_input_keywords = ['POWER','MOD',
            ]
        self.some_input_keywords_for_value_list = ['CONCAT']
        
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

    def match_keyword_as_column(self):
        if self.current_token.isnumeric():
            self.consume()
        elif self.current_token in self.one_word_keywords:
            self.consume()
        elif self.current_token in self.no_input_keywords:
            self.consume()
            self.match("(")
            self.match(")")
        elif self.current_token in self.one_input_keywords:
            self.consume()
            self.match("(")
            self.match_identifier(can_column=True)
            self.match(")")
        elif self.current_token in self.two_input_keywords:
            self.consume()
            self.match("(")
            self.match_identifier(can_column=True)
            self.match(",")
            self.match_identifier(can_column=True)
            self.match(")")
        elif self.current_token in self.some_input_keywords_for_value_list:
            self.consume()
            self.match("(")
            self.match_identifier(can_column=True)
            while self.current_token == ",":
                self.consume()
                self.match_identifier(can_column=True)
            self.match(")")
        else : 
            self.match_identifier()

    def match_identifier(self,can_column=False):
        if can_column :
            self.match_keyword_as_column()
        elif self.current_token.isidentifier():
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
            self.match_identifier(can_column=True)
            counter +=1
            while self.current_token != ")":
                self.match(",")
                self.match_identifier(can_column=True)
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
            raise SyntaxError(f"In Value Lists : {self.previous()} Expected ( but found {self.current_token}")

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
