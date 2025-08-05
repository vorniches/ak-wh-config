# Уровень 3 — Циклы

# Список поступлений товаров
shipments = [
    {"item": "Клавиатура", "qty": 4},
    {"item": "Мышь", "qty": 6},
    {"item": "Кабель HDMI", "qty": 2}
]

# Суммарное количество и данные для графика
total_items = 0
chart_data = []

for shipment in shipments:
    total_items += shipment["qty"]
    chart_data.append(shipment["qty"])

# Результат
RESULT = {
    "title": "Поступления на склад",
    "value": total_items,
    "status": "OK" if total_items >= 10 else "LOW",
    "chart_type": "bar",
    "chart_data": chart_data,
    "category": "Логистика",
    "alerts": [f"{len(shipments)} новых партий на складе"],
    "meta": {
        "unit": "шт.",
        "last_update": "now"
    }
}
