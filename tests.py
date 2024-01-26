
tests = {"tests" : [
    {"TEST1" : """
    CREATE TABLE Employees (
        EmployeeID INT NOT NULL UNIQUE PRIMARY KEY FOREIGN KEY REFERENCES Departments(DepartmentID),
        FirstName VARCHAR(50),
        LastName VARCHAR(50) UNIQUE,
        dateColumn DATE,
        Email VARCHAR(100),
        DepartmentID INT UNIQUE,
        PRIMARY KEY (EmployeeID),
        FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
    );
    ""","status" : False}
    ,{"TEST2" : "CREATE TABLE Users (ID INT , Name VARCHAR(50));","status" : False}
    ,{"TEST3" : "CREATE TABLE Orders (OrderID INT PRIMARY KEY, ProductName VARCHAR(100), Quantity INT);","status" : False}
    ,{"TEST4" : "CREATE TABLE Products (ProductID INT UNIQUE, ProductName VARCHAR(100));","status" : False}
    ,{"TEST5" : "CREATE TABLE Orders (OrderID INT, CustomerID INT FOREIGN KEY REFERENCES Customers(CustomerID));","status" : False}
    ,{"TEST6" : "CREATE TABLE Employees (EmployeeID INT DEFAULT 1001, Name VARCHAR(50));","status" : False}
    #CREATE TABLE Employees (EmployeeID INT DEFAULT 1001, Name VARCHAR(50);
    ,{"TEST7" : "CREATE TABLE Students (StudentID INT PRIMARY KEY, Name VARCHAR(50) NOT NULL, Age INT CHECK(Age >= 18), Email VARCHAR(100) UNIQUE);","status" : False} #failed
    ,{"TEST8" : """
    CREATE TABLE Books (
        BookID INT,
        Title VARCHAR(200),
        Author VARCHAR(100),
        PublishedDate DATE,
        Price DECIMAL(10, 2)
    );
    ""","status" : False}
    ,{"TEST9" : """
    CREATE TABLE Employees (
        EmployeeID INT,  -- This is the primary key
        Name VARCHAR(50)  -- Employee Name
    );
    ""","status" : False}
,{"TEST10" : """CREATE TABLE Customers (CustomerID INT INDEX, Name VARCHAR(100), Address VARCHAR(200));""","status" : False}
],
"insert" : [
    {"TEST1" : """INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    DEFALUT
    , 1);""","status" : False}
    ,{"TEST2" : """INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    NOW
    , 1);""","status" : False}
    ,{"TEST3" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    LAST_INSERT_ID()
    , 1);""","status" : False}
    ,{"TEST4" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    MD5
    , 1);""","status" : False}
    ,{"TEST5" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    MD5()
    , 1);""","status" : False}
    ,{"TEST6" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    MD5(1)
    , 1);""","status" : False}
    ,{"TEST7" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    MD5(salam)
    , 1);""","status" : False}
    ,{"TEST8" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    MD5(SHA1(salam))
    , 1);""","status" : False}
    ,{"TEST9" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    POWER
    , 1);""","status" : False}
    ,{"TEST10" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    POWER()
    , 1);""","status" : False}
    ,{"TEST11" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    POWER(1)
    , 1);""","status" : False}
    ,{"TEST12" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    POWER(1,2)
    , 1);""","status" : False}
    ,{"TEST13" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    POWER(POWER(1,2),2)
    , 1);""","status" : False}
    ,{"TEST14" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    POWER(POWER(1,2),POWER(2,1))
    , 1);""","status" : False}
    ,{"TEST15" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    POWER(POWER(1,2),POWER(2,1),2)
    , 1);""","status" : False}
    ,{"TEST16" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    CONCAT(1,2,3,4,5,6,7,8,9,10)
    , 1);""","status" : False}
    ]
}

def get_tests(type="create"):
    if type == "create":
        return tests["tests"]
    elif type == "insert":
        return tests["insert"]
        
