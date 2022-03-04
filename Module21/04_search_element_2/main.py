def search(key, words, depth=2):
    if key in words:
        return words[key]
    for sub_struct in words.values():
        if isinstance(sub_struct, dict):
            result = search(key, sub_struct, depth - 1)
            if result or depth == 0:
                break
    else:
        result = None

    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


N = input('Введите ключ: ')
dep = int(input('Введите глубину поиска: '))

value = search(N, site, dep)
if value:
    print(value)
else:
    print('Такой ключ не найдет!')
