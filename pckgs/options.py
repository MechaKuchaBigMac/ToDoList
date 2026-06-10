import json
from datetime import datetime

def AddTask(filePath: str,title: str):
    with open(filePath, "r", encoding="utf-8") as f:
        db = json.load(f)

        status = 'X'

        task = {
            "id":         db["next_id"],
            "status":     status,
            "title":      title,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        db["tasks"].append(task)
        db["next_id"] += 1

        with open(filePath, "w", encoding="utf-8") as f:
            json.dump(db,f, indent=4, ensure_ascii=False)

            print(f"Task \"{title}\" successfuly added to ({filePath})")

            return task
    
    return

def ShowTasks(filePath:str):
    with open(filePath, 'r', encoding="utf-8") as fl:
        db = json.load(fl)

        tasks = db.get("tasks",[])
        
        if not tasks:
            print("\n [WARNING] There's no single task left")
            return

        print("\n" + "~"*55)
        print(f"{"St":<2} | {"ID":<5} | {"Task Name":<20} | {"Created at"}")
        print("="*55)
        for ts in tasks:
            print(f"{ts["status"]:<2} | {ts["id"]:<5} | {ts["title"]:<20} | {ts["created_at"]}")
        print("~"*55 + "\n")

        
    
    return

def Compleate(filePath:str, taskID:int):
    with open(filePath, 'r', encoding="utf-8") as ffff:
        db = json.load(ffff)

        taskFound = False

        for task in db['tasks']:
            if task["id"] == taskID:
                task["status"] = "O"
                taskFound      = True
                break
        
        if not taskFound:
            print(f"\nThere's no task with ID:{taskID}")
    
    with open(filePath, 'w', encoding="utf-8") as f:
        json.dump(db, f, indent=4, ensure_ascii=False)
    
    print(f"\nTask with ID {taskID} successfuly updated!")
        
    return

def DeleteTask(filePath:str,taskID:int):
    with open(filePath, 'r', encoding="utf-8") as f:
        db = json.load(f)
    
    initial_count = len(db["tasks"])

    db["tasks"] = [task for task in db["tasks"] if task["id"] != taskID]

    if len(db["tasks"]) == initial_count:
        print(f"\nThe task with ID: {taskID} is not Found")
        return False
    
    with open(filePath,'w', encoding="utf-8") as f:
        json.dump(db, f, indent=4,ensure_ascii=False)
    print(f"The task with ID: {taskID} successfuly deleted")
    return True