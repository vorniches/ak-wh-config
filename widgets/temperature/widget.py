# Уровень 2 — Условия

# Температура на складе
current_temperature = 150  # текущая температура в градусах
optimal_min = 16
optimal_max = 22

def tem_status(current_temperature, optimal_max, optimal_min):
    if current_temperature > optimal_max:
        status = "TOO_HOT"
        label = "жарко"
    elif current_temperature < optimal_min:
        status = "TOO_COLD"
        label = "холодно"
    else:
        status = "OK"
        label = "в норме"
        
    # print(status, label)
    return status

status = tem_status(current_temperature, optimal_max, optimal_min) #аргументы
print(status)
status = tem_status(28, 35, 10) #аргументы
print(status)

# # Данные для пайчарта (относительные проценты)
# chart_data = [
#     round(current_temperature),               # текущая температура
#     round((optimal_max + optimal_min) / 2)    # идеальная среда
# ]

# # Результат
# RESULT = {
#     "title": "Температура на складе",
#     "value": current_temperature,
#     "status": status,
#     "chart_type": "pie",
#     "chart_data": chart_data,
#     "category": "Климат-контроль",
#     "alerts": [
#         f"Температура {label} — {current_temperature}°C"
#     ],
#     "meta": {
#         "unit": "°C",
#         "checked_at": "now"
#     }
# }
