# 3.4 Список гостей
guests = ['anna','emma','amelia','william']
invitation = (f"{guests[0].title()}, I’d like to invite you to lunch on Thursday at 1:30 PM.")
print(invitation)
invitation_2 = (f"{guests[1].title()}, I’d like to invite you to lunch on Thursday at 1:30 PM.")
print(invitation_2)
invitation_3 = (f"{guests[2].title()}, I’d like to invite you to lunch on Thursday at 1:30 PM.")
print(invitation_3)
invitation_4 = (f"{guests[3].title()}, I’d like to invite you to lunch on Thursday at 1:30 PM.")
print(invitation_4)

# 3.5 Изменение списка гостей
guests_2 = ['anna','emma','amelia','william']
popped_guest = guests_2[3]
print(f"{popped_guest.title()} can't make it.") # Вывод удаленного гостя 
guests_2[3] = 'jon' # Изменение списка гостей 
invitation_5 = (f"{guests_2[0].title()}, I’d like to invite you to lunch on Thursday at 1:30 PM.")
print(invitation_5)
invitation_6 = (f"{guests_2[1].title()}, I’d like to invite you to lunch on Thursday at 1:30 PM.")
print(invitation_6)
invitation_7 = (f"{guests_2[2].title()}, I’d like to invite you to lunch on Thursday at 1:30 PM.")
print(invitation_7)
invitation_8 = (f"{guests_2[3].title()}, I’d like to invite you to lunch on Thursday at 1:30 PM.")
print(invitation_8)

# 3.6 Больше гостей
guests_3 = ['anna','emma','amelia','william']
guests_3.insert(0, 'jon')  # Добавление нового гостя в начало списка
guests_3.insert(2, 'sarah')  # Добавление нового гостя в середину списка
guests_3.append('michael')  # Добавление нового гостя в конец списка
print(guests_3)  # Вывод обновленного списка гостей
invitation_9 = (f"{guests_3[0].title()}, I’d like to invite you to lunch on Thursday at 1:30 PM.")
print(invitation_9)
invitation_10 = (f"{guests_3[1].title()}, I’d like to invite you to lunch on Thursday at 1:30 PM.")
print(invitation_10)
invitation_11 = (f"{guests_3[2].title()}, I’d like to invite you to lunch on Thursday at 1:30 PM.")
print(invitation_11)
invitation_12 = (f"{guests_3[3].title()}, I’d like to invite you to lunch on Thursday at 1:30 PM.")
print(invitation_12)
invitation_13 = (f"{guests_3[4].title()}, I’d like to invite you to lunch on Thursday at 1:30 PM.")
print(invitation_13)
invitation_14 = (f"{guests_3[5].title()}, I’d like to invite you to lunch on Thursday at 1:30 PM.")
print(invitation_14)
invitation_15 = (f"{guests_3[6].title()}, I’d like to invite you to lunch on Thursday at 1:30 PM.")
print(invitation_15)

#3.7 Сокращение списка гостей
guests_4 = ['jon','anna','sarah','emma','amelia','william','michael']
print("Unfortunately, I can only invite two guests to lunch.")
popped_guest_1 = guests_4.pop()  # Удаление последнего гостя из списка
print(f"Sorry, {popped_guest_1.title()}, I can’t invite you to lunch.")
popped_guest_2 = guests_4.pop()
print(f"Sorry, {popped_guest_2.title()}, I can’t invite you to lunch.")
popped_guest_3 = guests_4.pop()
print(f"Sorry, {popped_guest_3.title()}, I can’t invite you to lunch.")
popped_guest_4 = guests_4.pop()
print(f"Sorry, {popped_guest_4.title()}, I can’t invite you to lunch.")
popped_guest_5 = guests_4.pop()
print(f"Sorry, {popped_guest_5.title()}, I can’t invite you to lunch.")
print(f"{guests_4[0].title()}, you are still invited to lunch.")
print(f"{guests_4[1].title()}, you are still invited to lunch.")
del guests_4[0]  # Удаление оставшихся гостей из списка
del guests_4[0]
print(guests_4)  # Вывод пустого списка гостей