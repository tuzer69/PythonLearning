violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

N = int(input("Сколько песен выбрать? "))
time = 0
for i_ in range(1, N + 1):
    print('Название', i_, 'песни:', end=' ')
    music = input()
    if violator_songs.get(music, {}):
        time += violator_songs[music]

print('Общее время звучания песен:', round(time, 2), 'минут')
