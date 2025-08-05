# Уровень 3 — Циклы

# Список поступлений товаров
shipments = [
    {"item": "Клавиатура", "qty": 4},
    {"item": "Мышь", "qty": 6},
]

# Суммарное количество и данные для графика

def count_items(shipments):
    total_items = 0
    if len(shipments) >= 3:
        for item in shipments:
            total_items += item["qty"]
    else:
        print("Too few items")
    
    return total_items
    
print(count_items(shipments))
