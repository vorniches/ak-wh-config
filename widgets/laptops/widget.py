# Данные о ноутбуках
stock = 8
price = 120000
category = "Электроника"

def process_laptops():
    global stock
    # Более сложная логика
    weekend_sales = 2
    stock -= weekend_sales
    
    # Если мало товара, "заказываем" новую партию
    if stock < 5:
        stock += 15
        
    return stock

# Обработка
final_stock = process_laptops()

RESULT = {
    'title': 'Ноутбуки MacBook',
    'value': final_stock,
    'status': 'IN_STOCK' if final_stock > 10 else 'LOW_STOCK',
    'chart_type': 'bar',
    'chart_data': [5, 8, 12, final_stock],
    'category': category,
    'price_total': final_stock * price
}
