# В Python список обозначается квадратными скобками [], а отдельные 
# элементы списка разделяются запятыми.
bicycles = ['trek','cannondale', 'redline', 'specialized']
print(bicycles)
# Для обращения к любому элементу списка следует сообщить Python индекс нужного 
# элемента. Индексы начинаются с нуля.
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
# Если запросить элемент с индексом –1, Python вернет последний элемент списка.
print(bicycles[-1])
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
