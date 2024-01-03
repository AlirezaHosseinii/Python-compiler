from LexicalAnalyzer.LexicalAnalyzer import LexicalAnalyzer
from SyntaxAnalyzer.SyntaxAnalyzer import SyntaxAnalyzer

#Line = input("Enter a line: ")
Line1 = """
CREATE TABLE Employees (
    EmployeeID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50) UNIQUE,
    dateColumn DATE,
    Email VARCHAR(100),
    DepartmentID INT,
    PRIMARY KEY (EmployeeID),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);
"""

Line2 = "CREATE TABLE Users (ID INT, Name VARCHAR(50));"
Line3 = "CREATE TABLE Orders (OrderID INT PRIMARY KEY, ProductName VARCHAR(100), Quantity INT);" #failed
Line4 = "CREATE TABLE Products (ProductID INT UNIQUE, ProductName VARCHAR(100));"
Line5 = "CREATE TABLE Orders (OrderID INT, CustomerID INT FOREIGN KEY REFERENCES Customers(CustomerID));" #failed
Line6 = "CREATE TABLE Employees (EmployeeID INT DEFAULT 1001, Name VARCHAR(50));" #failed
Line7 = "CREATE TABLE Students (StudentID INT PRIMARY KEY, Name VARCHAR(50) NOT NULL, Age INT CHECK(Age >= 18), Email VARCHAR(100) UNIQUE);"
#failed
Line8 = """
CREATE TABLE Books (
    BookID INT,
    Title VARCHAR(200),
    Author VARCHAR(100),
    PublishedDate DATE
);
"""
#fails with Price DECIMAL(10, 2)
Line9 = """
CREATE TABLE Employees (
    EmployeeID INT,  -- This is the primary key
    Name VARCHAR(50)  -- Employee Name
);
"""
#fails
Line10 = """
CREATE TABLE Customers (CustomerID INT INDEX, Name VARCHAR(100), Address VARCHAR(200));
"""
#fails
#end of first 10 cases



lexicalAnalyzer = LexicalAnalyzer(Line8)
Lexicaltokens = list(lexicalAnalyzer.analyze_line())
print(f"lexical tokens: {Lexicaltokens}")
syntaxAnalyzer = SyntaxAnalyzer(Lexicaltokens)
syntaxAnalyzer.parse()
