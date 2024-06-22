from random import choice

# варианты ответов
answers = ["бесспорно", "предрешено", "никаких сомнений", "определённо да","можешь быть уверен в этом",
           "мне кажется - да", "вероятнее всего", "хорошие перспективы", "знаки говорят - да", "да",
           "пока неясно, попробуй снова", "спроси позже", "лучше не рассказывать", "сейчас нельзя предсказать",
           "сконцентрируйся и спроси опять", "даже не думай", "мой ответ - нет", "по моим данным - нет",
           "перспективы не очень хорошие", "весьма сомнительно"]

print("Привет! Сейчас отвечу на все твои вопросы. Только сначала представься")
user_name = input("Тебя зовут: ")
while True:
    input(f"Твой вопрос, {user_name}: ")

    # TO DO добавить sleep и фразы типа "ожидайте"

    print(f"Ответ звезд: {user_name}, {choice(answers)}")
    again = input("Еще вопросы имеются? \nВведи 'да' или 'нет': ")
    while again.strip() not in ['да', 'нет']:
        print("Звезды понимают только 'да' и 'нет'")
        again = input("Введи 'да' или 'нет', я не шучу: ")
    if again.strip() == 'нет':
        print("Удачи, возвращайся!")
        break

