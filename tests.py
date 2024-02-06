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
    ,{"TEST2" : "CREATE TABLE Users if not exists(ID INT , Name VARCHAR(50));","status" : False}
    ,{"TEST3" : "CREATE TABLE Orders (OrderID INT PRIMARY KEY, ProductName VARCHAR(100), Quantity INT);","status" : False}
    ,{"TEST4" : "CREATE TABLE Products (ProductID INT UNIQUE, ProductName VARCHAR(100));","status" : False}
    ,{"TEST5" : "CREATE TABLE Orders (OrderID INT, CustomerID INT FOREIGN KEY REFERENCES Customers(CustomerID));","status" : False}
    ,{"TEST6" : "CREATE TABLE Employees (EmployeeID INT DEFAULT 1001, Name VARCHAR(50));","status" : False}
,{"TEST7" : """CREATE TABLE Customers (CustomerID INT INDEX, Name VARCHAR(100), Address VARCHAR(200));""","status" : False}
],
"insert" : [
    {"TEST8" : """INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    DEFALUT
    , 1);""","status" : False}
    ,{"TEST9" : """INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    NOW
    , 1);""","status" : False}
    ,{"TEST10" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    LAST_INSERT_ID()
    , 1);""","status" : False}
    ,{"TEST11" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    MD5
    , 1);""","status" : False}
    ,{"TEST12" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    MD5()
    , 1);""","status" : False}
    ,{"TEST13" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    MD5(1)
    , 1);""","status" : False}
    ,{"TEST14" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    MD5(salam)
    , 1);""","status" : False}
    ,{"TEST15" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    MD5(SHA1(salam))
    , 1);""","status" : False}
    ,{"TEST16" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    POWER
    , 1);""","status" : False}
    ,{"TEST17" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    POWER()
    , 1);""","status" : False}
    ,{"TEST18" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    POWER(1)
    , 1);""","status" : False}
    ,{"TEST19" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    POWER(1,2)
    , 1);""","status" : False}
    ,{"TEST20" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    POWER(POWER(1,2),2)
    , 1);""","status" : False}
    ,{"TEST21" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    POWER(POWER(1,2),POWER(2,1))
    , 1);""","status" : False}
    ,{"TEST22" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    POWER(POER(1,2),POWER(2,1),2)
    , 1);""","status" : False}
    ,{"TEST23" : """
    INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DepartmentID) VALUES (2, John, Doe, 
    CONCAT(1,2,3,4,5,6,7,8,9,10)
    , 1);""","status" : False}
    ],
"alter" : [
    {"TEST24" : """ALTER TABLE my_table ADD new_column INT;""","status" : False}
    ,{"TEST25" : """ALTER TABLE my_table;""","status" : False}
    ,{"TEST26" : """ALTER TABLE my_table MODIFY existing_column VARCHAR(50);""","status" : False}
    ,{"TEST27" : """ALTER TABLE my_table ADD new_column INT;""","status" : False}
    ,{"TEST28" : """
    ALTER TABLE table_name
    DROP Column column_name;""","status" : False}
    ,{"TEST29" : """
    ALTER TABLE table_name
    RENAME COLUMN old_name to new_name;""","status" : False}
    ,{"TEST30" : """
    ALTER TABLE my_table ADD new_column INT PRIMARY KEY;""","status" : False}
    ,{"TEST31" : """
    ALTER TABLE my_table ADD col1 INT, ADD col2 VARCHAR(50);""","status" : False}
    ,{"TEST32" : """
    ALTER TABLE my_table MODIFY column existing_column VARCHAR(50) UNIQUE;""","status" : False}
    ,{"TEST33" : """
    ALTER TABLE my_table DROP Column column1, DROP column column2;""","status" : False}
    ,{"TEST34" : """
    ALTER TABLE my_table MODIFY Column existing_column VARCHAR(50), ADD new_column INT;""","status" : False}
    ,{"TEST35" : """
    ALTER TABLE my_table ADD VARCHAR(50);""","status" : False}
    ]
}

def get_tests(type="create"):
    if type == "create":
        return tests["tests"] + tests["insert"] + tests["alter"]
    elif type == "insert":
        return tests["insert"]
    elif type == "alter":
        return tests["alter"]
        
