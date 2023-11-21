from functions import open_file, mixing, history, results

name = input('Введите ваше имя: ')
points = 0

for question in open_file():
    print(f'Угадайте слово: {mixing(question)}')
    user_input = input('Ваш ответ: ')
    if user_input == question:
        print('Верно! Вы получаете 10 очков.\n')
        points += 10
    else:
        print(f'Неверно! правильный ответ - {question}.\n')


history(name, points)
results()
