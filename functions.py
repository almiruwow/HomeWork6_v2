import random


def open_file():
    data = []
    with open('words.txt', 'r') as file:
        for word in file:
            data.append(word[:-1])

    return data


def mixing(word):
    new_word = ''.join(random.sample(word, len(word)))
    return new_word


def history(name, score):
    with open('history.txt', 'a') as file:
        file.write(name + ' ' + str(score) + '\n')


def results():
    data = []
    record = 0
    with open('history.txt', 'r') as file:
        for line in file:
            data.append(line[:-1])
            score = line.split(' ')[-1]
            if int(score[:-1]) > record:
                record = int(score[:-1])

    print(f'Всего игр сыграно: {len(data)}\n'
          f'Максимальный рекорд: {record}')

