import json

student = {"name" : "david", "age" : 13, "marks": 87}
print(type(student))
data = json.dumps(student)
print(data)
print(type(data))

data2 = json.loads(data)
print(type(data2))

print(data2["name"])


# data3 = json.dumps(student, indent = 4, seperators = (",","="))
# print(data3)

#write to file sort following json keys
f = open("demo.json", "w")
data4 = json.dumps(student, indent = 4, sort_keys= True)
f.write(data4)