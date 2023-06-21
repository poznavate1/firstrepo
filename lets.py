def character_counter_v1(s):
    counter_for_ops = 0
    for sym in s:
        counter = 0
        for sub_sym in s:
            counter_for_ops += 1
            if sym == sub_sym:
                counter += 1
        print(f'количество "{sym}" = {counter}')
    print(counter_for_ops)


def character_counter_v2(s):
    counter_for_ops = 0
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            counter_for_ops += 1
            if sym == sub_sym:
                counter += 1
        print(f'количество "{sym}" = {counter}')
    print(counter_for_ops)

def character_counter_v3(s):
    counter_for_ops = 0 # счетчик операций, просто для наглядности эффективности решения
    syms_counter = {} # словарь для хранения пар символ: количество

def is_palindrome(word):
    return word == word[::-1]



    """
    Идея алгоритма следующая:
    берем букву
    обращаемся к словарю, где ключ будет буква
    Если этой буквы там еще не было, то она просто создастся
    После этого используем функцию get, чтобы получить значение по ключу буквы, 
    то сколько раз она уже встретилась в строке
    Если это её первое вхождение, то get вернет default значение 0 и мы прибавим к нему 1
    Если это не первое вхождение, то вернется текущее количество и прибавится 1
    """
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
        counter_for_ops += 1

    for sym, counter in syms_counter.items():
        print(f'количество "{sym}" = {counter}')
    print(f'{counter_for_ops=}')

word = input()
print(is_palindrome(word))



character_counter_v3("abccccssds")
