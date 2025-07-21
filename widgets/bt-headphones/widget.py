# Уровень 1 — Введение в функции

# Простая функция для расчета общей стоимости партии товара
def calculate_total_price(unit_price, quantity):
    return unit_price * quantity

# Входные данные (переменные)
product_name = "Наушники Bluetooth"
unit_price = 1790
quantity = 8

# Вызов функции
total = calculate_total_price(unit_price, quantity)

RESULT = {
    "title": f"Товар: {product_name}",
    "value": quantity,
    "status": "IN_STOCK" if quantity > 5 else "LOW_STOCK",
    "chart_type": "bar",
    "chart_data": [quantity - 2, quantity - 1, quantity],
    "category": "Аудио",
    "price": unit_price,
    "price_total": total,
    "alerts": ["Низкий остаток"] if quantity <= 5 else [],
    "meta": {
        "unit": "шт.",
        "last_update": "now"
    }
}