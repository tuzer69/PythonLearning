def shift_word(word, word_shift):
    word_ln = len(word)
    shift = word_shift % word_ln
    return ''.join([word[shift:], word[:shift]])


def word_decode(word: str, word_shift):
    correct_word = shift_word(word, word_shift)
    return ''.join([chr(ord(symbol) - 1) for symbol in correct_word])


def decode_text(txt: str):
    word_shift = -3
    for word in txt.split():
        if word.find('/') != -1:
            print(word_decode(word, word_shift))
            word_shift -= 1
        else:
            print(word_decode(word, word_shift), end=' ')


if __name__ == '__main__':
    txt = (
      'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm '
      'yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef '
      'uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf '
      'ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf '
      'Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv '
      'Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ '
      'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs '
      'uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op '
      'gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb '
      'Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ '
      'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
    )
    decode_text(txt)
