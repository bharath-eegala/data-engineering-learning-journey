# Day 2 - Python Functions

# Basic function
def greet():
    print("Hello")

greet()


# Function with a parameter
def greet(name):
    print("Hello", name)

greet("Bharath")


# Function with return
def calculate_double(number):
    double_val = number * 2
    return double_val

result = calculate_double(10)
print(result)


# Calculate total sales
sales = [100, 200, 300]

def calculate_total(sales):
    total = 0
    for sale in sales:
        total = sale + total
    return total

result = calculate_total(sales)
print(result)


# Calculate total of high-value sales
sales = [100, 500, 200, 800, 300]

def calculate_high_sales(sales):
    h_sale = 0
    for sale in sales:
        if sale > 300:
            h_sale = sale + h_sale
    return h_sale

print(calculate_high_sales(sales))
