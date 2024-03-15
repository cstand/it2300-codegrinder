import sqlite3
#from sqlite3 import Error
#import pandas as pd

def create_connection(path):
    return sqlite3.connect(path)
# conn=create_connection("mydata.db")
# Open and read the file as a single buffer


def run_sqlfile(conn,filename):
    mylist = []
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()      
    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')
    #cursor = conn.cursor()
    # Execute every command from the input file
    lastError=None
    lineCounter=1
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        command=command.strip()
        if not command:
            continue
        try:
            cursor =conn.execute(command)
            tmp = cursor.fetchall()
            if tmp:
                mylist.append(tmp)
        except Exception as e:
            lastError=e
        if lastError:
            raise Exception("error on line "+str(lineCounter)+": "+str(lastError))
        lineCounter+=1
    conn.close()
    return mylist