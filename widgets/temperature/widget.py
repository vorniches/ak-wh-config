# Температура на складе
current_temperature = 150  # текущая температура в градусах
optimal_max = 22 # оптимально максимальная
optimal_min = 16 # оптимально минимальная

# Условия
def tem_status(current_temperature, optimal_max, optimal_min): # функция с аргументами
    if current_temperature > optimal_max: # если
        status = "TOO_HOT"
        label = "жарко"
    elif current_temperature < optimal_min: # иначе если
        status = "TOO_COLD"
        label = "холодно"
    else: # иначе
        status = "OK"
        label = "в норме"
        
    # print(status, label)
    return status # возврат только статуса

status = tem_status(current_temperature, optimal_max, optimal_min) #аргументы
print(status) # печатает TOO_HOT, т к 150 > 22
status = tem_status(28, 35, 10) #аргументы
print(status) # 28 внутри диапазона, печатает ОК
status = tem_status(8, 25, 19)
print(status)

# current_temperature = 11  # текущая температура в градусах
# optimal_max = 33 # оптимально максимальная
# optimal_min = 17 # оптимально минимальная

# status = tem_status(current_temperature, optimal_max, optimal_min)
# print()

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
