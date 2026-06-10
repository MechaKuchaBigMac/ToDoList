import pckgs.options as opt

filePath = "D:\INQUISITOR\ToDoList\db.json"

def main():
    isAlive = True

    while isAlive:
        command = input("(a)[add] (s)[show] (c)[compleate] (d)[delete] (e)[exit]\nChoose the option: ")

        if command == "add" or command == "a":
            taskName = str(input("The task: "))
            opt.AddTask(filePath, taskName)
            continue

        if command == "show" or command == "s":
            opt.ShowTasks(filePath)
            continue

        if command == "compleate" or command == "c":
            taskID = int(input("(COMPLEATE)Task ID: "))
            opt.Compleate(filePath,taskID)
            continue

        if command == "delete" or command == "d":
            taskID = int(input("(DELETE)Task ID: "))
            opt.DeleteTask(filePath,taskID)
            continue

        if command == "exit" or command == "e":
            print("You're pressed 'exit' bye bye..(^ w ^)")
            isAlive = False
    
    return 0;

main()