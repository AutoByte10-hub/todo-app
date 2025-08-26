tasks = [] #seznam  úkolů
while True:
    command = input("Enter command (add/list/remove/quit): ")
                
    if command == "add":
        task = input ("Enter a Task: ")
        tasks.append(task)
        print("Task added!")

    elif command == "list":
        print("Task list:")
        for t in tasks:
                print("-", t)
    elif command == "remove":
        task = input("Enter task to remove: ")      
        if task in tasks:
             tasks.remove(task)
             print("Task removed!") 
        else:
             print("Task not found!") 
    elif command =="quit":
        print("Exiting program.")
        break    
    else:
     print ("Unknown command")

    
