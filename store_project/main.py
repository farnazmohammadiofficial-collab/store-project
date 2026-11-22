sales = [
    {"product": "Laptop", "price": 30000000, "quantity": 2},
    {"product": "Mouse", "price": 500000, "quantity": 5},
    {"product": "Phone", "price": 20000000, "quantity": 3},
    {"product": "Keyboard", "price": 1200000, "quantity": 2},
    {"product": "Monitor", "price": 10000000, "quantity": 1}
]
from calculations import report

revenue, count, average_price = report(sales)

print("Total revenue:", revenue)
print("Products count:", count)
print("Average price:", average_price)
