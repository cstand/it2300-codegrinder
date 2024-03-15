import csv
import sqlite3
import sys
import os

def addCSVToDB(csv_file,out):
        
    table_name="_".join(csv_file.split(os.sep)[-1].split(".")[:-1])

    # Connect to MySQL database
    conn = sqlite3.connect(out)
    cur = conn.cursor()

    # Read data from CSV and insert into MySQL table
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        header=next(csv_reader)
        first_row=next(csv_reader)
        command="CREATE TABLE IF NOT EXISTS "+table_name+" ("
        insertCommand = "INSERT INTO "+table_name+" ("
        for (name,value) in zip(header,first_row):
            if name[0].isdigit():
                name="N_"+name
            name=name.replace(".","_")
            insertCommand+=name+","
            if name=="id":
                command+=name+" INTEGER PRIMARY KEY"
            else:
                command+=name+" "
                try:
                    int(value)
                    command+="INTEGER"
                except:
                    try:
                        float(value)
                        command+="FLOAT"
                    except:
                        command+="TEXT"
            command+=","
        command=command[:-1]+")"
        insertCommand=insertCommand[:-1]+") VALUES ("+"?, "*(len(header)-1)+"?)"
        # Create table
        cur.execute(command)
        cur.execute(insertCommand, first_row)
        for row in csv_reader:
            cur.execute(insertCommand, row)

    # Commit changes and close connection
    conn.commit()
    conn.close()