def write_log(file, string):
    with open(file, 'a', encoding='utf-8') as log_file:
        log_file.write(string)


with open('registrations.txt', 'r', encoding='utf-8') as data_reg:
    for i_line in data_reg:
        i_string = i_line.split()
        try:
            if len(i_string) < 3:
                raise IndexError
            elif not i_string[0].isalpha():
                raise NameError
            elif not '@' in i_string[1] and not '.' in i_string[1]:
                raise SyntaxError
            elif int(i_string[2]) < 10 or int(i_string[2]) > 99:
                raise ValueError
            else:
                write_log('registrations_good.log', i_line)
        except IndexError:
            write_log('registrations_bad.log',
                      i_line.strip() + ' : НЕ присутствуют все три поля' + '\n')
        except NameError:
            write_log('registrations_bad.log',
                      i_line.strip() + ' : Поле имени содержит НЕ только буквы' + '\n')
        except SyntaxError:
            write_log('registrations_bad.log',
                      i_line.strip() + ' : Поле «Имейл» НЕ содержит @ и .(точку)' + '\n')
        except ValueError:
            write_log('registrations_bad.log',
                      i_line.strip() + ' : Поле «Возраст» НЕ является числом от 10 до 99' + '\n')
