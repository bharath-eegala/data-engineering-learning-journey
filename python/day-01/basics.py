# Day 1 - Python Fundamentals

ctc = 5.75
company = "Carelon Global Solutions"
salary = 42900

annual_salary = salary * 12

print(ctc)
print(company)
print(annual_salary)

if salary >= 50000:
    print("HIGH")
elif salary >= 40000:
    print("MED")
else:
    print("LOW")

numbers = [10, 20, 30, 40, 50]

filtered_num = []

for num in numbers:
    if num > 25:
        filtered_num.append(num)

print(filtered_num)
