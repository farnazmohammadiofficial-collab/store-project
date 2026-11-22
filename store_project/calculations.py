
def calculate_revenue(sales):
    total = 0
    for item in sales:
        total += item["price"] * item["quantity"]
    return total


def total_products(sales):
    return len(sales)


def calculate_average_price(sales):
    total_price = sum(item["price"] for item in sales)
    return total_price / total_products(sales)


def report(sales):
    revenue = calculate_revenue(sales)
    count_products = total_products(sales)
    average_price = calculate_average_price(sales)

    return revenue, count_products, average_price


    
