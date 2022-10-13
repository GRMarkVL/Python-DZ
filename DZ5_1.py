
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Я удалю слова, которые содержат букву "а" Есенин лучшее

lukomorie = ' Не тужи, дорогой, и не ахай, \
Жизнь держи, как коня, за узду,\
Посылай всех и каждого на х*й,\
Чтоб тебя не послали в пиз*у!\
'
print("Исходный текст: ")
print(lukomorie)

def delite(lukomorie):
    lukomorie = list(filter(lambda x: 'о' not in x, lukomorie.split()))
    return " ".join(lukomorie)

lukomorie = delite(lukomorie)
print()
print("Текст, с удаленными словами, содержащими *о*: ")
print(lukomorie)