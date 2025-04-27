import time
import json

# clear the file before anything
with open("/app/answers/counter.txt", "w") as f:
    json.dump({"count": 0}, f)

while True:    
    with open("/app/answers/counter.txt", "r+") as f:                
        time.sleep(0.05) # helps with viewing so values dont fly past too fast
        try:
            data = json.load(f)            
        #except json.JSONDecodeError:
        except json.JSONDecodeError as e:
            print("json ERROR, Currently reading empty or corrupted value:")
            print("======================")
            print(e)
            print("======================")
            data = {"count": 0}

        count = data.get("count")
        print(data)

        count += 1
        f.seek(0)
        f.truncate()
        json.dump({"count": count}, f)