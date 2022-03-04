guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print("Сейчас на вечеринке", len(guests), "человек", guests)

    guest = input("Гость пришёл или ушёл? ")
    if guest == "Пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break
    name = input("Имя гостя: ")
    if (guest == "пришёл") and (len(guests) < 6):
        print("Привет, ", name)
        guests.append(name)
    elif (guest == "пришёл") and (len(guests) == 6):
        print("Прости, ", name, "но мест нет")
    elif guest == "ушёл":
        print("Пока, ", name)
        guests.remove(name)

# зачтено
