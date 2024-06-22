from random import randint
from math import log2, ceil

# проверка на соответствие числа интервалу
def is_valid(user_input, low, upper):
    if user_input.isdigit() and low <= int(user_input) <= upper:
        return True
    else:
        return False

# TO DO
# вычисление шанса на победу
def chances_to_win(lower, upper, attempts):
    chance = 1/ ((upper - lower + 1)/2**attempts)
    chance = round(chance * 100, 2)
    if chance == 100:
        message = 'Шанса не угадать не существует'
        return chance, message
    if chance > 70:
        message = 'Шансы неплохие'
        return chance, message
    if chance > 50:
        message = 'Шансы есть'
        return chance, message

    message = 'Вы безумец... Или гений... Или все вместе...'
    return chance, message


print("Добро пожаловать в угадайку, Великолепный Угадайка")

#TO DO добавить ограничение, что старт должен быть натуральным
# старт случайной последовательности
lower_border = 0
while True:
    lower_border = input("\nЗадай нижнюю границу для случайного числа: ")
    if not lower_border.isdigit():
        print("\nА число будет сегодня? Или ты Великий Шутник? \nПоследняя попытка! (шутка)")
        continue
    lower_border = int(lower_border)
    print("Записала, идем дальше")
    break

# конец случайной последовательности
upper_border = 0
while True:
    upper_border = input("\nА теперь напиши верхнюю границу для случайного числа: ")
    if not upper_border.isdigit():
        print("\nА число будет сегодня? Или ты Великий Шутник? \nПоследняя попытка! (шутка)")
        continue
    upper_border = int(upper_border)
    print("Записала, идем дальше")
    break

random_num = randint(lower_border, upper_border)
print("\nНу что, поехали! Я свою ставку сделала. Выбери сложность игры:")
print(f"1. Легкая - если будешь играть по правилам, то точно угадаешь. Количество попыток "
      f"{ceil(log2(upper_border - lower_border + 1))}")
print(f"2. Средняя - оптимально, чтобы проверить свою интуицию, попыток в два раза меньше, то есть "
      f"{ceil(log2(upper_border - lower_border + 1)) // 2}")
print("3. Сложнейшая - невозможная для человека везучесть. Всего 1 (!) попытка")
attempt = 0
while True:
    lvl = input("Какую сложность ты выбрал? Укажи 1 (легкая), 2 (средняя) или 3 (невозможная): ")

    if lvl not in ['1', '2', '3']:
        print("\nМы будем повторять это, пока ты не начнешь играть по правилам! Только 1, 2 или 3!")
        continue

    if lvl == '1':
        attempt = ceil(log2(upper_border - lower_border + 1))
        # TO DO сделать склонение "попыток"
        print(f"\nОтличный выбор! У тебя будет {attempt} попыток")
        break

    if lvl == '2':
        attempt = ceil(log2(upper_border - lower_border + 1)) // 2
        # TO DO сделать склонение "попыток"
        print(f"Желаю удачи, будет достаточно сложно, но ты справишься! У тебя будет {attempt} попыток")
        # TO DO добавить расчет вероятности (оптимальной и безумной)
        # chance, message = chances_to_win(low_border, upper_border)
        # print(f"Небольшое предсказание. Шансы победить в процентах: {chance}. {message}")
        break

    attempt = 1
    print("А ты из тех, кто верит в удачу? Ну что ж, у тебя одна попытка... Знаешь, какие у тебя шансы угадать?")
    # TO DO add probability calculation (optimal and insane)
    # chance, message = chances_to_win(low_border, upper_border)
    # print(f"Небольшое предсказание. Шансы победить в процентах: {chance}. {message}")
    break

# игра!
# TO DO добавить возможность повторения игры
# TO DO добавить подсчет попыток, которые пользователь использовал
i = 1
is_win = False
while (i <= attempt):
    guess = input('\nВведи свое число: ')
    if not is_valid(guess, lower_border, upper_border):
        continue

    # проверка числа
    if (int(guess) < random_num):
        print("Загаданное число больше")
        i += 1
        continue
    if (int(guess) > random_num):
        print("Загаданное число меньше")
        i += 1
        continue
    is_win = True
    break
if is_win:
    print(f"Поздравляю! Ты угадал! Я загадала число {random_num} "
          f"\nСпасибо, что сыграл!")
else:
    print(f"В этот раз не повезло... Я загадала число {random_num} "
          f"\nНу, как говорится, не везет в угадайке, повезет в любви"
          f"\nСпасибо, что сыграл!")
