video_cards = [2060, 3070, 3060, 3090, 3070, 3090]
n_video_cards = []
print("Количество ведеокарт: ", len(video_cards))
for i in range(len(video_cards)):
    print(i + 1, "Видеокарта: ", video_cards[i])
print("Старый спискок видеокарт: ", video_cards)
max_n = 0
for i in video_cards:
    if i > max_n:
        max_n = i
for i in video_cards:
    if i != max_n:
        n_video_cards.append(i)
print("Новый список видеокарт: ", n_video_cards)

# зачтено
