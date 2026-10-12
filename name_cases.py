# 2.3 Личное сообщение
name = "Eric"
message = f"Hello, {name}, would you like to learn some Python today?"
print(message)
# 2.4 Регистр символов в именах
name_2 = "john"
print(name_2.lower())
print(name_2.upper())
print(name_2.title())
# 2.5 Знаменитая цитата:
quote ='Albert Einstein once said "A person who never made a mistake never tried anything new."'
print(quote)
# 2.6 Знаменитая цитата 2:
famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)
# 2.6 Удаление пропусков:
name_3 = "\tEric\t"
print(name_3)
print(name_3.lstrip()) # lstrip() — удаляет пробельные символы слева, то есть в начале строки.
print(name_3.rstrip())# rstrip() — удаляет пробельные символы справа, то есть в конце строки.
print(name_3.strip())# strip() — удаляет пробельные символы с обеих сторон строки.

