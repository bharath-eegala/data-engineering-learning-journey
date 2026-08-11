# Day 3 - Python Dictionaries

employee = {
    "name": "Bharath",
    "role": "Data Engineer",
    "exp": 3
}

print(employee["role"])


employees = [
    {"name": "Bharath", "role": "Data Engineer", "exp": 3},
    {"name": "John", "role": "Developer", "exp": 2},
    {"name": "Priya", "role": "Data Engineer", "exp": 4}
]

for employee in employees:
    if employee["role"] == "Data Engineer":
        print(employee["name"])
