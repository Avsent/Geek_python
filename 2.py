# seconds = int(input('Введите время в секундах - '))
# minutes = seconds // 60
# hours = minutes // 60
# print(f'{hours}:{minutes % 60}:{seconds % 60}')

# ВАРИАНТ РЕШЕНИЯ ВЫШЕ - ПРОСТОЙ, НО НЕ ДАЕТ НУЖНЫЙ ФОРМАТ ВРЕМЕНИ, КОГДА РЕЗУЛЬТАТ ЕДИНИЦЫ ВРЕМЕНИ МЕНЬШЕ 10.
# НИЖЕ ПОПЫТАЛСЯ ИСПОЛЬЗОВАТЬ ТОЛЬКО БАЗУ ИЗ ПЕРВОГО УРОКА, НЕ ИСПОЛЬЗУЯ МОДУЛИ, КОТОРЫЕ ЕЩЕ НЕ ПРОХОДИЛИ:

seconds = int(input('Введите время в секундах - '))

sec_ost = seconds % 60
if sec_ost < 10:
    sec_ost = str(0) + str(sec_ost)

minutes = seconds // 60
min_ost = minutes % 60
if min_ost < 10:
    min_ost = str(0) + str(min_ost)

hours = minutes // 60
if hours < 10:
    hours = str(0) + str(hours)

print(f'{hours}:{min_ost}:{sec_ost}')
