# ============================================================
# Data Engineering Learning Journey
# Python Practice - Day 4 & Day 5
# ============================================================



# ============================================================
# DAY 4 - DICTIONARIES
# ============================================================

# 1. Dictionary
employee = {
    "name": "Bharath",
    "role": "Data Engineer",
    "exp": 3
}

print(employee["role"])


# 2. Loop through dictionary keys
for key in employee:
    print(key)


# 3. Get dictionary values
for key in employee:
    print(employee[key])


# 4. Modify an existing dictionary value
employee["exp"] = 4

# 5. Add a new key-value pair
employee["loc"] = "Hyd"

print(employee)


# 6. List of dictionaries
employees = [
    {
        "name": "Bharath",
        "role": "Data Engineer",
        "exp": 3
    },
    {
        "name": "Rahul",
        "role": "Data Analyst",
        "exp": 2
    },
    {
        "name": "Priya",
        "role": "Data Engineer",
        "exp": 5
    }
]


# 7. Filter employees based on role
for employee in employees:
    if employee["role"] == "Data Engineer":
        print(employee["name"], employee["exp"])


# ============================================================
# DAY 5 - FUNCTIONS, LISTS & DATA PROCESSING
# ============================================================

sales = [100, 250, 400, 150, 500]


# 1. Calculate total of low sales
def calculate_low_sales(sales):
    total_low = 0

    for sale in sales:
        if sale < 300:
            total_low = sale + total_low

    return total_low


result = calculate_low_sales(sales)
print(result)


# 2. Count sales below 300
def count_low_sales(sales):
    count = 0

    for sale in sales:
        if sale < 300:
            count += 1

    return count


result = count_low_sales(sales)
print(result)


# 3. Collect all sales below 300
def get_low_sales(sales):
    low_sales = []

    for sale in sales:
        if sale < 300:
            low_sales.append(sale)

    return low_sales


result = get_low_sales(sales)
print(result)


# 4. Nested list inside a dictionary
employee = {
    "id": 101,
    "name": "Bharath",
    "role": "Data Engineer",
    "skills": ["Python", "SQL", "Snowflake"]
}

print(employee["skills"])
print(employee["skills"][0])


# 5. List of dictionaries with nested lists
employees = [
    {
        "name": "Bharath",
        "role": "Data Engineer",
        "skills": ["Python", "SQL"]
    },
    {
        "name": "Rahul",
        "role": "Data Analyst",
        "skills": ["SQL", "Power BI"]
    }
]


# 6. Get skills of a Data Engineer
def get_engineer_skills(employees):
    for employee in employees:
        if employee["role"] == "Data Engineer":
            return employee["skills"]


result = get_engineer_skills(employees)
print(result)


# ============================================================
# KEY CONCEPTS LEARNED
# ============================================================
#
# Day 4:
# - Dictionaries
# - Dictionary keys and values
# - Modifying dictionaries
# - Adding key-value pairs
# - Lists of dictionaries
# - Filtering records
#
# Day 5:
# - Functions with lists
# - Accumulator pattern
# - Counting matching records
# - Collecting matching values using append()
# - return inside vs outside a loop
# - Nested dictionaries and lists
# - Processing one result vs all results
#
# ============================================================
