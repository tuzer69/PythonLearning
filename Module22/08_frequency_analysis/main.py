def s_key(e):
    return e[0]


def int_key(e):
    return e[1]


text_dict = {}
dict_len = 0

with open('text.txt', 'r', encoding='utf-8') as f:
    for i_sym in f.read().lower():
        if i_sym.isalpha():
            if text_dict.get(i_sym, {}):
                text_dict[i_sym] += 1
            else:
                text_dict[i_sym] = 1
            dict_len += 1


with open('analysis.txt', 'w', encoding='utf-8') as fwrite:
    for i_sym in sorted(sorted(text_dict.items(), key=s_key, reverse=False),
                        key=int_key,
                        reverse=True):
        count = round(1 / dict_len * int(i_sym[1]), 3)
        w_str = f'{i_sym[0]}\t{str(count)}\n'
        fwrite.write(w_str)
