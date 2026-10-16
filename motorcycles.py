motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

# Изменение первого элемента списка
# Чтобы изменить элемент, укажите имя списка и индекс изменяемого элемента в квадратных скобках
motorcycles[0] = 'ducati'
print(motorcycles) 

# Добавление нового элемента списка в конец списка
motorcycles.append('toyota')
print(motorcycles)

# Добавление новых элементов в пустой список 
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Добавление нового элемента в любое место списка
# Метод insert() позволяет добавить новый элемент в произвольную позицию списка
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'jeep')
print(motorcycles)

# Удаление элемента из списка
# Удаление элемента из списка, если известна позиция элемента, пользуйтесь командой del
motorcycles = ['jeep', 'honda', 'yamaha', 'suzuki']
del motorcycles[2]
print (motorcycles)

# Удаление последнего элемента из списка с помощью метода pop() 
motorcycles = ['jeep', 'honda', 'suzuki', 'yamaha']
print(motorcycles)
# Удаленный элеменный yamaha записывается в переменную popped_motocycles
popped_motocycles = motorcycles.pop()
print(motorcycles)
# Вывод удаленного элемента 
print(popped_motocycles)

motorcycles = ['jeep', 'honda', 'suzuki', 'yamaha']
print(motorcycles)
last_owned = motorcycles.pop()
print(motorcycles)
print(f"The last motorcycle I owned was a {last_owned.title()}\n")

# Вызов pop() может использоваться для удаления элемента в произвольной позиции 
# списка
motorcycles = ['jeep', 'honda', 'suzuki', 'yamaha']
first_owned = motorcycles.pop(1)
print(motorcycles)
print(f"The first motorcycle I owned was a {first_owned.title()}\n")

# Если вы собираетесь просто удалить элемент из списка, никак не используя его, выбирайте команду del
# Если же вы намерены использовать элемент после удаления из списка, выбирайте метод pop().

# Удаление элемента по значению с помощью метода remove() 
motorcycles = ['suzuki', 'honda', 'ducati', 'jeep', 'yamaha']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive) 
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")
