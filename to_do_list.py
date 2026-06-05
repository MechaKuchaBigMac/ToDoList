import pckgs.options as opt

filePath = "README.md"

def main():
    isAlive = True

    while isAlive:
        command = input("(a)[add] (s)[show] (c)[compleate] (d)[delete] (e)[exit]\nChoose the option: ")

        if command == "add" or command == "a":
            taskName = input("The task: ")
            opt.AddTask(filePath, taskName)
            continue

        if command == "show":
            pass

        if command == "compleate":
            pass

        if command == "delete":
            pass

        if command == "exit" or command == "e":
            isAlive = False
    
    
    
    
    
    return

main()