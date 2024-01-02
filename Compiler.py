from LexicalAnalyzer.LexicalAnalyzer import LexicalAnalyzer
from SyntaxAnalyzer.SyntaxAnalyzer import SyntaxAnalyzer

#Line = input("Enter a line: ")
Line = """
CREATE TABLE Employees (
    EmployeeID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    dateColumn DATE,
    Email VARCHAR(100) UNIQUE,
    DepartmentID INT,
    PRIMARY KEY (EmployeeID),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);
"""
lexicalAnalyzer = LexicalAnalyzer(Line)
Lexicaltokens = list(lexicalAnalyzer.analyze_line())
print(f"lexical tokens: {Lexicaltokens}")
syntaxAnalyzer = SyntaxAnalyzer(Lexicaltokens)
syntaxAnalyzer.parse()
