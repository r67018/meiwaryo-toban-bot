import numpy as np


def pretty_cure():
    rand_num = np.random.randint(2)
    text = ''

    if(rand_num == 0):
        text = 'ぷいきゅあー！がんばえー！'
    else:
        text = 'ぷいきゅあにちからおー！'

    return text


def cat():
    rand_num = np.random.randint(3)
    text = ''

    if(rand_num == 0):
        text = 'ねこかわいい'
    elif(rand_num == 1):
        text = '明和寮でねこ飼え'
    else:
        text = 'ねこぺろぺろ'

    return text


def omikuji():
    rand_num = int(np.random.rand() * 100)

    if rand_num > 95:
        return '大吉'
    elif rand_num > 80:
        return '中吉'
    elif rand_num > 55:
        return '吉'
    elif rand_num > 30:
        return '小吉'
    elif rand_num > 5:
        return '末吉'
    elif rand_num > 1:
        return '凶'
    else:
        return '大凶'
