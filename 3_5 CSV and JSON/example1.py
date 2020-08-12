import json

student1 = {
    "first_name": "Oleg",
    "last_name": "Dean",
    "certificate": True,
    "scores": [
        70,
        80,
        90
    ],
    "description": "Good job, Greg"
}
student2 = {
    "first_name": "Wirl",
    "last_name": "Wood",
    "certificate": True,
    "scores": [
        70,
        80,
        90
    ],
    "description": "Nicely Done"
}

data = [student1, student2]
print(json.dumps(data, indent=4, sort_keys=True))
