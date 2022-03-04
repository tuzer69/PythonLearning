violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]


def search_song(song, list_song):
    for i_song in list_song:
        if i_song[0] == song:
            return i_song[1]


minutes = 0
N = int(input("Сколько песен выбрать? "))
for i_s in range(N):
    print("Название ", i_s + 1, "песни: ", end='')
    minutes += search_song(input(), violator_songs)
print("Общее время звучания песен: ", round(minutes, 2), "минут")

# зачтено
