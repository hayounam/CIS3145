import sqlite3
from object import Description
conn = sqlite3.connect("task_list_db.sqlite")
cursor = conn.cursor()


def view_list():
    cursor.execute("select taskID, description from Task where completed = 0")
    lists = cursor.fetchall()
    print()
    for Task in lists:
        print("{}. {}".format(Task[0], Task[1]))
    
def history_list():
    cursor.execute("select description from Task where completed = 1")
    lists = cursor.fetchall()
    print()          
    for Task in lists:
        print("{} (DONE!)".format(Task[0]))
        
def add_list():
    descp = input("description: ")
    conn.execute("insert into Task (description, completed) Values('"+descp+"', 0);")
    conn.commit()

def complete_list():
    num = int(input("Task ID: "))
    query = "update Task set completed = 1 where taskID = ?"
    cursor.execute(query, (num,))
    conn.commit()
    
def delete_list():
    num = int(input("Number: "))
    query = "delete from Task where id = ?"
    cursor.execute(query, (num,))
    conn.commit()

