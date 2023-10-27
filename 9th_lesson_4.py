data = [
    {"name": "Alisa", "country": "UA", "item": "socks", "price": 15},
    {"name": "Alisa", "country": "UA", "item": "socks", "price": 25},
    {"name": "Ben", "country": "US", "item": "pencil", "price": 95},
    {"name": "Alisa", "country": "UA", "item": "pencil", "price": 45},
    {"name": "Oleg", "country": "GB", "item": "socks", "price": 100},
    {"name": "Ben", "country": "US", "item": "pencil", "price": 10}
]

# Створюємо множину працівників
workers_set = set(sale["name"] for sale in data)
print("Список працівників:", workers_set)

# Створюємо словник зі сумами виторгу за тиждень для кожного працівника
sales_by_worker = {}
for sale in data:
    name = sale["name"]
    price = sale["price"]
    if name in sales_by_worker:
        sales_by_worker[name] += price
    else:
        sales_by_worker[name] = price

print("Сума виторгу за тиждень для кожного працівника:")
for name, total_sales in sales_by_worker.items():
    print(f"{name}: {total_sales}")
