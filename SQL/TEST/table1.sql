CREATE -- Create a new table called 'DROP TABLE SchemaName.TableName

GO
-- Create the table in the specified schema
CREATE TABLE SchemaName.TableName

(
    TableName
Id INT NOT NULL PRIMARY KEY, -- primary key column
    Column1 [NVARCHAR](50) NOT NULL,
    Column2 [NVARCHAR](50) NOT NULL
    -- specify more columns here
);
GO