def create_file(filename):
    f = open(filename, 'w', encoding='utf-8')
    f.close()


def write_log(filename, message):
    with open('chat.log', 'a', encoding='utf-8') as chat_log:
        chat_log.write(message + '\n')


def print_log(filename):
    with open('chat.log', 'r', encoding='utf-8') as chat_log:
        for i_line in chat_log:
            print(i_line)


def check_user(user):
    try:
        with open('users.txt', 'r', encoding='utf-8') as users_file:
            for i_user in users_file:
                if user.lower() == i_user.lower().strip():
                    raise ValueError
        return False
    except FileNotFoundError:
        print('Файл users.txt не обнаружен')
        create_file('users.txt')
    except ValueError:
        print('Такой пользователь уже существует, попробуйте еще раз')
        return True


user_name = input('Введите имя пользователя: ').lower()
while check_user(user_name):
    user_name = input('Введите имя пользователя: ').lower()

with open('users.txt', 'a', encoding='utf-8') as add_user:
    add_user.write(user_name + '\n')

while True:
    action = 0
    try:
        while action != 1 and action != 2:
            print('Выбелите действие: \n\t'
                  '1. Посмотреть текущий текст чата\n\t'
                  '2. Отправить сообщение')
            action = int(input())
    except ValueError:
        print('Выберите действие (1 или 2)!')
        action = int(input())
    if action == 1:
        try:
            print_log('chat.log')
        except FileNotFoundError:
            create_file('chat.log')
            print('Лог чата создан')
    else:
        message = input('Введите сообщение: ')
        write_log('chat.log', str(user_name + ': ' + message))
