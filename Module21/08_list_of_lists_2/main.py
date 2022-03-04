nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def conv_list(lst):
    new_list = []
    for i_item in lst:
        if isinstance(i_item, list):
           new_list += conv_list(i_item)
        else:
            new_list.append(i_item)
    return new_list


print('Ответ:', conv_list(nice_list))
