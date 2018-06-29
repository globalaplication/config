from config import load
data = load("./data")
print (data.get("version"))
data.set("textcolor", "None")
