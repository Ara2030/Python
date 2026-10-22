cars = ['bmw','audi','toyota','subaru']
# Метод sort() позволяет относительно легко отсортировать список.
cars.sort()
print(cars)
# Названия машин располагаются в алфавитном порядке, и вернуться к 
# исходному порядку уже не удастся.

# Для отсортирование списка в обратном алфавитном порядке нужно методу
# sort передать аргумет reverse = True
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse = True)
print(cars)

# Функция sorted() позволяет временно представить список в определенном порядке, 
# но фактически не изменяет порядок элементов в списке
cars = ['bmw','audi','toyota','subaru']
print("Here is the orinal list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the orinal list again:")
print(cars)
# Функции sorted() также можно передать аргумент reverse = True,
# чтобы список был представлен в порядке, обратном алфавитному

#Вывод списка в обратном порядке reverse()
cars = ['bmw','audi','toyota','subaru']
print(cars)
# Метод reverse() не сортирует элементы в обратном алфавитном порядке, 
# а просто переходит к обратному порядку списка:
cars.reverse()
print(cars)
# С помощью повторного применение метода revers(),
# можете легко вернуться к исходному порядку списка
cars.reverse()
print(cars)

# Определение длинны списка методом len()
cars = ['bmw','audi','toyota','subaru']
print(len(cars))
