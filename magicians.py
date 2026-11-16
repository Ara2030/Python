magicians=['alice','david','carolina']
# Цикл for
# Python берет очередное имя из списка и 
# сохраняет его в переменной magician
# «Для каждого фокусника в списке вывести его имя»
for magician in magicians:
    print(magician)
    # «Для каждого фокусника в списке выведи отдельное сообщение»
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")