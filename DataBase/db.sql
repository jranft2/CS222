-- Major Table
CREATE TABLE Major (
    Name VARCHAR(255) PRIMARY KEY,
    Type_of_degree VARCHAR(255) NOT NULL
);

-- Student Table
CREATE TABLE Student (
    NetID VARCHAR(255) PRIMARY KEY,
    Major_Name VARCHAR(255),
    Degree_Type VARCHAR(255) NOT NULL,
    Name VARCHAR(255) NOT NULL,
    GitHub VARCHAR(255),
    Leetcode VARCHAR(255),
    Bio TEXT,
    PFP_URL VARCHAR(255),
    FOREIGN KEY (Major_Name) REFERENCES Major(Name)
);

-- Course Table
CREATE TABLE Course (
    Name VARCHAR(255) NOT NULL,
    Subject VARCHAR(255) NOT NULL,
    Number INT NOT NULL,
    PRIMARY KEY (Name, Subject, Number)
);

-- Enroll Table (Relationship Table)
CREATE TABLE Enroll (
    NetID VARCHAR(255),
    Course_Number INT,
    FOREIGN KEY (NetID) REFERENCES Student(NetID),
    FOREIGN KEY (Course_Number) REFERENCES Course(Number)
);


