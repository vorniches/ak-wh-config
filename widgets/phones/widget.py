import random
import sys
import os

# Начальные данные
stock = 25
price = 80000
min_stock_alert = 10

# Простая логика (пока что)
def calculate_current_stock():
    global stock
    # Имитируем продажи (для демо)
    daily_sales = random.randint(0, 5)
    stock = max(0, stock - daily_sales)
    return stock

def get_status():
    if stock == 0:
        return "OUT_OF_STOCK"
    elif stock <= min_stock_alert:
        return "LOW_STOCK"
    else:
        return "IN_STOCK"

# Обработка данных
current_stock = calculate_current_stock()
status = get_status()

# Данные для графика (последние 7 дней)
chart_data = [30, 28, 25, current_stock, current_stock-1, current_stock-2, current_stock]

# Результат для Django
RESULT = {
    'title': 'Телефоны на складе',
    'value': current_stock,
    'status': status,
    'price': price,
    'chart_type': 'line',
    'chart_data': chart_data,
    'alerts': ['Мало товара!'] if status == 'LOW_STOCK' else [],
    'meta': {
        'unit': 'шт.',
        'last_update': 'now'
    }
}
