"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
import random
random_number = random.randint(1, 101)
def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    start_ = 1
    final_ = 100
    while True:
        count += 1
        average_ = (start_ + final_) // 2
        if average_ == random_number:
            print(f'число {average_} найден за {count} попыток!')
            break  #выход из цикла, если угадали
        elif average_ > random_number:
            final_  = average_
        else:
            start_ = average_
            
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
