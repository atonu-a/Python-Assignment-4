import json

student = {
    "name" : "Rahim",
    "age" : 20,
    "department" : "CSE"
}

json_str = json.dumps(student)
print(json_str)
