from random import sample
from re import sub

# символы для пароля
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous_symbols = '[il1Lo0O]'


def is_contains(name_ru):
    while True:
        answer = input(f"Должны ли пароли содержать {name_ru} (да/нет): ")
        if answer.strip().lower() == 'да':
            return True
        if answer.strip().lower() == 'нет':
            return False
        # если введено что-то кроме "да" и "нет"
        print("Очень умно, но надо внимательно прочитать то, что в скобках")


def input_digit(name_ru):
    while True:
        digit = input(f"Введите {name_ru} (только цифры): ")
        if not digit.strip().isdigit():
            print("Очень умно, но надо внимательно прочитать то, что в скобках")
            continue
        return int(digit)


def generate_password(len, symbols):
    password = ''.join(sample(symbols, len))
    return password


# считать кол-во паролей
cnt_password = input_digit('число паролей')

# считать длину паролей
len_password = input_digit('длину паролей')

# включать ли цифры
is_contains_digits = is_contains('цифры')
# включать ли прописные буквы
is_contains_uppercase_letters = is_contains('прописные буквы')
# включать ли строчные буквы
is_contains_lower_letters = is_contains('строчные буквы')
# включать ли символы пунктуации
is_contains_punctuation = is_contains('символы пунктуации')
# включать ли неоднозначные символы il1Lo0O
is_contains_ambiguous_symbols = is_contains('неоднозначные символы')

print("Ваш запрос принят, вот ваши пароли:")

# собираем набор того, из чего может строиться пароль
symbols = ''
symbols += digits if is_contains_digits else ''
symbols += uppercase_letters if is_contains_uppercase_letters else ''
symbols += lowercase_letters if is_contains_lower_letters else ''
symbols += punctuation if is_contains_punctuation else ''

if not is_contains_ambiguous_symbols:
    symbols = sub(ambiguous_symbols, '', symbols)

# генерация пролей
# TO DO предусмотреть ситуацию, когда выбраны все четыре категории и только 3 символа в пароле
for _ in range(cnt_password):
    while True:
        password = generate_password(len_password, symbols)
        is_digit = any(c for c in password if c in digits) or not is_contains_digits
        is_lowercase = any(c for c in password if c in lowercase_letters) or not is_contains_lower_letters
        is_uppercase = any(c for c in password if c in uppercase_letters) or not is_contains_uppercase_letters
        is_punctuation = any(c for c in password if c in punctuation) or not is_contains_punctuation

        # если все нужные символы на месте
        if is_digit and is_lowercase and is_uppercase and is_punctuation:
            break
    print(password)
