import sys
sys.path.insert(1, 'LexicalAnalyzer')
from LexicalAnalyzer import LexicalAnalyzer

class AlterTableSyntaxAnalyzerClass:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = ""
        self.index = 0
        self.error_messages = []
        self.reserved_keywords = [
            "ALTER", "TABLE", "ADD", "DROP", "MODIFY", "RENAME", "CONSTRAINT", "FOREIGN", "PRIMARY", "KEY", 
            "UNIQUE", "INDEX", "COLUMN", "REFERENCES", "CHECK","VARCHAR"
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
            if self.index < 2:
                return "" 
            else:    
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
                raise SyntaxError(f'{self.previous()} expected a name but got a keyword {self.current_token}!')
        else:
                raise SyntaxError(f'{self.previous()} Expected identifier but found  "{self.current_token}" ')

    def add_column(self):
        self.match("ADD")
        self.match_identifier()
        self.data_type()
        self.constraint_list()

    def modify_column(self):
        self.match("MODIFY")
        self.match("COLUMN")
        self.match_identifier()
        self.data_type()
        self.constraint_list()

    def drop_column(self):
        self.match("DROP")
        self.match("COLUMN")
        self.match_identifier()

    def rename_table(self):
        self.match("RENAME")
        self.match("COLUMN")
        self.match_identifier()
        self.match("TO")
        self.match_identifier()    

    def constraint(self):
        if self.current_token == "PRIMARY":
            self.match("PRIMARY")
            self.match("KEY")
            if self.current_token == "(":
                self.match("(")
                self.match_identifier()
                while self.current_token == ",":
                    self.consume()
                    self.match_identifier()
                self.match(")")
            if self.current_token == ",":
                self.consume()
                if not self.current_token.upper() in ["PRIMARY", "FOREIGN", "NOT", "UNIQUE"]:
                    self.column_list()
                else:
                    self.constraint_list()

        elif self.current_token == "FOREIGN":
            self.match("FOREIGN")
            self.match("KEY")
            if self.current_token == "(":
                self.match("(")
                self.match_identifier()
                while self.current_token == ",":
                    self.consume()
                    self.match_identifier()
                self.match(")")
            self.match("REFERENCES")
            self.match_identifier()
            if self.current_token == "(":
                self.match("(")
                self.match_identifier()
                while self.current_token == ",":
                    self.consume()
                    self.match_identifier()
                self.match(")")
            if self.current_token == ",":
                self.consume()
                if not self.current_token.upper() in ["PRIMARY", "FOREIGN", "NOT", "UNIQUE"]:
                    self.column_list()
                else:
                    self.constraint_list()

        elif self.current_token in ["NOT", "UNIQUE"]:
            self.consume()
            if self.current_token == ",":
                self.consume()
                if not self.current_token.upper() in ["PRIMARY", "FOREIGN", "NOT", "UNIQUE"]:
                    self.column_list()
                else:
                    self.constraint_list()

        else:
            raise SyntaxError(f'{self.previous()} Unexpected token:  "{self.current_token}" ')

    def constraint_list(self):
        if self.current_token.upper() in ["PRIMARY", "FOREIGN", "NOT", "UNIQUE"]: 
            self.constraint()
            while self.current_token == ",":
                self.constraint()
                self.consume() 

    def check_numeric(self):
        try:
            float_token = float(self.current_token)
        except ValueError:
            raise SyntaxError(f'{self.previous()} should be numeric but found "{self.current_token}" ')
        self.consume()

    def data_type(self):
        if self.current_token.upper() in ["INT", "VARCHAR", "DATE", "FLOAT", "DECIMAL"]:
            self.consume()
            if self.current_token == "(":
                self.match("(")
                self.check_numeric()
                self.match(")")
        else:
             raise SyntaxError(f"{self.previous()} Unexpected token: {self.current_token}")


    def statement(self):
        self.match("ALTER")
        self.match("TABLE")
        self.match_identifier()
        if self.current_token == "ADD":
            self.add_column()
        elif self.current_token == "MODIFY":
            self.modify_column()
        elif self.current_token == "DROP":
            self.drop_column()
        elif self.current_token == "RENAME":
            self.rename_table()
        elif self.current_token == ";":
            raise SyntaxError("Expected a command after alter table!")
        else:
            raise SyntaxError(f"{self.current_token} is not recognized!")

        while(self.current_token == ","):
            self.consume()
            if self.current_token == "ADD":
                self.add_column()
            elif self.current_token == "MODIFY":
                self.modify_column()
            elif self.current_token == "DROP":
                self.drop_column()
            elif self.current_token == "RENAME":
                self.rename_table()
            else:
                raise SyntaxError(f"{self.current_token} is not recognized!")

                    
        print("is:" , self.current_token)
        if self.current_token == ";":
            return "Accepted."
        else:
            raise SyntaxError(f'{self.previous()} Not finishing with ; and finished with  "{self.current_token}" ')

    def parse(self):
        self.consume()
        if self.statement() == "Accepted.":
            return "Accepted."
        else:
            raise SyntaxError(f"Error: Not accepted, Why? ")
        
Command  = "ALTER TABLE my_table ADD new_column INT;"
Command  = "ALTER TABLE my_table;"
Command = "ALTER TABLE my_table MODIFY existing_column VARCHAR(50);"
Command = "ALTER TABLE my_table INVALID_OPERATION;"
Command = "ALTER TABLE my_table ADD new_column INT"

Command = '''
ALTER TABLE table_name
DROP Column column_name;
'''

Command = '''
ALTER TABLE table_name
RENAME COLUMN old_name to new_name;
'''

Command = "ALTER TABLE my_table ADD new_column INT PRIMARY KEY;"
Command = "ALTER TABLE my_table ADD col1 INT, ADD col2 VARCHAR(50);"
Command = "ALTER TABLE my_table MODIFY column existing_column VARCHAR(50) UNIQUE;"
Command = "ALTER TABLE my_table DROP Column column1, DROP column column2;"

Command = "ALTER TABLE my_table MODIFY Column existing_column VARCHAR(50), ADD new_column INT;"

Command = "ALTER TABLE my_table add new int; existing_column VARCHAR(50);"

Command = "ALTER TABLE my_table ADD VARCHAR(50);"

Command = "ALTER TABLE my_table ADD new_column;"


Command = '''
ALTER TABLE table_name
ALTER COLUMN column_name INT;
'''

Command  ='''
ALTER TABLE table_name
MODIFY COLUMN column_name int;
'''

Command  ='''ALTER table table_name
MODIFY column_name int;
'''

Command = "ALTER TABLE my_table add existing_column VARCHAR(50) FOREIGN KEY(kk) references mm, ADD new_column INT;"


lexicalAnalyzer = LexicalAnalyzer(Command)
Lexicaltokens = list(lexicalAnalyzer.analyze_line())
print(f"lexical tokens: {Lexicaltokens}")
syntaxAnalyzer = AlterTableSyntaxAnalyzer(Lexicaltokens)
print(syntaxAnalyzer.parse())
