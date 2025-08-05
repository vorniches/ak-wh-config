# Уровень 3 — Циклы

# Список поступлений товаров
shipments = [
    {"item": "Клавиатура", "qty": 4},
    {"item": "Мышь", "qty": 6},
    {"item": "Кабель HDMI", "qty": 2},
]

# Суммарное количество и данные для графика
total_items = 0

for shipment in shipments:
    total_items += shipment["qty"]

print(total_items)