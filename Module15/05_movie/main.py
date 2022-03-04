def check_film(f, n):
    for i in f:
        if n == i:
            return True
    return False


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
like_films = []
film = ""
while True:
    film = input("Введите название фильма: ")
    if film == "end":
        break
    if check_film(films, film) and not check_film(like_films, film):
        like_films.append(film)
    elif not check_film(films, film):
        print("Ошибка. Такого фильма нет")
    elif check_film(like_films, film):
        print("Ошибка. Такой фильм уже есть в списке")
print("Список любимых фильмов: ", like_films)

# зачтено
