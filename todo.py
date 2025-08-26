tasks = [] #seznam  úkolů
while True:
    command = input("Zadej prikaz (add/list/quit): ")
                
    if command == "add":
        task = input ("zadej ukol: ")
        tasks.append(task)
        print("Úkol přidán!")

    elif command == "list":
        print("Seznam úkolů:")
        for t in tasks:
                print("-", t)

    elif command =="quit":
        print("Konec programu.")
        break
    
else:
    print ("Neznámý příkaz")