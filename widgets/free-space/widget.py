# Уровень 2 — Условия

# Место на складе
current_space = 200     # свободное место в м²
total_space = 200            # общая площадь склада

# Подсказка: здесь пока нет условий — нужно будет написать их самому
# Например: если меньше 20%, то "Мало места", иначе "Достаточно"

# Пока фиксируем статус и лейбл вручную
status = "UNKNOWN"
label = "не определено"

if current_space >= total_space:
    status = "WARNING"
    label = "STOP"
else:
    status = "OK"
    label = "в норме"

# Расчёт для пайчарта
used_space = total_space - current_space
chart_data = [used_space, current_space]

# Результат
RESULT = {
    "title": "Свободное место на складе",
    "value": current_space,
    "status": status,
    "chart_type": "pie",
    "chart_data": chart_data,
    "category": "Логистика",
    "alerts": [
        f"Места {label} — {current_space} м²"
    ],
    "meta": {
        "unit": "м²",
        "checked_at": "now"
    }
}