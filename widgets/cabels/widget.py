# Учебный виджет — Переменные на складе

# Простые переменные
item_name = "USB-кабель"
stock_count = 100
unit_price = 500
chart_type = "bar"

unit_price = unit_price - (unit_price * 0.1)

# Результат для отображения
RESULT = {
    "title": f"Товар: {item_name}",
    "value": stock_count,
    "status": "IN_STOCK" if stock_count > 5 else "LOW_STOCK",
    "chart_type": chart_type,
    "chart_data": [stock_count],
    "category": "Кабели и переходники",
    "price": unit_price,
    "price_total": unit_price * stock_count,
    "alerts": ["Осталось мало!"] if stock_count <= 5 else [],
    "meta": {
        "unit": "шт.",
        "last_update": "now"
    }
}
