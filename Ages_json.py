import simplejson as json
import os

if os.path.isfile("./ages.json")and os.stat("./ages.json").st_size !=0:
	oldfile = open("./ages.json", "r+")
	data=json.loads(oldfile.read())
	print("current age is",data["age"],"--Adding a year.")
	data["age"]=data["age"]+1
	print("New age is",data["age"])


oldfile=open("./ages.json","w+")
data={"Name":"Jack","age":25}
print("no file found,setting to default age",data["age"])

oldfile.seek(0)
oldfile.write(json.dumps(data))