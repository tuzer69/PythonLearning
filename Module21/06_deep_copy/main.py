site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def create_site(site):
    if isinstance(site, dict):
        for i_item in site.keys():
            if isinstance(site[i_item], dict):
                print(i_item, ':', '{', '\n\t', end='')
                if isinstance(site[i_item], dict):
                    create_site(site[i_item])
            else:
                print('\t', i_item + ':', site[i_item], '\n\t', end='')

    print('}', '\n\t', end='')

N = int(input('Сколько сайтов: '))

for i_site in range(N):
    print()
    _name = input('Введите название продукта для нового сайта: ')
    site['html']['head']['title'] = \
        'Куплю/продам {0} недорого'.format(_name)
    site['html']['body']['h2'] = \
        'У нас самая низкая цена на {0}'.format(_name)
    create_site(site)
