# Hayoung Nam
# Task List
# Create a program that allows user to manage a task list that’s stored in a database.
# 07 23 2020

import sqlite3
from db import*


print("\nCOMMAND MENU\n")
print()
print("view - View pending tasks")
print("history - View complted tasts")
print("add - Add a task")
print("complete - Complete a task")
print("delete - Delete a task")
print("exit - Exit program")
while True:
    print ()
    choice = input("Command: ")                
    choice = choice.lower()
    if choice == "view":
        view_list()
    elif choice == "history":
        history_list()
    elif choice == "add":
        add_list()
    elif choice == "complete":
        complete_list()
    elif choice == "delete":
        delete_list()
    elif choice == "exit":
        print ("Bye!")
        quit()
    else:
        print ("Error! Try again")
        choice = input("Command: ") 
