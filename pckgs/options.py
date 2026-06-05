import json
from datetime import datetime

def AddTask(filePath: str,title: str):
    with open(filePath, "r", encoding="utf-8") as f:
        db = json.load(f)

        task = {
            "id":         db["next_id"],
            "title":      title,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        db["tasks"].append(task)
        db["next_id"] += 1

        with open(filePath, "w", encoding="utf-8") as f:
            json.dump(db,f, indent=4, ensure_ascii=False)
            return task
    